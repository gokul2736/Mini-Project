import json

import pytest

from geosentinel.aoi.validator import AOIValidationError, validate_geojson


def write_geojson(tmp_path, data):
    path = tmp_path / "aoi.geojson"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_accepts_valid_polygon(tmp_path):
    path = write_geojson(
        tmp_path,
        {
            "type": "Feature",
            "properties": {"name": "test"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [80.0, 12.0],
                    [80.2, 12.0],
                    [80.2, 12.2],
                    [80.0, 12.2],
                    [80.0, 12.0],
                ]],
            },
        },
    )

    report = validate_geojson(path)

    assert report["status"] == "valid"
    assert report["geometry_type"] == "Polygon"
    assert report["coordinate_reference_system"].startswith("EPSG:4326")
    assert report["bounds"]["min_longitude"] == pytest.approx(80.0)


def test_rejects_missing_file(tmp_path):
    with pytest.raises(AOIValidationError, match="does not exist"):
        validate_geojson(tmp_path / "missing.geojson")


def test_rejects_non_polygon_geometry(tmp_path):
    path = write_geojson(
        tmp_path,
        {"type": "Point", "coordinates": [80.0, 13.0]},
    )

    with pytest.raises(AOIValidationError, match="Expected a GeoJSON"):
        validate_geojson(path)


def test_rejects_invalid_polygon(tmp_path):
    # Self-intersecting bow-tie polygon.
    path = write_geojson(
        tmp_path,
        {
            "type": "Polygon",
            "coordinates": [[
                [80.0, 12.0],
                [81.0, 13.0],
                [80.0, 13.0],
                [81.0, 12.0],
                [80.0, 12.0],
            ]],
        },
    )

    with pytest.raises(AOIValidationError, match="geometry is invalid"):
        validate_geojson(path)


def test_rejects_out_of_range_coordinates(tmp_path):
    path = write_geojson(
        tmp_path,
        {
            "type": "Polygon",
            "coordinates": [[
                [200.0, 12.0],
                [201.0, 12.0],
                [201.0, 13.0],
                [200.0, 13.0],
                [200.0, 12.0],
            ]],
        },
    )

    with pytest.raises(AOIValidationError, match="Longitude bounds"):
        validate_geojson(path)
