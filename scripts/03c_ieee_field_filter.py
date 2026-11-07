"""IEEE Xplore API 'querytext' searches all metadata. To match the title/abstract/keyword scope used for Scopus
(TITLE-ABS-KEY) and WoS (TS=), the same concept blocks are evaluated on each IEEE record's title, abstract and
keywords (author keywords and index terms). Records failing any block are removed before deduplication."""
import json, os, re, sys, csv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, os.environ.get('RAW_DIR', 'data_raw'))
B = json.load(open(os.path.join(ROOT, 'queries', 'blocks.json')))
def tokenize(s): return re.findall(r'"[^"]*"|\(|\)|W/\d+|OR|AND|[^\s()"]+', s)
def term_rx(t):
    t = t.strip('"').lower()
    parts = [re.escape(w).replace(r'\*', r'\w*').replace(r'\?', r'\w?') for w in t.split()]
    return r'\b' + r'[\s\-]+'.join(parts) + r'\b'
def parse(tokens):
    def expr(i):
        node, i = atom(i); alts = [node]
        while i < len(tokens) and tokens[i] in ('OR',) or (i < len(tokens) and tokens[i].startswith('W/')):
            op = tokens[i]; nxt, i = atom(i + 1)
            if op == 'OR': alts.append(nxt)
            else: alts[-1] = ('NEAR', int(op[2:]), alts[-1], nxt)
        return ('OR', alts), i
    def atom(i):
        if tokens[i] == '(':
            n, i = expr(i + 1); return n, i + 1
        return ('T', term_rx(tokens[i])), i + 1
    return expr(0)[0]
def positions(node, text):
    k = node[0]
    if k == 'T': return [m.start() for m in re.finditer(node[1], text)]
    if k == 'OR': return sorted(p for a in node[1] for p in positions(a, text))
    if k == 'NEAR':
        a, b = positions(node[2], text), positions(node[3], text)
        words = lambda x, y: len(re.findall(r'\w+', text[min(x, y):max(x, y)]))
        return [x for x in a if any(words(x, y) <= node[1] + 1 for y in b)]
TREES = {n: parse(tokenize(s)) for n, s in B.items()}
CORP = json.loads(os.environ.get('CORPORA', '{"A": ["R", "M", "W", "H"]}'))  # search v0.4: CORPORA='{"X": ["RX", "MX", "H"]}'
def text_of(a):
    it = a.get('index_terms') or {}
    kw = []
    for v in it.values(): kw += v.get('terms', []) if isinstance(v, dict) else []
    return ' '.join([a.get('title', ''), a.get('abstract', ''), ' '.join(kw)]).lower()
if __name__ == '__main__':
    KEEP = {'Journals', 'Conferences', 'Early Access Articles'}
    log = json.load(open(os.path.join(ROOT, 'queries', 'ieee_queries' + os.environ.get('LOG_SUFFIX', '') + '.json')))
    for c, names in CORP.items():
        recs = [a for a in json.load(open(os.path.join(RAW, 'ieee', f'corpus_{c}.json'))) if a.get('content_type') in KEEP]
        ok = [a for a in recs if all(positions(TREES[n], text_of(a)) for n in names)]
        out = [dict(src='IEEE', doi=(a.get('doi') or '').lower(), title=a.get('title', ''), year=str(a.get('publication_year', '')),
                    venue=a.get('publication_title', ''), authors=((a.get('authors') or {}).get('authors') or [{}])[0].get('full_name', ''),
                    doctype=a.get('content_type', ''), abstract=a.get('abstract', ''),
                    kw='; '.join((a.get('index_terms') or {}).get('author_terms', {}).get('terms', []))) for a in ok]
        json.dump(out, open(os.path.join(RAW, f'extra_{c}.json'), 'w'))
        with open(os.path.join(ROOT, 'hits', f'ieee_{c}.csv'), 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['doi', 'year', 'content_type', 'title', 'source_title'])
            for a in ok: w.writerow([(a.get('doi') or '').lower(), a.get('publication_year', ''), a.get('content_type', ''), a.get('title', ''), a.get('publication_title', '')])
        log['corpora'][c]['count_field_restricted'] = len(ok)
        log['corpora'][c]['field_restriction'] = 'blocks evaluated on title, abstract and keywords (equivalent to TITLE-ABS-KEY)'
        print(c, 'content-type filtered', len(recs), '-> title/abstract/keywords', len(ok))
    json.dump(log, open(os.path.join(ROOT, 'queries', 'ieee_queries' + os.environ.get('LOG_SUFFIX', '') + '.json'), 'w'), indent=1)
