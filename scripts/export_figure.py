"""Export helpers for academic research figures."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import matplotlib.figure


VECTOR_FORMATS = {"pdf", "svg", "eps"}
RASTER_FORMATS = {"png", "tif", "tiff", "jpg", "jpeg"}


def normalize_formats(formats: Iterable[str]) -> tuple[str, ...]:
    """Normalize and validate output formats."""
    cleaned = tuple(fmt.lower().lstrip(".") for fmt in formats)
    unknown = [fmt for fmt in cleaned if fmt not in VECTOR_FORMATS | RASTER_FORMATS]
    if unknown:
        raise ValueError(f"Unsupported figure format(s): {', '.join(unknown)}")
    return cleaned


def export_figure(
    fig: matplotlib.figure.Figure,
    output_base: str | Path,
    *,
    formats: Iterable[str] = ("pdf", "png"),
    dpi: int = 300,
    transparent: bool = False,
    facecolor: str = "white",
    tight: bool = True,
    pad_inches: float = 0.03,
) -> list[Path]:
    """Save a Matplotlib figure in multiple academic-friendly formats.

    `output_base` may include or omit an extension. If it includes an extension
    and `formats` is not supplied, prefer passing the desired format explicitly.
    """
    base = Path(output_base)
    if base.suffix:
        base = base.with_suffix("")

    base.parent.mkdir(parents=True, exist_ok=True)
    bbox_inches = "tight" if tight else None
    saved_paths: list[Path] = []

    for fmt in normalize_formats(formats):
        path = base.with_suffix(f".{fmt}")
        save_kwargs = {
            "format": fmt,
            "bbox_inches": bbox_inches,
            "pad_inches": pad_inches,
            "transparent": transparent,
            "facecolor": "none" if transparent else facecolor,
        }
        if fmt in RASTER_FORMATS:
            save_kwargs["dpi"] = dpi
        fig.savefig(path, **save_kwargs)
        saved_paths.append(path)

    return saved_paths


def export_manuscript_figure(
    fig: matplotlib.figure.Figure,
    output_base: str | Path,
    *,
    dpi: int = 300,
) -> list[Path]:
    """Export default manuscript formats."""
    return export_figure(fig, output_base, formats=("pdf", "svg", "png"), dpi=dpi)


def export_raster_heavy_figure(
    fig: matplotlib.figure.Figure,
    output_base: str | Path,
    *,
    dpi: int = 600,
) -> list[Path]:
    """Export heatmaps, microscopy-like composites, or raster-heavy figures."""
    return export_figure(fig, output_base, formats=("png", "tiff"), dpi=dpi)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "This helper is primarily intended to be imported from plotting scripts. "
            "It does not load existing figure files from disk."
        )
    )
    parser.add_argument("--explain", action="store_true", help="Print usage guidance.")
    return parser.parse_args()


def main() -> None:
    _parse_args()
    print(
        "Import export_figure from scripts.export_figure inside your plotting script, "
        "then call export_figure(fig, 'outputs/figure_name')."
    )


if __name__ == "__main__":
    main()

