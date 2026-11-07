"""Figure: included studies by tier, (a) evidence class and (b) dominant parallelism level.
Tier and evidence class come from the extraction sheet; the dominant parallelism level of each study (K kernel or
data-parallel, L label-level, S segment, P population-level, J job-level) is the one given in the year table of the
manuscript (Table 6) and is derived here from the extraction column parallelism_level.
usage: 16_fig_evidence_parallelism.py EXTRACTION_CSV OUT.pdf"""
import collections, csv, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

EXT, OUT = sys.argv[1:3]
rows = list(csv.DictReader(open(EXT, encoding='utf-8')))
key = lambda r: r['rec_id_or_key'].split('=')[-1].strip()
tier = {key(r): r['tier'] for r in rows}
evid = {key(r): r['evidence_class'] for r in rows}
def dominant(text):
    t = text.strip().lower()
    for prefix, code in (('label', 'L'), ('segment', 'S'), ('population', 'P'), ('job', 'J')):
        if t.startswith(prefix): return code
    return 'K'
level = {key(r): dominant(r['parallelism_level']) for r in rows}
assert collections.Counter(level.values()) == {'K': 10, 'L': 2, 'S': 2, 'P': 1, 'J': 2}, collections.Counter(level.values())

TIERS = ['A2', 'A1']                      # bottom to top
n = collections.Counter(tier.values())
labels = [f'Tier {x} (n={n[x]})' for x in TIERS]
C = plt.rcParams['axes.prop_cycle'].by_key()['color']
panels = [('(a) Performance-evidence classes', evid, ['E-S', 'E-C', 'E-T'], C[:3]),
          ('(b) Dominant parallelism levels', level, ['K', 'L', 'S', 'P', 'J'], C[:5])]
fig, axes = plt.subplots(1, 2, figsize=(13.2, 4.2))
for ax, (title, cls, cats, cols) in zip(axes, panels):
    left = [0] * len(TIERS)
    for c, col in zip(cats, cols):
        v = [sum(1 for k in tier if tier[k] == x and cls[k] == c) for x in TIERS]
        ax.barh(labels, v, left=left, color=col, edgecolor='white', linewidth=1.2, height=0.5, label=c)
        for i, x in enumerate(v):
            if x: ax.text(left[i] + x / 2, i, str(x), ha='center', va='center', color='white', fontsize=12.5, fontweight='bold')
        left = [a + b for a, b in zip(left, v)]
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.set_xlim(0, 12); ax.set_xticks(range(0, 13, 2)); ax.set_xlabel('Number of included studies', fontsize=11)
    ax.tick_params(axis='y', labelsize=11, length=0); ax.tick_params(axis='x', labelsize=10)
    ax.grid(axis='x', color='#e6e6e6', linewidth=0.8); ax.set_axisbelow(True)
    for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=len(cats), frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(OUT, bbox_inches='tight')
for x in TIERS:
    print(x, n[x], {c: sum(1 for k in tier if tier[k] == x and evid[k] == c) for c in ('E-S', 'E-C', 'E-T')},
          {c: sum(1 for k in tier if tier[k] == x and level[k] == c) for c in 'KLSPJ'})
