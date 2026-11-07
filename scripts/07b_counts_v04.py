"""PRISMA 2020 counts for search v0.4, computed from the released query logs and decision files.
Writes counts/prisma_counts.json (every count reported in the manuscript; keys are the names used there)."""
import csv, json, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = lambda f: json.load(open(f'{ROOT}/queries/{f}'))
sc, wo, ie, oa, ch = (q('scopus_queries_v04.json'), q('wos_queries_v04.json'), q('ieee_queries_v04.json'),
                      q('openalex_queries_v04.json'), q('citation_snowballing_X.json'))
dec = list(csv.DictReader(open(f'{ROOT}/screening/decisions_databases_v04.csv')))
om = list(csv.DictReader(open(f'{ROOT}/screening/decisions_other_methods_v04.csv')))
W = {'I1': 'Ione', 'I2': 'Itwo', 'I3': 'Ithree', 'I4': 'Ifour', 'E1': 'Eone', 'E2': 'Etwo', 'E3': 'Ethree', 'E4': 'Efour', 'E5': 'Efive', 'author decision': 'AD'}
C = dict(searchDate=sc['date'], ieeeDate=ie['date'], openalexDate=oa['date'], chaseDate=ch['date'],
         nScopusRawA=sc['corpora']['X']['counts']['all'], nScopusA=sc['corpora']['X']['counts']['doctype+english'],
         nWoSRawA=wo['corpora']['X']['count_all'], nWoSA=wo['corpora']['X']['count_filtered'],
         nIEEERawA=ie['corpora']['X']['count_all'], nIEEEA=ie['corpora']['X']['count_field_restricted'],
         nOpenAlexRawA=oa['corpora']['X']['count_all'], nOpenAlexA=oa['corpora']['X']['count_filtered'])
C['nIdentifiedA'] = C['nScopusA'] + C['nWoSA'] + C['nIEEEA'] + C['nOpenAlexA']
C['nUniqueA'] = C['nTAScreenedA'] = len(dec); C['nDuplicatesA'] = C['nIdentifiedA'] - len(dec)
ft = [d for d in dec if d['stage'] == 'full text']
C['nTAExcludedA'] = len(dec) - len(ft); C['nSoughtA'] = len(ft)
C['nNotRetrievedA'] = sum(d['decision'] == 'not_retrieved' for d in ft); C['nFullTextA'] = len(ft) - C['nNotRetrievedA']
ex = collections.Counter(d['code'] for d in ft if d['decision'] == 'exclude')
for k, w in W.items(): C[f'nFTx{w}A'] = ex.get(k, 0)
C['nFTExcludedA'] = sum(ex.values()); inc = [d for d in ft if d['decision'] == 'include']; C['nIncludedDbA'] = len(inc)
known = [r for r in om if r['found_via'] == 'known to the authors']
C['nCitChaseA'] = ch['n_new_candidates']; C['nKnownA'] = len(known)
C['nOtherRemovedA'] = sum(r['decision'] == 'duplicate' for r in om)
C['nOtherScreenedA'] = C['nCitChaseA'] + C['nKnownA'] - C['nOtherRemovedA']
oft = [r for r in om if r['stage'] == 'full text']
C['nOtherSoughtA'] = len(oft); C['nOtherTAExcludedA'] = C['nOtherScreenedA'] - len(oft)
C['nOtherNotRetrievedA'] = sum(r['decision'] == 'not_retrieved' for r in oft); C['nOtherAssessedA'] = len(oft) - C['nOtherNotRetrievedA']
oex = collections.Counter(r['code'] for r in oft if r['decision'] == 'exclude')
for k, w in W.items(): C[f'nOx{w}A'] = oex.get(k, 0)
C['nOtherExcludedA'] = sum(oex.values()); C['nOtherMethodsA'] = sum(r['decision'] == 'include' for r in oft)
C['nIncludedA'] = C['nIncludedDbA'] + C['nOtherMethodsA']
C['nIncludedAone'] = sum(d['tier'] == 'A1' for d in inc); C['nIncludedAtwo'] = sum(d['tier'] == 'A2' for d in inc)
os.makedirs(f'{ROOT}/counts', exist_ok=True)
with open(f'{ROOT}/counts/prisma_counts.json', 'w') as f:
    json.dump(C, f, indent=1)
print(json.dumps(C))
