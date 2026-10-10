# Area of Interest (AOI)

Place the **verified expanded Chennai Metropolitan Area** boundary here as:

`Chennai_CMA.geojson`

## Correct target boundary

For GeoSentinel, the target is the **expanded CMA (approximately 5,904 km²)** approved by Government Order G.O. Ms. No. 184 dated 21 October 2022, not the old CMA (approximately 1,189 km²), and not the Greater Chennai Corporation (GCC) boundary alone.

CMDA reference material:
- [CMDA Blue-Green Infrastructure Terms of Reference and CMA expansion map](https://cmdachennai.gov.in/pdfs/tenders/BlueGreenInfrastructure/TOR.pdf)
- [CMDA Study of Demand and Supply Pattern of Housing in CMA](https://cmdachennai.gov.in/pdfs/tenders/DSPH/TOR.pdf)
- [Tamil Nadu GIS — CUMTA map editor](https://tngis.tn.gov.in/apps/cumta/)

The expanded CMA includes relevant portions of Chennai, Tiruvallur, Kancheepuram and Chengalpattu districts, plus part of Arakkonam taluk in Ranipet district. Preserve the official CMA perimeter; do not union whole districts to approximate it.

## First vector candidate to download and verify

[OpenCity: Chennai Urban Metropolitan Transport Authority Boundary](https://data.opencity.in/dataset/chennai-urban-metropolitan-transport-authority-boundary) lists a resource named **CUMTA Boundary Map** in GeoJSON format. The listing identifies CUMTA as the source and labels the licence as “Other (Public Domain)”, with a last-updated date of 13 May 2026.

This is a **candidate, not an accepted master AOI yet**. Download the GeoJSON and verify that the extent represents the expanded CMA rather than only a transport-planning or older CMA extent. Record the exact file URL and licence text shown at download time.

## Candidate screened and rejected as master AOI

[Community `CMA.geojson`](https://github.com/yashveeeeeeer/india-geodata/raw/main/data/urban/municipal-boundaries/chennai/CMA.geojson) has a bounding extent of approximately 80.0039–80.3453° E and 12.8515–13.2924° N. A spherical ring-area estimate is approximately **1,193 km²**, consistent with the old CMA rather than the expanded 5,904 km² area. Its directory README attributes the municipal data to the Transparent Chennai team, but this geometry does not establish the expanded 2022 CMA. Do not rename it as `Chennai_CMA.geojson` or use it to clip the final study dataset.

## Download and validation procedure

1. Open the OpenCity CUMTA boundary dataset page linked above.
2. Under **Data and Resources**, choose **CUMTA Boundary Map — GeoJSON**, then use **Download**.
3. Keep the untouched file temporarily as `aoi/candidates/CUMTA_Boundary_candidate.geojson`; do not overwrite the master filename yet.
4. Run the GeoSentinel GeoJSON validator and inspect the result in QGIS.
5. Check the polygon/multipolygon geometry, CRS, bounding extent, approximate area, and whether it matches the expanded CMA map from CMDA.
6. If the boundary is confirmed, record its source URL, publisher, access date, boundary version/date, licence/terms, CRS, processing history and validation results in `docs/data-provenance.md`; then save the accepted file as `aoi/Chennai_CMA.geojson`.
7. If it looks like the old boundary or CUMTA jurisdiction does not match CMA, do not use it as the master AOI. Request the vector from CMDA/TNGIS instead.

## Validation requirements

- Polygon or MultiPolygon; non-empty and geometrically valid.
- GeoJSON longitude/latitude in WGS 84 (EPSG:4326).
- Spatial extent and area consistent with the expanded CMA, not the old CMA.
- Visual comparison against the CMDA expansion map and district/taluk context.
- Record boundary coverage and provenance before acquisition begins.

Do not commit large satellite scenes in this folder; store only the AOI and small related metadata.
