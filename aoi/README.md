# Area of Interest (AOI)

Place the **verified expanded Chennai Metropolitan Area** boundary here as:

`Chennai_CMA.geojson`

## Correct target boundary

For GeoSentinel, the target is the **expanded CMA (approximately 5,904 km²)** approved by Government Order G.O. Ms. No. 184 dated 21 October 2022, not the old CMA (approximately 1,189 km²), and not the Greater Chennai Corporation (GCC) boundary alone.

CMDA reference material:
- [CMDA Blue-Green Infrastructure Terms of Reference and CMA expansion map](https://cmdachennai.gov.in/pdfs/tenders/BlueGreenInfrastructure/TOR.pdf)
- [CMDA GIS Expert Terms of Reference](https://cmdachennai.gov.in/pdfs/TOR-GIS.pdf)

The expanded CMA includes relevant portions of Chennai, Tiruvallur, Kancheepuram and Chengalpattu districts, plus part of Arakkonam taluk in Ranipet district. Preserve the official CMA perimeter; do not union whole districts to approximate it.

## Candidate screened but NOT accepted as the master AOI

[Community `CMA.geojson`](https://github.com/yashveeeeeeer/india-geodata/raw/main/data/urban/municipal-boundaries/chennai/CMA.geojson) exists, but its bounds and a spherical area check indicate approximately **1,193 km²**, consistent with the old CMA rather than the expanded 5,904 km² area. Its directory README attributes the municipal data to the Transparent Chennai team, but the file does not establish that it is the expanded boundary. Do not rename it as `Chennai_CMA.geojson` or use it to clip the final study dataset.

## Acquisition route

1. Seek the official expanded-CMA boundary as KML, GeoJSON or Shapefile from CMDA / the Tamil Nadu GIS authority.
2. If no vector download is publicly offered, request the digital AOI from the CMDA GIS cell. CMDA GIS procurement material refers to AOIs supplied in KML format.
3. Use the official expansion map only as a visual reference if digitization becomes necessary. Any digitized polygon must be documented as derived/approximate and checked before publication; do not call it an official vector boundary.
4. Record source URL, responsible organization, access date, boundary version/date, license/terms, original CRS, processing steps, and validation results in `docs/data-provenance.md`.

## Validation requirements

- Polygon or MultiPolygon; non-empty and geometrically valid.
- GeoJSON longitude/latitude in WGS 84 (EPSG:4326).
- Spatial extent and area consistent with the expanded CMA, not the old CMA.
- Visual comparison against the CMDA expansion map and district/taluk context.
- Record boundary coverage and provenance before acquisition begins.

Do not commit large satellite scenes in this folder; store only the AOI and small related metadata.
