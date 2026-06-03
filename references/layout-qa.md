# Plot Doctor Layout QA

Use this checklist when fixing or finalizing figures.

## Chart Integrity

- Does the chart type answer the research question?
- Are summary statistics appropriate for the distribution?
- Are transformations disclosed: log, z-score, normalization, scaling, smoothing?
- Are uncertainty intervals defined?
- Are sample sizes visible or stated nearby?
- Are axes truthful and not visually misleading?

## Text and Labels

- Axis labels include units when applicable.
- Tick labels are not overcrowded or clipped.
- Long category names are wrapped, abbreviated with explanation, or moved to horizontal bars.
- Annotations do not overlap each other or cover important data.
- Panel labels are placed consistently.
- Mathematical notation renders correctly.

## Legend

- Legend does not cover data.
- Legend order matches visual order or logical order.
- Legend title is meaningful or removed if unnecessary.
- Legend uses readable markers/lines at final size.
- Multi-panel legends are shared when appropriate.

## Layout

- No subplot titles, axis labels, or tick labels overlap.
- Margins are sufficient after export.
- Colorbars have labels and do not squeeze the main plot.
- Multi-panel spacing is consistent.
- Aspect ratio is appropriate for the chart type.
- The figure remains legible when printed at final dimensions.

## Color and Accessibility

- Color palette is colorblind-safe.
- Continuous data use perceptually ordered colormaps.
- Diverging data have a meaningful center.
- Grayscale view remains interpretable when required.
- Contrast is high enough for thin lines and small labels.

## Discipline-Specific QA

- Bioinformatics heatmaps state scaling and clustering method.
- UMAP/t-SNE plots are not over-interpreted as distances or proof.
- Event study plots show reference period and confidence intervals.
- DiD plots show pre-period trend evidence when relevant.
- Regression discontinuity plots show cutoff and binning logic.
- ML classification plots include class imbalance context when relevant.
- Survival plots include censoring and number at risk when feasible.
- Maps use appropriate projection and normalized quantities.
- Network plots avoid hairballs or explain filtering.

## Fix Strategy

Fix in this order:

1. Wrong chart type.
2. Missing or misleading statistical encoding.
3. Overplotting and excessive labels.
4. Typography and spacing.
5. Color and accessibility.
6. Export settings.

Do not solve a chart-choice problem with styling alone.

