"""Validation helpers for GeoSentinel Area of Interest (AOI) GeoJSON files."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from shapely.geometry import shape
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from shapely.validation import explain_validity


class AOIValidationError(ValueError):
    """Raised when an AOI file is missing or geometrically invalid."""


def _extract_geometry(document: dict[str, Any]) -> BaseGeometry:
    """Read a GeoJSON geometry, Feature, or FeatureCollection into one geometry."""
    kind = document.get("type")

    if kind == "Feature":
        geometry_data = document.get("geometry")
        if not geometry_data:
            raise AOIValidationError("GeoJSON Feature has no geometry.")
        return shape(geometry_data)

    if kind == "FeatureCollection":
        features = document.get("features")
        if not isinstance(features, list) or not features:
            raise AOIValidationError("GeoJSON FeatureCollection has no features.")

        geometries = []
        for index, feature in enumerate(features):
            if not isinstance(feature, dict) or feature.get("type") != "Feature":
                raise AOIValidationError(
                    f"FeatureCollection item {index} is not a GeoJSON Feature."
                )
            geometry_data = feature.get("geometry")
            if not geometry_data:
                raise AOIValidationError(
                    f"GeoJSON Feature at index {index} has no geometry."
                )
            geometries.append(shape(geometry_data))
        return unary_union(geometries)

    # A raw GeoJSON geometry has a geometry type such as Polygon/MultiPolygon.
    if kind in {"Polygon", "MultiPolygon"}:
        return shape(document)

    raise AOIValidationError(
        "Expected a GeoJSON Polygon, MultiPolygon, Feature, or FeatureCollection."
    )


def validate_geojson(path: str | Path) -> dict[str, Any]:
    """Validate a polygon AOI and return a compact metadata report.

    GeoJSON coordinates are treated as WGS 84 longitude/latitude (EPSG:4326),
    as specified by modern GeoJSON. This function validates a local boundary;
    it does not download or certify an official CMA boundary.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise AOIValidationError(f"AOI file does not exist: {file_path}")
    if not file_path.is_file():
        raise AOIValidationError(f"AOI path is not a file: {file_path}")

    try:
        document = json.loads(file_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AOIValidationError(f"Could not read valid JSON from {file_path}: {exc}") from exc

    if not isinstance(document, dict):
        raise AOIValidationError("GeoJSON root must be an object.")

    # Old GeoJSON files sometimes carry a non-standard CRS member. Do not
    # silently reinterpret coordinates from another coordinate system.
    crs_data = document.get("crs")
    if crs_data:
        crs_name = (
            crs_data.get("properties", {}).get("name", "")
            if isinstance(crs_data, dict)
            else ""
        )
        normalized_crs = crs_name.upper()
        accepted = (
            "4326" in normalized_crs
            or "CRS84" in normalized_crs
            or "CRS:84" in normalized_crs
        )
        if not accepted:
            raise AOIValidationError(
                f"GeoJSON declares a CRS that is not recognized as WGS 84: {crs_name!r}. "
                "Reproject the boundary to EPSG:4326 before validation."
            )

    geometry = _extract_geometry(document)

    if geometry.is_empty:
        raise AOIValidationError("AOI geometry is empty.")
    if geometry.geom_type not in {"Polygon", "MultiPolygon"}:
        raise AOIValidationError(
            f"AOI must be Polygon or MultiPolygon, got {geometry.geom_type}."
        )
    if not geometry.is_valid:
        raise AOIValidationError(f"AOI geometry is invalid: {explain_validity(geometry)}")

    min_lon, min_lat, max_lon, max_lat = geometry.bounds
    bounds = (min_lon, min_lat, max_lon, max_lat)

    if not all(math.isfinite(value) for value in bounds):
        raise AOIValidationError("AOI bounds contain a non-finite coordinate.")
    if not (-180 <= min_lon <= 180 and -180 <= max_lon <= 180):
        raise AOIValidationError("Longitude bounds fall outside [-180, 180].")
    if not (-90 <= min_lat <= 90 and -90 <= max_lat <= 90):
        raise AOIValidationError("Latitude bounds fall outside [-90, 90].")

    return {
        "status": "valid",
        "file": str(file_path),
        "geometry_type": geometry.geom_type,
        "coordinate_reference_system": "EPSG:4326 (GeoJSON longitude/latitude)",
        "bounds": {
            "min_longitude": min_lon,
            "min_latitude": min_lat,
            "max_longitude": max_lon,
            "max_latitude": max_lat,
        },
        "area_geometry_count": len(geometry.geoms) if geometry.geom_type == "MultiPolygon" else 1,
        "note": "Geometry validated; source authority and CMA coverage must be verified separately.",
    }
