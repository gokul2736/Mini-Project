# Area of Interest (AOI)

Place the verified Chennai Metropolitan Area boundary here as:

`Chennai_CMA.geojson`

## Boundary requirements

- Prefer a boundary published by CMDA or another authoritative government source.
- Record the exact source URL, download date, version/date of the boundary, usage terms, and any transformation performed in `docs/data-provenance.md`.
- Ensure the polygon represents the **CMA**, including only the relevant portions of surrounding districts. Do not union entire districts as a substitute for the CMA.
- Use GeoJSON longitude/latitude coordinates in WGS 84 (EPSG:4326).
- Do not commit large satellite scenes here; this folder is only for small AOI boundary files and their metadata.

The repository currently does not contain a verified CMA boundary. Do not create a hand-drawn or approximate boundary and describe it as official.
