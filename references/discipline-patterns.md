# Discipline Patterns

Use this file as a starting catalog. Prefer the chart that matches the data relationship and the field's reporting convention.

## Bioinformatics and Omics

Common figures:

- PCA plot, scree plot, biplot
- UMAP, t-SNE, diffusion map, PHATE
- Volcano plot, MA plot
- Expression heatmap, clustered heatmap, correlation heatmap
- Gene expression violin, box, ridge, dot, feature plot
- Differential expression dot plot and pathway enrichment bar/dot plot
- Venn diagram, UpSet plot
- Manhattan plot, QQ plot for GWAS
- Genome browser track, coverage profile, sashimi plot
- Circos/chord diagram for genomic relationships
- Phylogenetic tree and dendrogram
- Pseudotime trajectory and stream plot
- Survival curve for biomarker studies

Typical Python stack: `scanpy`, `seaborn`, `matplotlib`, `plotly`, `networkx`, `lifelines`.

Key cautions:

- UMAP and t-SNE are visual summaries, not proof of cluster separation.
- Label only important genes or use collision-aware labels.
- For heatmaps, explain scaling: raw, log, z-score, row-scaled, or column-scaled.
- Use perceptually uniform colormaps for continuous expression.

## Single-Cell and Spatial Omics

Common figures:

- UMAP/t-SNE colored by cluster, condition, marker gene, batch, or score
- Feature plot, dot plot, matrix plot, violin plot
- Cluster composition stacked bar
- Marker gene heatmap
- Pseudotime trajectory and lineage plot
- Cell-cell communication chord, Sankey, or network
- Spatial spot map, tissue overlay, spatial heatmap

Key cautions:

- Avoid overloaded UMAP panels with tiny unreadable legends.
- Keep cluster colors consistent across figures.
- For spatial figures, preserve aspect ratio and tissue orientation.

## Economics, Management, Finance, Marketing

Common figures:

- Coefficient plot with confidence intervals
- Event study plot with leads/lags and reference period
- Difference-in-differences trend plot and parallel trends check
- Regression discontinuity plot with binned means and fitted lines
- Marginal effects plot and interaction plot
- Partial residual and residual diagnostics
- Forest plot for meta-analysis or subgroup effects
- Funnel plot for publication bias or conversion funnels
- Cumulative abnormal return and CAAR plots
- Lorenz curve, concentration curve, inequality plots
- Distribution, density, ECDF, quantile, and binned scatter plots
- Time series, seasonal decomposition, forecast fan chart
- Sankey for flows and customer journeys
- Conjoint utility and attribute importance plots

Typical Python stack: `matplotlib`, `seaborn`, `statsmodels`, `linearmodels`, `plotly`.

Key cautions:

- Always show confidence intervals for estimated effects.
- Mark treatment/event time explicitly.
- Avoid implied causality in descriptive time trends.
- Keep coefficient order meaningful, not formula order.

## Psychology, Behavioral Science, Education

Common figures:

- Raincloud plot, violin + raw points, box + jitter
- Within-subject paired dot/line plot
- Interaction plot for factorial designs
- Reaction time distribution, ex-Gaussian-style density, ECDF
- Likert diverging stacked bar
- Forest plot of effect sizes
- Correlation scatter with confidence band
- Bland-Altman plot for agreement
- Learning curve and trial-level trend
- Mediation/moderation schematic

Typical Python stack: `seaborn`, `matplotlib`, `pingouin`, `statsmodels`, `plotly`.

Key cautions:

- Do not hide small-n data behind mean bars.
- Plot paired designs as paired when possible.
- State what error bars mean: SD, SEM, CI, or credible interval.

## HCI, UX, Human Factors

Common figures:

- Task completion rate, error rate, and time-on-task plots
- SUS score distribution and item-level Likert plots
- NASA-TLX dimension plot
- Condition comparison raincloud or box + raw points
- Within-subject connected dot plot
- Click heatmap, gaze heatmap, scanpath
- Funnel/drop-off plot
- Timeline of interaction events
- Confusion/error taxonomy stacked bar
- Qualitative coding frequency bar or mosaic plot

Typical Python stack: `matplotlib`, `seaborn`, `plotly`, `pandas`.

Key cautions:

- Avoid averaging ordinal Likert items without explaining aggregation.
- For within-subject studies, show paired structure.
- Keep survey response order stable and semantically ordered.

## Machine Learning and Data Science

Common figures:

- Confusion matrix
- ROC curve, precision-recall curve, threshold curves
- Calibration curve / reliability diagram
- Learning curve and validation curve
- Training loss and metric curves
- Predicted-vs-observed scatter
- Residual plot and error distribution
- Feature importance, permutation importance
- SHAP beeswarm, waterfall, dependence, interaction heatmap
- Partial dependence and ICE plots
- Ablation bar chart or line chart
- Embedding projection with PCA/UMAP/t-SNE
- Class distribution and missingness plots
- Model comparison dot plot with intervals across folds/seeds

Typical Python stack: `matplotlib`, `seaborn`, `scikit-learn`, `shap`, `plotly`.

Key cautions:

- For imbalanced classes, include PR curves and class-specific metrics.
- Do not use one split result as a final comparison when folds/seeds are available.
- Include baselines and uncertainty when comparing models.

