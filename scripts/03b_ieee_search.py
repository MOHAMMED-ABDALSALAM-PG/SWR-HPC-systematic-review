"""IEEE Xplore search (IEEE Xplore Metadata Search API, querytext over metadata and abstract).
Raw responses -> data_raw/ieee/ (not redistributed). Public: queries/ieee_queries.json, hits/ieee_<corpus>.csv."""
import os, json, time, csv, datetime, urllib.parse, urllib.request
KEY = os.environ['IEEE_API_KEY']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, os.environ.get('RAW_DIR', 'data_raw'), 'ieee')
B = json.load(open(os.path.join(ROOT, 'queries', 'blocks.json')))
conv = lambda s: s.replace(' W/3 ', ' NEAR/3 ').replace('"voyage optimi?ation"', '"voyage optimization" OR "voyage optimisation"')
CORPORA = json.loads(os.environ.get('CORPORA', '{"A": ["R", "M", "W", "H"]}'))  # search v0.4: CORPORA='{"X": ["RX", "MX", "H"]}'
KEEP = {'Journals', 'Conferences', 'Early Access Articles'}
def call(q, start):
    u = 'https://ieeexploreapi.ieee.org/api/v1/search/articles?' + urllib.parse.urlencode(
        {'apikey': KEY, 'format': 'json', 'max_records': 200, 'start_record': start, 'querytext': q, 'sort_field': 'article_number', 'sort_order': 'asc'})
    d = json.load(urllib.request.urlopen(u, timeout=90)); time.sleep(1.0); return d
os.makedirs(RAW, exist_ok=True); os.makedirs(os.path.join(ROOT, 'hits'), exist_ok=True)
log = {'source': 'IEEE Xplore (Metadata Search API, querytext)', 'date': datetime.date.today().isoformat(), 'corpora': {}}
for c, names in CORPORA.items():
    q = ' AND '.join('(' + conv(B[n]) + ')' for n in names)
    recs, start = [], 1
    while True:
        d = call(q, start); arts = d.get('articles', []); recs += arts
        total = d.get('total_records', 0); start += 200
        if not arts or start > total: break
    json.dump(recs, open(os.path.join(RAW, f'corpus_{c}.json'), 'w'))
    kept = [a for a in recs if a.get('content_type') in KEEP]
    with open(os.path.join(ROOT, 'hits', f'ieee_{c}.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['doi', 'year', 'content_type', 'title', 'source_title'])
        for a in kept:
            w.writerow([(a.get('doi') or '').lower(), a.get('publication_year', ''), a.get('content_type', ''), a.get('title', ''), a.get('publication_title', '')])
    log['corpora'][c] = {'query': q, 'filters': 'content type: Journals, Conferences, Early Access Articles', 'count_all': total, 'count_filtered': len(kept)}
    print(c, total, len(kept), flush=True)
json.dump(log, open(os.path.join(ROOT, 'queries', 'ieee_queries' + os.environ.get('LOG_SUFFIX', '') + '.json'), 'w'), indent=1)
