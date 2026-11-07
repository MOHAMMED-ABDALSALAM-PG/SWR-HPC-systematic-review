"""Web of Science Core Collection via WoS Starter API (Free Trial plan: 1 req/s, 50 req/day).
Raw records -> data_raw/wos/ (not redistributed). Public: queries/wos_queries.json, hits/wos_<corpus>.csv."""
import os, json, time, csv, datetime, urllib.parse, urllib.request
KEY = os.environ['WOS_API_KEY']; ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUDGET = int(os.environ.get('WOS_BUDGET', '20')); used = 0
B = json.load(open(os.path.join(ROOT, 'queries', 'blocks.json')))
def wosify(s):  # Scopus -> WoS syntax
    return s.replace(' W/3 ', ' NEAR/3 ').replace('"voyage optimi?ation"', '"voyage optimization" OR "voyage optimisation"')
TS = lambda n: 'TS=(' + wosify(B[n]) + ')'
CORPORA = json.loads(os.environ.get('CORPORA', '{"A": ["R", "M", "W", "H"]}'))  # search v0.4: CORPORA='{"X": ["RX", "MX", "H"]}'
FILT = ' AND DT=(Article OR Proceedings Paper) AND LA=(English)'
def call(q, page, limit):
    global used
    if used >= BUDGET: raise SystemExit('budget reached')
    u = 'https://api.clarivate.com/apis/wos-starter/v1/documents?' + urllib.parse.urlencode({'db': 'WOS', 'q': q, 'limit': limit, 'page': page})
    r = urllib.request.Request(u, headers={'X-ApiKey': KEY}); used += 1
    resp = urllib.request.urlopen(r, timeout=90); left = resp.headers.get('x-ratelimit-remaining-day')
    d = json.load(resp); time.sleep(1.3); return d, left
log = {'source': 'Web of Science Core Collection (WoS Starter API v1, db=WOS)', 'date': datetime.date.today().isoformat(), 'corpora': {}}
os.makedirs(os.path.join(ROOT, 'data_raw', 'wos'), exist_ok=True)
for c, names in CORPORA.items():
    q = ' AND '.join(TS(n) for n in names); qf = q + FILT
    d, left = call(q, 1, 1); n_all = d['metadata']['total']
    recs, page = [], 1
    while True:
        d, left = call(qf, page, 50); recs += d['hits']
        n_f = d['metadata']['total']
        if len(recs) >= n_f or not d['hits']: break
        page += 1
    json.dump(recs, open(os.path.join(ROOT, 'data_raw', 'wos', f'corpus_{c}.json'), 'w'))
    with open(os.path.join(ROOT, 'hits', f'wos_{c}.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['doi', 'year', 'doctype', 'source_title'])
        for h in recs:
            w.writerow([((h.get('identifiers') or {}).get('doi') or '').lower(), (h.get('source') or {}).get('publishYear', ''), ';'.join(h.get('types') or []), (h.get('source') or {}).get('sourceTitle', '')])
    log['corpora'][c] = {'query': q, 'filters': FILT.strip(), 'count_all': n_all, 'count_filtered': n_f, 'retrieved': len(recs)}
    print(c, n_all, n_f, len(recs), 'calls used', used, 'day-left', left, flush=True)
json.dump(log, open(os.path.join(ROOT, 'queries', 'wos_queries' + os.environ.get('LOG_SUFFIX', '') + '.json'), 'w'), indent=1)
