# Style System

Apply style before plotting. Keep the figure calm, readable, and consistent.

## Typography

Default final-print sizes:

| Element | Manuscript | Slide/Poster |
|---|---:|---:|
| Axis labels | 8-10 pt | 14-22 pt |
| Tick labels | 6-8 pt | 11-18 pt |
| Legend text | 6-8 pt | 11-18 pt |
| Panel labels | 9-12 pt bold | 16-24 pt bold |
| Annotation text | 6-8 pt | 11-18 pt |

Use sans-serif fonts unless the target venue requires otherwise. Prefer Arial, Helvetica, DejaVu Sans, or a known installed font.

## Figure Sizes

Common manuscript widths:

- Single column: 3.3 to 3.5 inches.
- One-and-half column: 4.5 to 5.5 inches.
- Double column: 6.8 to 7.2 inches.

Poster and slide figures should be designed at final aspect ratio, not scaled up from tiny manuscript defaults.

## Colors

Use colorblind-safe defaults:

- Okabe-Ito for categories.
- `viridis`, `cividis`, `magma`, or `plasma` for ordered continuous values.
- `RdBu_r`, `PuOr`, or `BrBG` for centered diverging data.

Avoid:

- `jet`, `rainbow`, and non-uniform colormaps.
- Red-green contrasts as the only signal.
- More than 8 distinct categorical colors without grouping or faceting.

Use redundant encoding when possible: color plus marker, line style, hatch, label, or panel split.

## Lines, Markers, and Grids

- Data lines: 1.0-1.8 pt for manuscripts.
- Error bars: thinner than data lines, with caps only when they improve readability.
- Markers: large enough to inspect, but not so large that they merge.
- Grid lines: light and sparse. Remove if they do not help reading values.
- Spines: remove top and right spines for most statistical plots.

## Legends and Labels

- Prefer direct labels for small numbers of lines.
- Move legends outside the plotting area when they cover data.
- Use compact legends for multi-panel figures.
- Keep legend order consistent with plot order.
- Do not use legend labels like `var1` or `group_a`; use reader-facing labels.

## Layout

- Use `constrained_layout=True` for most Matplotlib figures.
- Use `GridSpec` or `subplot_mosaic` for complex multi-panel layouts.
- Keep consistent y-axis scales when direct panel comparisons matter.
- Use shared axes when panels represent the same measurement.
- Do not crowd panels. Reduce detail or split into separate figures.

## Export

Recommended defaults:

- Manuscript: PDF or SVG plus PNG at 300 DPI.
- Raster-heavy figures: PNG or TIFF at 300-600 DPI.
- Line art: vector preferred.
- Interactive: HTML plus static image.

Always use a white background unless transparency is explicitly requested.

