# Python Patterns

Use reproducible, explicit plotting code. Avoid hidden notebook state for final figures.

## Matplotlib Object-Oriented Pattern

```python
import matplotlib.pyplot as plt

from scripts.research_plot_style import apply_academic_style
from scripts.export_figure import export_figure

apply_academic_style()

fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.plot(x, y, label="Model A")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Accuracy")
ax.legend(frameon=False)

export_figure(fig, "outputs/figure1", formats=("pdf", "png"), dpi=300)
```

## Seaborn Statistical Pattern

```python
import matplotlib.pyplot as plt
import seaborn as sns

from scripts.research_plot_style import apply_academic_style
from scripts.export_figure import export_figure

apply_academic_style()

fig, ax = plt.subplots(figsize=(3.5, 2.8), constrained_layout=True)
sns.boxplot(data=df, x="condition", y="score", ax=ax, color="white", fliersize=0)
sns.stripplot(data=df, x="condition", y="score", ax=ax, alpha=0.55, size=3, jitter=0.18)
ax.set_xlabel("Condition")
ax.set_ylabel("Score")

export_figure(fig, "outputs/score_by_condition")
```

## Estimate With Confidence Interval

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.errorbar(
    estimates,
    labels,
    xerr=[estimates - ci_low, ci_high - estimates],
    fmt="o",
    capsize=2,
    linewidth=1,
)
ax.axvline(0, color="0.3", linewidth=0.8)
ax.set_xlabel("Estimated effect")
ax.set_ylabel("")
```

## Multi-Panel Pattern

```python
fig, axes = plt.subplot_mosaic(
    [["A", "B"], ["C", "C"]],
    figsize=(7.0, 4.6),
    constrained_layout=True,
)

for label, ax in axes.items():
    ax.text(
        -0.12,
        1.05,
        label,
        transform=ax.transAxes,
        fontweight="bold",
        va="top",
        ha="left",
    )
```

## Dense Scatter Pattern

```python
fig, ax = plt.subplots(figsize=(3.5, 2.8), constrained_layout=True)
ax.hexbin(df["x"], df["y"], gridsize=40, cmap="viridis", mincnt=1)
ax.set_xlabel("Variable X")
ax.set_ylabel("Variable Y")
```

## Plotly Exploration Pattern

```python
import plotly.express as px

fig = px.scatter(
    df,
    x="x",
    y="y",
    color="group",
    hover_data=["id"],
    template="simple_white",
)
fig.write_html("outputs/exploration.html")
fig.write_image("outputs/exploration.png", scale=3)
```

## Reproducibility Rules

- Put final figures in scripts, not only notebook cells.
- Define data transformations before plotting.
- Set random seeds for jitter, sampling, or stochastic embeddings.
- Save intermediate cleaned data when figure generation is expensive.
- Keep chart functions small and parameterized.
- Do not hard-code unexplained magic offsets for labels unless necessary.

