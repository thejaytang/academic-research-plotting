"""Lightweight Plot Doctor audit for Matplotlib figures."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import matplotlib as mpl
import matplotlib.figure
import matplotlib.pyplot as plt


@dataclass
class AuditIssue:
    severity: str
    code: str
    message: str
    target: str = "figure"


def _text_size(text: mpl.text.Text) -> float:
    size = text.get_fontsize()
    return float(size) if size is not None else 0.0


def _visible_texts(fig: matplotlib.figure.Figure) -> list[mpl.text.Text]:
    texts: list[mpl.text.Text] = []
    for text in fig.findobj(match=mpl.text.Text):
        if text.get_visible() and text.get_text():
            texts.append(text)
    return texts


def _tick_text_ids(fig: matplotlib.figure.Figure) -> set[int]:
    """Return ids for tick label text objects."""
    tick_texts: set[int] = set()
    for ax in fig.axes:
        for text in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
            tick_texts.add(id(text))
    return tick_texts


def _draw(fig: matplotlib.figure.Figure):
    canvas = fig.canvas
    canvas.draw()
    return canvas.get_renderer()


def _figure_bbox(fig: matplotlib.figure.Figure, renderer) -> mpl.transforms.Bbox:
    return fig.bbox


def audit_figure(
    fig: matplotlib.figure.Figure | None = None,
    *,
    min_text_size: float = 6.0,
    require_axis_labels: bool = True,
    check_legend_inside: bool = True,
    check_text_overlap: bool = True,
) -> list[AuditIssue]:
    """Audit a Matplotlib figure for common academic plotting problems."""
    fig = fig or plt.gcf()
    issues: list[AuditIssue] = []
    renderer = _draw(fig)
    figure_bbox = _figure_bbox(fig, renderer)
    clipping_bbox = figure_bbox.expanded(1.08, 1.08)
    tick_text_ids = _tick_text_ids(fig)

    axes = [ax for ax in fig.axes if ax.get_visible()]
    if not axes:
        issues.append(AuditIssue("error", "no_axes", "Figure has no visible axes."))
        return issues

    width, height = fig.get_size_inches()
    if width < 2.0 or height < 1.5:
        issues.append(
            AuditIssue(
                "warning",
                "small_figure",
                f"Figure size is very small ({width:.2f} x {height:.2f} in).",
            )
        )

    for i, ax in enumerate(axes, start=1):
        target = f"axes[{i}]"
        if require_axis_labels and ax.has_data():
            if not ax.get_xlabel():
                issues.append(AuditIssue("warning", "missing_xlabel", "Missing x-axis label.", target))
            if not ax.get_ylabel():
                issues.append(AuditIssue("warning", "missing_ylabel", "Missing y-axis label.", target))

        xticks = [tick.get_text() for tick in ax.get_xticklabels() if tick.get_visible() and tick.get_text()]
        yticks = [tick.get_text() for tick in ax.get_yticklabels() if tick.get_visible() and tick.get_text()]
        if len(xticks) > 12:
            issues.append(AuditIssue("info", "many_xticks", f"{len(xticks)} visible x tick labels.", target))
        if len(yticks) > 12:
            issues.append(AuditIssue("info", "many_yticks", f"{len(yticks)} visible y tick labels.", target))

        legend = ax.get_legend()
        if legend is not None and legend.get_visible():
            legend_bbox = legend.get_window_extent(renderer)
            ax_bbox = ax.get_window_extent(renderer)
            if check_legend_inside and legend_bbox.overlaps(ax_bbox):
                issues.append(
                    AuditIssue(
                        "info",
                        "legend_inside_axes",
                        "Legend is inside the plotting area. Confirm it does not hide data.",
                        target,
                    )
                )

    for text in _visible_texts(fig):
        if _text_size(text) < min_text_size:
            label = text.get_text().strip().replace("\n", " ")
            issues.append(
                AuditIssue(
                    "warning",
                    "small_text",
                    f"Text below {min_text_size:g} pt: '{label[:40]}'.",
                    "text",
                )
            )

        try:
            bbox = text.get_window_extent(renderer)
        except Exception:
            continue
        is_tick_label = id(text) in tick_text_ids
        if not is_tick_label and (
            not clipping_bbox.contains(bbox.x0, bbox.y0) or not clipping_bbox.contains(bbox.x1, bbox.y1)
        ):
            label = text.get_text().strip().replace("\n", " ")
            issues.append(
                AuditIssue(
                    "warning",
                    "text_may_be_clipped",
                    f"Text may be clipped after export: '{label[:40]}'.",
                    "text",
                )
            )

    if check_text_overlap:
        texts = _visible_texts(fig)
        bboxes = []
        for text in texts:
            try:
                bbox = text.get_window_extent(renderer).expanded(1.02, 1.10)
            except Exception:
                continue
            if bbox.width > 0 and bbox.height > 0:
                bboxes.append((text, bbox))

        for idx, (text_a, bbox_a) in enumerate(bboxes):
            for text_b, bbox_b in bboxes[idx + 1 :]:
                if bbox_a.overlaps(bbox_b):
                    a = text_a.get_text().strip().replace("\n", " ")
                    b = text_b.get_text().strip().replace("\n", " ")
                    if a and b and a != b:
                        issues.append(
                            AuditIssue(
                                "info",
                                "possible_text_overlap",
                                f"Possible overlap between '{a[:24]}' and '{b[:24]}'.",
                                "text",
                            )
                        )
                        break

    return issues


def summarize_issues(issues: Iterable[AuditIssue]) -> str:
    """Return a compact text report."""
    issues = list(issues)
    if not issues:
        return "Plot Doctor: no common layout issues detected."
    lines = ["Plot Doctor issues:"]
    for issue in issues:
        lines.append(f"- [{issue.severity}] {issue.code} ({issue.target}): {issue.message}")
    return "\n".join(lines)


def print_audit_report(fig: matplotlib.figure.Figure | None = None, **kwargs) -> list[AuditIssue]:
    """Audit a figure and print the report."""
    issues = audit_figure(fig, **kwargs)
    print(summarize_issues(issues))
    return issues


if __name__ == "__main__":
    print_audit_report()
