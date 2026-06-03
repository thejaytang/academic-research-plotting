# Academic Research Plotting

Publication-quality Python plotting skill for academic researchers who work across fields.

This skill helps an AI coding agent choose better research chart types, write reproducible Python plotting code, apply consistent academic styling, audit layout problems, and export journal-ready figures. It is designed for researchers who use Python across bioinformatics, economics, management, computer science, data science, machine learning, psychology, HCI, public health, geospatial research, and physical sciences.

## Why This Exists

Many research figures fail for practical reasons:

- The chart type is too simple for the research question.
- Font sizes are wrong for final print size.
- Legends, labels, and annotations overlap with data.
- Multi-panel spacing is inconsistent.
- Colors look attractive but fail accessibility checks.
- Exported figures are cropped, blurry, or not suitable for submission.

Academic Research Plotting turns those recurring problems into a repeatable workflow: choose the right chart, style it consistently, run a Plot Doctor audit, and export clean outputs.

## What It Does

- Selects chart types based on research task and data relationship.
- Covers common figure patterns across many academic disciplines.
- Provides a conservative Python style system for `matplotlib` and `seaborn`.
- Includes export helpers for `PDF`, `SVG`, `PNG`, and `TIFF`.
- Audits common layout issues such as missing labels, tiny text, legend placement, clipping risk, and possible overlap.
- Encourages reproducible figure scripts instead of fragile notebook-only plots.

## Included Skill Files

```text
academic-research-plotting/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── journal_presets.json
├── references/
│   ├── chart-selection.md
│   ├── discipline-patterns.md
│   ├── layout-qa.md
│   ├── python-patterns.md
│   └── style-system.md
└── scripts/
    ├── audit_figure.py
    ├── export_figure.py
    └── research_plot_style.py
```

## Discipline Coverage

The bundled reference library covers figure patterns for:

- Bioinformatics, omics, single-cell, and spatial omics
- Economics, management, finance, and marketing
- Psychology, behavioral science, education, HCI, and UX
- Machine learning, data science, and model evaluation
- Computer systems and software engineering
- Network science and graph data
- Geospatial, urban, and environmental research
- Public health, medicine, and clinical research
- Materials science, chemistry, and molecular simulation
- Physics, astronomy, Earth science, optimization, and decision science

## Example Prompts

Use the skill explicitly:

```text
Use $academic-research-plotting to turn this regression table into a publication-quality coefficient plot.
```

```text
Use $academic-research-plotting to improve this seaborn plot. Fix font sizes, spacing, legend placement, and export it as PDF and PNG.
```

```text
Use $academic-research-plotting to choose the best chart for these HCI Likert survey results and generate Python code.
```

```text
Use $academic-research-plotting to audit my UMAP, heatmap, and volcano plot for manuscript readiness.
```

## Python Helper Usage

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scripts.research_plot_style import apply_academic_style, figure_size
from scripts.export_figure import export_figure
from scripts.audit_figure import audit_figure, summarize_issues

apply_academic_style()

fig, ax = plt.subplots(figsize=figure_size("single"), constrained_layout=True)
ax.plot([0, 1, 2], [0, 1, 0], label="Example")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Response")
ax.legend(frameon=False)

print(summarize_issues(audit_figure(fig)))
export_figure(fig, "outputs/figure1", formats=("pdf", "png"), dpi=300)
```

## Installation

Install it as a skill by placing this repository folder in your agent's skills directory, or install it using your agent's supported skill installer.

Manual install:

```bash
git clone https://github.com/thejaytang/academic-research-plotting.git
mkdir -p ~/.codex/skills
cp -R academic-research-plotting ~/.codex/skills/
```

For tools that support repository-based skill installation, use this repository as the skill source.

## Design Principles

- Prefer the simplest defensible chart.
- Use code-generated figures for numerical data.
- Show raw data and uncertainty when they matter.
- Do not fix chart-choice problems with styling alone.
- Keep style consistent across a paper.
- Audit before export.

## Star This Repo If

- You regularly make Python figures for papers, theses, reports, or grants.
- You want an AI agent to stop producing generic, cramped charts.
- You work across fields and need discipline-aware figure guidance.
- You care about reproducible, readable, accessible academic figures.

## License

MIT

