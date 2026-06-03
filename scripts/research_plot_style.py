"""Shared style helpers for academic research figures.

Import this module before creating final Matplotlib figures.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping

import matplotlib as mpl
import matplotlib.pyplot as plt


SKILL_DIR = Path(__file__).resolve().parents[1]
PRESETS_PATH = SKILL_DIR / "assets" / "journal_presets.json"

OKABE_ITO = [
    "#E69F00",
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#0072B2",
    "#D55E00",
    "#CC79A7",
    "#000000",
]

ACADEMIC_BLUE = "#2563EB"
ACADEMIC_GRAY = "#374151"
LIGHT_GRID = "#E5E7EB"


def load_presets() -> dict:
    """Load bundled journal/style presets."""
    with PRESETS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_preset(name: str = "default") -> Mapping[str, object]:
    """Return a preset, falling back to the default preset."""
    presets = load_presets()
    return presets.get(name, presets["default"])


def apply_academic_style(
    preset: str = "default",
    *,
    font_family: str | None = None,
    color_cycle: Iterable[str] = OKABE_ITO,
    grid: bool = True,
) -> None:
    """Apply conservative publication-oriented Matplotlib defaults."""
    settings = get_preset(preset)
    family = font_family or str(settings.get("font_family", "DejaVu Sans"))

    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": [family, "Arial", "Helvetica", "DejaVu Sans"],
            "font.size": settings.get("axis_label_size", 8),
            "axes.labelsize": settings.get("axis_label_size", 8),
            "axes.titlesize": settings.get("axis_label_size", 8),
            "xtick.labelsize": settings.get("tick_label_size", 7),
            "ytick.labelsize": settings.get("tick_label_size", 7),
            "legend.fontsize": settings.get("legend_size", 7),
            "figure.dpi": settings.get("dpi", 300),
            "savefig.dpi": settings.get("dpi", 300),
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.03,
            "savefig.facecolor": "white",
            "axes.prop_cycle": mpl.cycler(color=list(color_cycle)),
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": ACADEMIC_GRAY,
            "axes.labelcolor": "black",
            "xtick.color": "black",
            "ytick.color": "black",
            "text.color": "black",
            "legend.frameon": False,
            "lines.linewidth": 1.2,
            "lines.markersize": 4,
            "patch.linewidth": 0.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )

    if grid:
        mpl.rcParams.update(
            {
                "axes.grid": True,
                "grid.color": LIGHT_GRID,
                "grid.linewidth": 0.5,
                "grid.alpha": 0.7,
            }
        )
    else:
        mpl.rcParams["axes.grid"] = False


def figure_size(
    width: str = "single",
    *,
    aspect: float = 0.68,
    preset: str = "default",
    height: float | None = None,
) -> tuple[float, float]:
    """Return a figure size in inches for common academic widths."""
    settings = get_preset(preset)
    if width == "single":
        w = float(settings["single_column_width_in"])
    elif width == "double":
        w = float(settings["double_column_width_in"])
    else:
        w = float(width)

    h = float(height) if height is not None else w * aspect
    return w, h


def despine(ax: mpl.axes.Axes) -> None:
    """Remove top and right spines from an axis."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def annotate_panels(
    axes: Mapping[str, mpl.axes.Axes] | Iterable[mpl.axes.Axes],
    *,
    x: float = -0.12,
    y: float = 1.05,
    labels: Iterable[str] | None = None,
    fontsize: float | None = None,
) -> None:
    """Add panel labels to axes in a consistent position."""
    if isinstance(axes, Mapping):
        items = list(axes.items())
        panel_labels = [key for key, _ in items]
        axis_list = [ax for _, ax in items]
    else:
        axis_list = list(axes)
        panel_labels = list(labels or [chr(ord("A") + i) for i in range(len(axis_list))])

    for label, ax in zip(panel_labels, axis_list):
        ax.text(
            x,
            y,
            str(label),
            transform=ax.transAxes,
            fontweight="bold",
            fontsize=fontsize,
            va="top",
            ha="left",
        )


def place_legend_outside(
    ax: mpl.axes.Axes,
    *,
    loc: str = "center left",
    anchor: tuple[float, float] = (1.02, 0.5),
    **kwargs,
):
    """Move an axis legend outside the plotting area."""
    return ax.legend(loc=loc, bbox_to_anchor=anchor, borderaxespad=0.0, **kwargs)


def direct_label_lines(ax: mpl.axes.Axes, *, x_offset: float = 0.01) -> None:
    """Label line plots at their rightmost finite point when possible."""
    xlim = ax.get_xlim()
    dx = (xlim[1] - xlim[0]) * x_offset

    for line in ax.get_lines():
        label = line.get_label()
        if not label or label.startswith("_"):
            continue
        xdata = line.get_xdata(orig=False)
        ydata = line.get_ydata(orig=False)
        if len(xdata) == 0:
            continue
        x_last = xdata[-1]
        y_last = ydata[-1]
        ax.text(x_last + dx, y_last, label, va="center", fontsize=mpl.rcParams["legend.fontsize"])


if __name__ == "__main__":
    apply_academic_style()
    fig, ax = plt.subplots(figsize=figure_size("single"), constrained_layout=True)
    ax.plot([0, 1, 2], [0, 1, 0], label="Example")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Response")
    ax.legend()
    plt.show()

