"""Reproduce the README example using synthetic values; no research data."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scripts.research_plot_style import apply_academic_style
from scripts.audit_figure import audit_figure, summarize_issues
from scripts.export_figure import export_figure

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.github' / 'assets'
LABELS = ['Context quality', 'Verification steps', 'Iteration depth', 'Task complexity']
VALUES = [0.38, 0.29, 0.14, -0.18]
INTERVALS = [0.09, 0.11, 0.08, 0.12]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(5.6, 3.4), constrained_layout=True)
    ax.bar(LABELS, VALUES, yerr=INTERVALS, color=['#224C75'] * 4, capsize=4)
    ax.tick_params(labelsize=5)
    ax.set_title('Synthetic values: before revision', fontsize=10)
    before = audit_figure(fig)
    export_figure(fig, OUT / 'figure-before', formats=('png',), dpi=180)
    plt.close(fig)

    apply_academic_style(font_family='DejaVu Sans', grid=False)
    fig, ax = plt.subplots(figsize=(5.6, 3.4), constrained_layout=True)
    ax.errorbar(VALUES, range(4), xerr=INTERVALS, fmt='o', color='#0072B2',
                ecolor='#435467', markersize=6, capsize=3, linewidth=1.3)
    ax.set_yticks(range(4), LABELS)
    ax.invert_yaxis()
    ax.axvline(0, color='#A5ADB5', linewidth=0.8, linestyle='--')
    ax.set_xlabel('Synthetic coefficient (arbitrary units)')
    ax.set_ylabel('Illustrative predictor')
    ax.set_title('Synthetic estimates with illustrative intervals', loc='left', pad=12)
    ax.spines[['top','right']].set_visible(False)
    after = audit_figure(fig)
    export_figure(fig, OUT / 'figure-after', formats=('png','svg'), dpi=180)
    plotted = list(ax.lines[0].get_xdata())
    assert plotted == VALUES, 'The layout revision must preserve the values.'
    assert any(x.code == 'missing_xlabel' for x in before)
    assert not any(x.code in {'missing_xlabel','missing_ylabel','small_text','no_axes'} for x in after)
    report = ('Synthetic demonstration only. Intervals are specified by the example, not estimated from observations.\n\n'
              + 'BEFORE\n' + summarize_issues(before) + '\n\nAFTER\n' + summarize_issues(after) + '\n')
    (ROOT / 'examples' / 'readme-audit.txt').write_text(report)
    print(report)
    plt.close(fig)
if __name__ == '__main__':
    main()