## Computer Science Systems and Software Engineering

Common figures:

- Latency-throughput curve
- P50/P90/P95/P99 latency over load
- CDF/CCDF of latency
- Scalability curve and speedup plot
- Resource utilization timeline
- Error rate, availability, retry, and saturation trends
- Flame graph and differential flame graph
- Trace waterfall and Gantt-style execution timeline
- Benchmark bar chart with uncertainty
- Ablation and sensitivity plots
- Queue depth and throughput over time
- Memory, CPU, I/O, and network time series

Typical Python stack: `matplotlib`, `seaborn`, `plotly`, `pandas`.

Key cautions:

- Means are often misleading for latency. Show tail percentiles.
- Use log scales only when justified and label them clearly.
- Benchmark plots need repeated runs and interval estimates.

## Networks and Graph Data

Common figures:

- Node-link graph with spring, circular, shell, bipartite, or hierarchical layout
- Community graph and ego network
- Degree distribution and rank-degree plot
- Centrality bar/dot plot
- Adjacency matrix heatmap
- Chord diagram and Sankey diagram
- Bipartite graph and alluvial flow
- Tree, dendrogram, and radial tree

Typical Python stack: `networkx`, `matplotlib`, `plotly`, Graphviz, Gephi, Cytoscape.

Key cautions:

- Dense node-link graphs become unreadable quickly.
- Filter, aggregate, facet, or switch to an adjacency matrix when needed.
- Layout choice changes interpretation, so do not overclaim spatial meaning.

## Geospatial, Urban, Environmental

Common figures:

- Choropleth map
- Point map and proportional symbol map
- Hexbin or grid map
- Kernel density / spatial heatmap
- Flow map and origin-destination map
- Raster map, contour map, terrain map
- Time-series small multiples by region
- Cartogram
- Spatial residual map
- Bivariate choropleth

Typical Python stack: `geopandas`, `cartopy`, `matplotlib`, `plotly`, `folium`, `contextily`.

Key cautions:

- Use appropriate projections, especially for area comparisons.
- Classification bins change interpretation. State quantile, equal interval, natural breaks, or custom bins.
- Choropleths should use rates or normalized values, not raw counts, unless justified.

## Public Health, Medicine, Clinical Research

Common figures:

- Kaplan-Meier survival curve
- Cumulative incidence curve
- Forest plot for hazard ratios, odds ratios, and subgroup effects
- ROC, PR, calibration, and decision curve
- Epidemic curve
- Incidence and prevalence time series
- CONSORT flow diagram
- Risk table and baseline balance plot
- Bland-Altman plot
- Dose-response curve
- Adverse event bar or dot plot
- Geographic incidence map

Typical Python stack: `lifelines`, `matplotlib`, `seaborn`, `statsmodels`, `scikit-learn`, `geopandas`.

Key cautions:

- Survival plots need censoring and number-at-risk context when possible.
- Clinical prediction plots should include calibration, not only discrimination.
- Distinguish absolute risk, relative risk, odds ratio, and hazard ratio.

## Materials Science, Chemistry, Molecular Simulation

Common figures:

- Phase diagram
- Band structure and density of states
- XRD, Raman, IR, UV-Vis spectra
- Nyquist and Bode plots
- Tafel plot and cyclic voltammetry curve
- RMSD, RMSF, radius of gyration, SASA, hydrogen bond plots
- Radial distribution function
- Free energy landscape, potential energy surface
- Reaction coordinate and energy profile
- Parity plot for predicted vs computed properties
- Structure-property scatter and composition map

Typical Python stack: `matplotlib`, `seaborn`, `pymatgen`, `ase`, `MDAnalysis`, `mdtraj`, `plotly`.

Key cautions:

- Preserve scientific units and axis conventions.
- Use consistent color for systems across all trajectory panels.
- Avoid 3D surfaces when a contour or heatmap communicates better.

## Physics, Astronomy, Earth and Space Science

Common figures:

- Spectrum plot and residual spectrum
- Light curve and phase-folded curve
- HR diagram / color-magnitude diagram
- Sky map and finder chart
- Power spectrum and periodogram
- Phase space plot
- Contour and density map
- Error ellipse and posterior corner plot
- Model fit with residual panel
- Airmass/altitude/parallactic angle plots
- Hovmoller diagram and climate anomaly map

Typical Python stack: `matplotlib`, `astropy`, `astroplan`, `cartopy`, `xarray`, `seaborn`.

Key cautions:

- Respect field conventions such as inverted magnitude axes.
- Include residuals when showing model fits.
- Use log scaling only with clear tick labeling.

## Optimization, Operations, Decision Science

Common figures:

- Pareto front
- Convergence curve
- Sensitivity tornado plot
- Scenario fan chart
- Trade-off scatter
- Constraint violation plot
- Gantt chart
- Resource utilization timeline
- Queueing performance curves
- Sankey for process flows

Typical Python stack: `matplotlib`, `seaborn`, `plotly`, `pymoo`, `pandas`.

Key cautions:

- Label objective direction: minimize or maximize.
- Show feasible and infeasible regions when helpful.
- Avoid hiding uncertainty in scenario charts.

