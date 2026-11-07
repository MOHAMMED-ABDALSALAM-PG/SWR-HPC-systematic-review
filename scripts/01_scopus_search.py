"""Scopus search (SWR x HPC).
Raw responses are stored under data_raw/ (not redistributed, Elsevier API terms).
Public outputs: queries/scopus_queries.json (strings, date, counts) and hits/scopus_<corpus>.csv (EID-free: DOI, year, doctype, source title only)."""
import os, json, time, csv, datetime, urllib.parse, urllib.request
KEY = os.environ['ELSEVIER_API_KEY']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKS = json.load(open(os.path.join(ROOT, 'queries', 'blocks.json')))
def q_of(names): return ' AND '.join('TITLE-ABS-KEY(' + BLOCKS[n] + ')' for n in names)
CORPORA = json.loads(os.environ.get('CORPORA', '{"A": ["R", "M", "W", "H"]}'))  # search v0.4: CORPORA='{"X": ["RX", "MX", "H"]}'
FILTERS = [('all', ''), ('doctype', ' AND DOCTYPE(ar OR cp)'), ('doctype+english', ' AND DOCTYPE(ar OR cp) AND LANGUAGE(english)')]

def call(params):
    u = 'https://api.elsevier.com/content/search/scopus?' + urllib.parse.urlencode(params)
    r = urllib.request.Request(u, headers={'X-ELS-APIKey': KEY, 'Accept': 'application/json'})
    for attempt in range(5):
        try:
            d = json.load(urllib.request.urlopen(r, timeout=90)); time.sleep(0.4); return d
        except Exception as e:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError('Scopus call failed')

log = {'source': 'Scopus (Elsevier Search API, view=COMPLETE)', 'date': datetime.date.today().isoformat(), 'corpora': {}}
os.makedirs(os.path.join(ROOT, 'data_raw', 'scopus'), exist_ok=True)
os.makedirs(os.path.join(ROOT, 'hits'), exist_ok=True)
for c, names in CORPORA.items():
    base = q_of(names); entry = {'blocks': names, 'counts': {}}
    for fname, f in FILTERS:
        d = call({'query': base + f, 'count': 1, 'view': 'STANDARD'})
        entry['counts'][fname] = int(d['search-results']['opensearch:totalResults'])
    final = base + FILTERS[-1][1]; entry['final_query'] = final
    recs, start = [], 0
    while True:
        d = call({'query': final, 'count': 25, 'start': start, 'view': 'COMPLETE'})
        es = [e for e in d['search-results'].get('entry', []) if 'error' not in e]
        recs += es; start += 25
        if not es or start >= entry['counts']['doctype+english']: break
    json.dump(recs, open(os.path.join(ROOT, 'data_raw', 'scopus', f'corpus_{c}.json'), 'w'))
    entry['retrieved'] = len(recs)
    with open(os.path.join(ROOT, 'hits', f'scopus_{c}.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['doi', 'year', 'doctype', 'source_title'])
        for e in recs:
            w.writerow([(e.get('prism:doi') or '').lower(), (e.get('prism:coverDate') or '')[:4], e.get('subtypeDescription', ''), e.get('prism:publicationName', '')])
    log['corpora'][c] = entry; print(c, entry['counts'], 'retrieved', len(recs), flush=True)
os.makedirs(os.path.join(ROOT, 'queries'), exist_ok=True)
json.dump(log, open(os.path.join(ROOT, 'queries', 'scopus_queries' + os.environ.get('LOG_SUFFIX', '') + '.json'), 'w'), indent=1)
