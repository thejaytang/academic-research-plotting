# Chart Selection

Start with the research question, not the available plotting function.

## General Data Relationships

| Task | Prefer | Use When | Avoid |
|---|---|---|---|
| Single distribution | Histogram, KDE, ECDF, box plot, violin, raincloud | Show shape, skew, outliers, or uncertainty | Bar of mean only |
| Group comparison | Dot + interval, box + jitter, violin + raw points, raincloud, forest plot | Compare conditions, treatments, methods, groups | 3D bars, unlabeled error bars |
| Time trend | Line chart, small multiples, ribbon interval, event study plot | Ordered time, repeated measurement, forecast | Pie, unsorted categorical bars |
| Correlation | Scatter, hexbin, contour density, pair plot, correlation heatmap | Numeric relationship, many points, multivariate relation | Dual-axis unless strongly justified |
| Composition | Stacked bar, 100 percent stacked bar, mosaic, treemap | Part-to-whole with few categories | Pie with many slices |
| Ranking | Horizontal bar, lollipop, dot plot, slope chart | Ordered categories, before-after ranking | Alphabetical order when rank matters |
| Uncertainty | Error bars, confidence bands, credible interval, violin, bootstrap interval | Estimates need precision or variability | Unspecified whiskers |
| Model evaluation | Confusion matrix, ROC, PR, calibration, residual, predicted-vs-observed | Classification, regression, calibration | Accuracy-only plots |
| Spatial pattern | Choropleth, point map, hexbin map, flow map, raster map | Geographic or spatial data | Unprojected comparisons of area |
| Network structure | Node-link, adjacency matrix, Sankey, chord, bipartite graph | Graph or flow data | Dense hairball without filtering |
| Workflow/mechanism | Flowchart, DAG, schematic, architecture diagram | Process, method, causal logic, model architecture | Decorative pseudo-3D diagrams |

## Decision Rules

- If values are precise and few: use dot plots or bars with direct labels.
- If distributions matter: show distributions and raw points when possible.
- If sample size is small: show raw points, not only summaries.
- If categories exceed 8-10: use horizontal layouts or small multiples.
- If points are overplotted: use alpha, jitter, hexbin, contours, or sampling with disclosure.
- If comparing estimates: use coefficient or forest plots instead of tables.
- If there are repeated measures: connect paired observations or use within-subject summaries.
- If ordinal survey data: use diverging stacked bars, not means-only bars.
- If the figure has a numerical axis: prefer code-generated plots over AI-generated images.

## Common Bad Defaults

- Pie charts with many categories.
- Radar charts for precise comparison.
- Bar charts of means without raw data or intervals.
- Truncated y-axis on bar charts.
- Rainbow or jet colormaps.
- Dense labels on every point.
- Legends that cover data.
- Too many panels with inconsistent scales.
- Dual y-axes without a clear reason.

## Output Choice

- Manuscript line art: PDF or SVG plus PNG 300 DPI.
- Heatmaps and raster-heavy images: PNG or TIFF 300-600 DPI.
- Posters: PNG 300 DPI at final print dimensions or vector PDF.
- Interactive exploration: Plotly HTML plus static PNG/PDF for paper.

