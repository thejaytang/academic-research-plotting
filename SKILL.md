---
name: academic-research-plotting
description: Create, improve, and audit publication-quality Python research figures across disciplines including bioinformatics, economics, management, computer science, data science, machine learning, psychology, HCI, public health, geospatial research, and physical sciences. Use when selecting academic chart types, writing matplotlib/seaborn/plotly/geopandas/networkx code, fixing poor aesthetics, font size, spacing, legend overlap, annotation overlap, layout issues, accessibility, or journal-ready export problems.
license: MIT
---

# Academic Research Plotting

Use this skill to produce clear, reproducible, publication-quality research figures in Python. Treat plotting as a small research design task, not a cosmetic final step.

## Core Workflow

Always follow this sequence:

1. Define the figure job: exploratory analysis, manuscript figure, report, presentation, poster, dashboard, or supplementary material.
2. Identify the data relationship: distribution, comparison, trend, correlation, composition, uncertainty, model evaluation, spatial pattern, network structure, time-to-event, mechanism, or workflow.
3. Select the simplest defensible chart type. Avoid decorative chart types unless they encode the research question better.
4. Choose the plotting stack:
   - Use `matplotlib` object-oriented API for final static academic figures.
   - Use `seaborn` for statistical distributions, categorical comparisons, and quick exploratory plots.
   - Use `plotly` for interactive exploration, dashboards, hover details, and HTML outputs.
   - Use `geopandas` or `cartopy` for maps.
   - Use `networkx`, Graphviz, Gephi, Cytoscape, or Plotly for graph/network data.
5. Apply a consistent style system before plotting.
6. Run Plot Doctor QA before final export.
7. Export both vector and high-DPI raster formats unless the user asks otherwise.

## Required Checks

Before finalizing any figure, verify:

- The chart type matches the data relationship and discipline convention.
- Axes have informative labels and units when applicable.
- Sample size, uncertainty type, and statistical meaning are not hidden.
- Text remains readable at final size.
- Legends, annotations, labels, and tick text do not overlap or hide data.
- Colors are accessible and not dependent on red-green contrast alone.
- Multi-panel figures use consistent panel labels, scales, spacing, and typography.
- The final file is not cropped and has enough whitespace.

## Reference Loading

Load only the relevant reference file:

- Use `references/chart-selection.md` when choosing a chart type.
- Use `references/discipline-patterns.md` when the domain matters.
- Use `references/style-system.md` before implementing final figure styling.
- Use `references/layout-qa.md` before diagnosing or fixing bad figures.
- Use `references/python-patterns.md` when writing reusable plotting code.

## Bundled Scripts

Prefer bundled scripts for repeated plotting infrastructure:

- `scripts/research_plot_style.py`: shared Matplotlib style, palettes, dimensions, and helpers.
- `scripts/export_figure.py`: journal-safe export helpers for PDF, SVG, PNG, and TIFF.
- `scripts/audit_figure.py`: lightweight Plot Doctor audit for fonts, labels, legends, clipping risk, and layout issues.

Use these scripts directly when possible instead of rewriting style and export boilerplate.

## Plot Doctor Procedure

When asked to improve, polish, or fix a figure:

1. Diagnose the failure mode: wrong chart type, clutter, weak encoding, typography, layout, color, labeling, or export.
2. Preserve the research meaning. Do not silently change variables, scales, summary statistics, or statistical interpretation.
3. Fix root causes first: chart choice and data transformation before styling.
4. Apply style and layout improvements.
5. Re-export and audit the final output.

## Default Academic Defaults

- Static manuscript figures: `matplotlib` + vector export.
- Statistical social science plots: raw data where feasible, interval estimates, and clear uncertainty.
- Machine learning plots: include baseline, uncertainty over folds/seeds when available, and avoid cherry-picked scales.
- Bioinformatics plots: use conventional encodings, but check label density and color accessibility.
- Maps: use appropriate projection and classification, and never imply precision beyond the data.
- Network plots: avoid unreadable hairballs; aggregate, filter, or use adjacency matrices when needed.

## Final Deliverables

For final figure work, provide:

- Reproducible Python code.
- Exported figure files.
- A short note describing chart choice, style choices, and QA result.

