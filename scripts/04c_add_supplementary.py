"""Add OpenAlex (supplementary) records to an existing deduplicated set without renumbering it.
Records matching an existing record by DOI, or by normalized title with years within +-1, are logged as duplicates;
the rest get new ids after the last existing one."""
import csv, os, re, sys, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c = sys.argv[1] if len(sys.argv) > 1 else 'X'
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
def read_log(path):
    rows = sorted(csv.DictReader(open(path, encoding='utf-8')), key=lambda x: int(x['order']))
    back = {v: k for k, v in MATCH.items()}
    return [(x['rec_id'], x['source'], x['doi'], x['year'], back[x['match']]) for x in rows]
P = f'{ROOT}/data_raw/screening_{c}_with_abstracts.csv'
rows = list(csv.DictReader(open(P))); hdr = list(rows[0].keys())
pub = ['rec_id', 'sources', 'doi', 'year', 'title', 'venue', 'first_author', 'doctype']
by_doi = {r['doi']: r for r in rows if r['doi']}
by_t = {}
for r in rows: by_t.setdefault(norm(r['title']), []).append(r)
def yr_ok(a, b): return not a or not b or not a.isdigit() or not b.isdigit() or abs(int(a) - int(b)) <= 1
n = max(int(r['rec_id'][1:]) for r in rows); log = []; new = []
for o in csv.DictReader(open(f'{ROOT}/hits/openalex_{c}.csv')):
    m = by_doi.get(o['doi']) if o['doi'] else None
    why = 'doi' if m else ''
    if not m:
        m = next((r for r in by_t.get(norm(o['title']), []) if yr_ok(r['year'], str(o['year']))), None); why = 'title+year' if m else ''
    if m:
        if 'OpenAlex' not in m['sources']: m['sources'] = '+'.join(sorted(m['sources'].split('+') + ['OpenAlex']))
        if len(m.get('abstract', '')) < 80 and len(o['abstract']) >= 80: m['abstract'] = o['abstract']; m['abstract_source'] = 'openalex'
        log.append((m['rec_id'], 'OpenAlex', o['doi'], o['year'], why)); continue
    n += 1
    r = dict(rec_id=f'{c}{n:04d}', sources='OpenAlex', doi=o['doi'], year=str(o['year']), title=o['title'], venue=o['source_title'],
             first_author='', doctype=o['type'], keywords='', abstract=o['abstract'], abstract_source='openalex')
    rows.append(r); new.append(r); by_doi[r['doi']] = r; by_t.setdefault(norm(r['title']), []).append(r)
    log.append((r['rec_id'], 'OpenAlex', o['doi'], o['year'], 'new'))
with open(P, 'w', newline='') as f:
    w = csv.DictWriter(f, hdr, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
with open(f'{ROOT}/dedup/records_{c}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, pub, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
L = f'{ROOT}/dedup/dedup_log_{c}.csv'
write_log(L, read_log(L) + log, {r['rec_id']: r['title'] for r in rows})
print('OpenAlex records', len(log), 'duplicates of existing', len(log) - len(new), 'new', len(new), 'total unique', len(rows))
open(f'{ROOT}/data_raw/new_openalex_{c}.txt', 'w').write('\n'.join(r['rec_id'] for r in new) + '\n')
