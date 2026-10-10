"""Command-line entry point for validating a GeoSentinel AOI GeoJSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from geosentinel.aoi.validator import AOIValidationError, validate_geojson


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="geosentinel-validate-aoi",
        description="Validate a polygon AOI GeoJSON file and print its metadata.",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input AOI GeoJSON file.",
    )
    parser.add_argument(
        "--report",
        help="Optional path to write the JSON validation report.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        report = validate_geojson(args.input)
    except AOIValidationError as exc:
        print(f"AOI validation failed: {exc}", file=sys.stderr)
        return 2

    output = json.dumps(report, indent=2)
    print(output)

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(output + "\n", encoding="utf-8")
        print(f"Report written to: {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
