"""Merge Scopus, WoS, OpenAlex and IEEE Xplore hits; deduplicate by DOI, then normalized title + year (+-1).
Output: dedup/dedup_log_<c>.csv and dedup/records_<c>.csv (no abstracts); the screening sheet with abstracts stays local."""
import json, csv, os, re, unicodedata, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def norm(t):
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', re.sub(r'<[^>]+>', '', t)).strip()
MATCH = {'new': 'first occurrence', 'doi': 'duplicate (same DOI)', 'title+year': 'duplicate (same title, year within 1)'}
def write_log(path, log, titles):
    """log: retrieval-ordered (rec_id, source, doi, year, match) tuples. Rows are written grouped by record (first
    occurrence, then its duplicates); `order` keeps the retrieval order on which the matching depends."""
    rows = [dict(rec_id=r, record_title=titles.get(r, ''), source=s, doi=d, year=y, match=MATCH[m], order=i + 1) for i, (r, s, d, y, m) in enumerate(log)]
    rows.sort(key=lambda x: (x['rec_id'], x['order']))
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, ['rec_id', 'record_title', 'source', 'doi', 'year', 'match', 'order']); w.writeheader(); w.writerows(rows)
def load(c):
    out = []
    for e in json.load(open(f'{ROOT}/data_raw/scopus/corpus_{c}.json')):
        out.append(dict(src='Scopus', doi=(e.get('prism:doi') or '').lower(), title=e.get('dc:title', ''), year=(e.get('prism:coverDate') or '')[:4],
                        venue=e.get('prism:publicationName', ''), authors=e.get('dc:creator', ''), doctype=e.get('subtypeDescription', ''), abstract=e.get('dc:description') or '', kw=e.get('authkeywords') or ''))
    for h in json.load(open(f'{ROOT}/data_raw/wos/corpus_{c}.json')):
        s = h.get('source') or {}; au = ((h.get('names') or {}).get('authors') or [{}])
        out.append(dict(src='WoS', doi=((h.get('identifiers') or {}).get('doi') or '').lower(), title=h.get('title', ''), year=str(s.get('publishYear', '')),
                        venue=s.get('sourceTitle', ''), authors=au[0].get('displayName', '') if au else '', doctype=';'.join(h.get('types') or []), abstract='', kw=';'.join((h.get('keywords') or {}).get('authorKeywords') or [])))
    oa = f'{ROOT}/hits/openalex_{c}.csv'
    for r in (csv.DictReader(open(oa)) if os.path.exists(oa) else []):
        out.append(dict(src='OpenAlex', doi=r['doi'], title=r['title'], year=r['year'], venue=r['source_title'], authors='', doctype=r['type'], abstract=r['abstract'], kw=''))
    extra = f'{ROOT}/data_raw/extra_{c}.json'   # IEEE Xplore records, field-restricted (written by 03c_ieee_field_filter.py)
    if os.path.exists(extra): out += json.load(open(extra))
    return out
os.makedirs(f'{ROOT}/dedup', exist_ok=True)
for c in os.environ.get('DEDUP_CORPORA', 'A').split(','):
    recs = load(c); groups = []; by_doi = {}; by_title = collections.defaultdict(list); log = []
    for r in recs:
        g = None
        if r['doi'] and r['doi'] in by_doi: g = by_doi[r['doi']]; why = 'doi'
        else:
            for gi in by_title.get(norm(r['title']), []):
                ys = {x['year'] for x in groups[gi]}
                if not r['year'] or any(y and abs(int(y) - int(r['year'])) <= 1 for y in ys if y.isdigit() and r['year'].isdigit()): g = gi; why = 'title+year'; break
        if g is None: groups.append([]); g = len(groups) - 1; why = 'new'
        groups[g].append(r); log.append((f'{c}{g+1:04d}', r['src'], r['doi'], r['year'], why))
        if r['doi']: by_doi[r['doi']] = g
        by_title[norm(r['title'])].append(g)
    rows = []
    for gi, rs in enumerate(groups):
        best = lambda f: max((x[f] for x in rs), key=len)
        rows.append(dict(rec_id=f'{c}{gi+1:04d}', sources='+'.join(sorted({x['src'] for x in rs})), doi=best('doi'), year=best('year'), title=best('title'),
                         venue=best('venue'), first_author=best('authors'), doctype=best('doctype'), abstract=best('abstract'), keywords=best('kw')))
    pub = ['rec_id', 'sources', 'doi', 'year', 'title', 'venue', 'first_author', 'doctype']
    with open(f'{ROOT}/dedup/records_{c}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, pub, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
    with open(f'{ROOT}/data_raw/screening_{c}_with_abstracts.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, pub + ['keywords', 'abstract']); w.writeheader(); w.writerows(rows)
    write_log(f'{ROOT}/dedup/dedup_log_{c}.csv', log, {r['rec_id']: r['title'] for r in rows})
    cnt = collections.Counter(r['src'] for r in recs)
    print(c, dict(cnt), 'total', len(recs), 'unique', len(groups), 'duplicates removed', len(recs) - len(groups),
          'by source combo', collections.Counter(r['sources'] for r in rows).most_common())
