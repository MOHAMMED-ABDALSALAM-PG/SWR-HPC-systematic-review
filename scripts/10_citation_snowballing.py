"""One round of backward and forward citation snowballing from the included studies (PRISMA 'other methods').
Backward: OpenAlex referenced_works + Crossref reference DOIs. Forward: OpenAlex works citing the seed.
Records already in the database set (by DOI or normalized title) are removed. Output: data_raw/snowball_<c>.csv (with abstracts),
queries/citation_snowballing_<c>.json (date, seeds, counts)."""
import csv, json, os, re, sys, time, datetime, unicodedata, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c = sys.argv[1]; seeds = [s.strip().lower() for s in open(sys.argv[2]) if s.strip()]
MAIL = os.environ.get('OPENALEX_MAILTO', '')
def get(u):
    for a in range(6):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'swr-review-snowballing/1.0'}), timeout=90))
        except Exception as e:
            if '404' in str(e): return None
            time.sleep(5 * (a + 1))
    return None
oa = lambda path, **p: get('https://api.openalex.org/' + path + ('?' + urllib.parse.urlencode({**p, **({'mailto': MAIL} if MAIL else {})}) if p or MAIL else ''))
def norm(t):
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower(); return re.sub(r'[^a-z0-9]+', '', t)
def inv(ab):
    if not ab: return ''
    return ' '.join(w for _, w in sorted((p, w) for w, ps in ab.items() for p in ps))
known = list(csv.DictReader(open(f'{ROOT}/data_raw/screening_{c}_with_abstracts.csv')))
kd = {r['doi'].lower() for r in known if r['doi']}; kt = {norm(r['title']) for r in known}
cand = {}; per_seed = {}
def add(w, how, seed):
    if not w: return
    doi = (w.get('doi') or '').replace('https://doi.org/', '').lower(); t = w.get('title') or w.get('display_name') or ''
    key = doi or norm(t)
    if not key or doi in kd or norm(t) in kt or doi in seeds: return
    r = cand.setdefault(key, dict(openalex_id=w.get('id', ''), doi=doi, year=w.get('publication_year', ''), title=t, type=w.get('type', ''),
                                  venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name', ''), abstract=inv(w.get('abstract_inverted_index')), found_via=set(), seeds=set()))
    r['found_via'].add(how); r['seeds'].add(seed)
SEL = 'id,doi,title,display_name,publication_year,type,primary_location,abstract_inverted_index,referenced_works'
for s in seeds:
    w = oa('works/doi:' + s) if not s.startswith('w') else oa('works/' + s)
    n_b = n_f = 0
    if w:
        refs = w.get('referenced_works') or []
        for i in range(0, len(refs), 50):
            ids = '|'.join(x.split('/')[-1] for x in refs[i:i + 50])
            d = oa('works', filter='openalex:' + ids, select=SEL.replace(',referenced_works', ''), **{'per-page': 50})
            for x in (d or {}).get('results', []): add(x, 'backward (OpenAlex)', s); n_b += 1
        cursor = '*'
        while cursor:
            d = oa('works', filter='cites:' + w['id'].split('/')[-1], select=SEL.replace(',referenced_works', ''), **{'per-page': 200, 'cursor': cursor})
            res = (d or {}).get('results', [])
            for x in res: add(x, 'forward (OpenAlex)', s); n_f += 1
            cursor = (d or {}).get('meta', {}).get('next_cursor') if res else None
    if not s.startswith('w'):
        cr = get('https://api.crossref.org/works/' + urllib.parse.quote(s))
        for ref in ((cr or {}).get('message') or {}).get('reference', []) or []:
            d = (ref.get('DOI') or '').lower()
            if d and d not in kd and d not in cand:
                x = oa('works/doi:' + d) or {'doi': d, 'title': ref.get('article-title') or ref.get('unstructured', '')[:200]}
                add(x, 'backward (Crossref)', s); n_b += 1
            time.sleep(0.1)
    per_seed[s] = dict(found=bool(w), backward=n_b, forward=n_f); print(s, per_seed[s], 'candidates so far', len(cand), flush=True)
rows = [dict(r, found_via='; '.join(sorted(r['found_via'])), seeds='; '.join(sorted(r['seeds']))) for r in cand.values()]
hdr = ['openalex_id', 'doi', 'year', 'title', 'type', 'venue', 'found_via', 'seeds', 'abstract']
with open(f'{ROOT}/data_raw/snowball_{c}.csv', 'w', newline='') as f:
    w_ = csv.DictWriter(f, hdr); w_.writeheader(); w_.writerows(rows)
json.dump(dict(date=datetime.date.today().isoformat(), seeds=per_seed, n_new_candidates=len(rows),
               note='candidates exclude records already in the database set'), open(f'{ROOT}/queries/citation_snowballing_{c}.json', 'w'), indent=1)
print('new candidate records', len(rows))
