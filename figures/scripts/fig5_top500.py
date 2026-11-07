"""Figure 7: HPL performance of the June TOP500 lists, 1993-2026 (sum, #1, #500).
Data: TOP500 Performance Development (https://top500.org/statistics/perfdevel/), retrieved 2026-09-30,
stored in ../data/top500_perfdevel_GFlops.csv. Values in GFlop/s.
Single-column figure (3.5 in wide); fonts >= 7 pt; Arial-compatible font (Liberation Sans where available)."""
import csv, matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, LogLocator, NullFormatter

import os
HERE = os.path.dirname(os.path.abspath(__file__))
for f in fm.findSystemFonts():
    if os.path.basename(f).startswith('LiberationSans'): fm.fontManager.addfont(f)
FONT = 'Liberation Sans' if any(x.name == 'Liberation Sans' for x in fm.fontManager.ttflist) else 'Arial'

rows = [r for r in csv.DictReader(open(os.path.join(HERE, '..', 'data', 'top500_perfdevel_GFlops.csv'))) if r['month'] == '6']
yr = [int(r['year']) for r in rows]
S = {k: [float(r[c]) for r in rows] for k, c in [('Sum of all 500 systems', 'sum_GFlops'), ('#1 system', 'rank1_GFlops'), ('#500 system', 'rank500_GFlops')]}
assert yr[0] == 1993 and yr[-1] == 2026 and len(yr) == 34

plt.rcParams.update({'font.family': FONT, 'font.size': 8, 'axes.linewidth': 0.6,
                     'pdf.fonttype': 42, 'mathtext.fontset': 'custom', 'mathtext.rm': FONT,
                     'mathtext.it': FONT + ':italic'})
fig, ax = plt.subplots(figsize=(3.5, 2.4))
style = {'Sum of all 500 systems': ('#2a78d6', '-', 'o'), '#1 system': ('#eb6834', '--', 's'), '#500 system': ('#1baf7a', ':', '^')}
for k, v in S.items():
    c, ls, mk = style[k]
    ax.plot(yr, v, color=c, ls=ls, lw=1.5, marker=mk, ms=3.0, markevery=3, label=k)
ax.set_yscale('log')
ticks = [1, 1e2, 1e4, 1e6, 1e8, 1e10]
lab = {1: '1 GFlop/s', 1e2: '100 GFlop/s', 1e4: '10 TFlop/s', 1e6: '1 PFlop/s', 1e8: '100 PFlop/s', 1e10: '10 EFlop/s'}
ax.yaxis.set_major_locator(FixedLocator(ticks)); ax.set_yticklabels([lab[t] for t in ticks])
ax.yaxis.set_minor_locator(LogLocator(base=10, subs=(1.0,), numticks=20)); ax.yaxis.set_minor_formatter(NullFormatter())
ax.tick_params(axis='y', which='minor', length=2, width=0.5)
ax.set_ylim(0.2, 6e10); ax.set_xlim(1992, 2027)
ax.set_xticks(range(1995, 2026, 5))
ax.set_xlabel('Year (June TOP500 list)'); ax.set_ylabel('HPL performance $R_{\\mathrm{max}}$')
ax.grid(True, which='major', color='#d9d9d9', lw=0.5); ax.set_axisbelow(True)
for s in ['top', 'right']: ax.spines[s].set_visible(False)
ax.legend(loc='upper left', fontsize=7.5, frameon=False, handlelength=2.6, borderaxespad=0.3)
fig.subplots_adjust(left=0.21, right=0.98, top=0.98, bottom=0.17)
fig.savefig(os.path.join(HERE, '..', 'fig5_top500_june.pdf'))
print('first', yr[0], {k: v[0] for k, v in S.items()}); print('last', yr[-1], {k: v[-1] for k, v in S.items()})
