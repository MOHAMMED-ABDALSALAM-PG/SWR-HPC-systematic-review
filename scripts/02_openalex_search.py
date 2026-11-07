"""OpenAlex supplementary search (title+abstract). OpenAlex has no wildcards/proximity,
so the Scopus blocks are expanded into explicit word forms (recorded in queries/openalex_queries.json)."""
import json, os, time, csv, datetime, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = os.environ.get('OPENALEX_MAILTO', '')
OR = lambda xs: '(' + ' OR '.join(f'"{x}"' if ' ' in x or '-' in x else x for x in xs) + ')'
R = ['weather routing','ship routing','vessel routing','voyage optimization','voyage optimisation','voyage planning','route optimization','route optimisation','route planning','routing optimization','path planning','path optimization','path search','route search','optimal route','optimal path','optimal planning','trajectory optimization','trajectory planning','route finding','path finding','pathfinding']
M = ['ship','ships','vessel','vessels','maritime','sailboat','sailboats','sailing','yacht','ferry','ferries','marine vehicle','marine vehicles']
W = ['weather','meteorological','metocean','meteo-oceanographic','wave','waves','wind','winds','current','currents','ocean flow','ocean flows','ocean environment','sea state','forecast','forecasts','sailboat','sailing']
H = ['high performance computing','high-performance computing','HPC','parallel','parallelization','parallelisation','parallelized','GPU','GPUs','graphics processing unit','CUDA','OpenCL','OpenMP','MPI','message passing','multicore','multi-core','multithreaded','multithreading','multi-threaded','supercomputer','supercomputing','distributed computing','cloud computing','computing cluster','HPC cluster','island model','many-core','FPGA']
RX = R + ['collision avoidance', 'collision-avoidance', 'anti-collision', 'obstacle avoidance', 'motion planning', 'shortest path', 'shortest paths',
            'search and rescue', 'route generation', 'path generation', 'route construction', 'route selection', 'route building', 'building a route',
            'path optimisation', 'trajectory optimisation', 'route computation', 'path computation']
MX = M + ['AUV', 'AUVs', 'autonomous underwater vehicle', 'autonomous underwater vehicles', 'underwater vehicle', 'underwater vehicles',
            'underwater glider', 'underwater gliders', 'ocean glider', 'ocean gliders', 'sea glider', 'seaglider', 'USV', 'USVs',
            'unmanned surface vehicle', 'unmanned surface vehicles', 'unmanned surface vessel', 'unmanned surface vessels',
            'autonomous surface vehicle', 'autonomous surface vehicles', 'autonomous surface vessel', 'autonomous surface vessels',
            'surface vehicle', 'surface vehicles', 'autonomous ship', 'autonomous ships', 'autonomous vessel', 'autonomous vessels',
            'maritime autonomous surface ship', 'boat', 'boats', 'marine robot', 'marine robots', 'ocean vehicle', 'ocean vehicles', 'marine craft']
LISTS = {'R': R, 'M': M, 'W': W, 'H': H, 'RX': RX, 'MX': MX}
CORPORA = {c: [LISTS[n] for n in names] for c, names in json.loads(os.environ.get('CORPORA', '{"A": ["R", "M", "W", "H"]}')).items()}
def get(params):
    u = 'https://api.openalex.org/works?' + urllib.parse.urlencode(params)
    for a in range(8):
        try:
            d = json.load(urllib.request.urlopen(u, timeout=90)); time.sleep(0.3); return d
        except Exception as e:
            time.sleep(4 * (a + 1))
    raise RuntimeError(u)
def inv(ab):
    if not ab: return ''
    pos = sorted((p, w) for w, ps in ab.items() for p in ps); return ' '.join(w for _, w in pos)
log = {'source': 'OpenAlex (title_and_abstract.search)', 'date': datetime.date.today().isoformat(), 'corpora': {}}
os.makedirs(os.path.join(ROOT, 'hits'), exist_ok=True)
for c, blocks in CORPORA.items():
    q = ' AND '.join(OR(b) for b in blocks)
    base = {'filter': 'title_and_abstract.search:' + q, **({'mailto': MAIL} if MAIL else {})}
    n_all = get({**base, 'per-page': 1})['meta']['count']
    flt = 'title_and_abstract.search:' + q + ',type:article|proceedings-article,language:en'
    recs, cursor = [], '*'
    while cursor:
        d = get({'filter': flt, 'per-page': 200, 'cursor': cursor, **({'mailto': MAIL} if MAIL else {})})
        recs += d['results']; cursor = d['meta'].get('next_cursor') if d['results'] else None
    with open(os.path.join(ROOT, 'hits', f'openalex_{c}.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['openalex_id', 'doi', 'year', 'type', 'title', 'source_title', 'abstract'])
        for r in recs:
            w.writerow([r['id'], (r.get('doi') or '').replace('https://doi.org/', '').lower(), r.get('publication_year'), r.get('type'), r.get('title') or '', ((r.get('primary_location') or {}).get('source') or {}).get('display_name', ''), inv(r.get('abstract_inverted_index'))])
    log['corpora'][c] = {'query': q, 'filters': 'type:article|proceedings-article, language:en', 'count_all': n_all, 'count_filtered': len(recs)}
    print(c, n_all, len(recs), flush=True)
json.dump(log, open(os.path.join(ROOT, 'queries', 'openalex_queries' + os.environ.get('LOG_SUFFIX', '') + '.json'), 'w'), indent=1)
