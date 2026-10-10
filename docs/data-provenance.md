# Data Provenance Register

Record the source and processing history for every external dataset used by GeoSentinel.

## Chennai Metropolitan Area boundary

| Field | Value |
|---|---|
| Dataset | Expanded Chennai Metropolitan Area boundary |
| Required extent | Approximately 5,904 km² (expanded CMA, approved in 2022) |
| Local path | `aoi/Chennai_CMA.geojson` |
| Official reference | [CMDA Blue-Green Infrastructure TOR / expansion map](https://cmdachennai.gov.in/pdfs/tenders/BlueGreenInfrastructure/TOR.pdf) |
| Official digital vector source | Pending: request/verify KML, GeoJSON or Shapefile from CMDA / Tamil Nadu GIS |
| Access/download date | Pending |
| Boundary version/date | Expanded CMA, approved by G.O. Ms. No. 184 dated 2022-10-21; vector version pending |
| License / terms of use | Pending for the digital vector |
| Original CRS | Pending |
| Output CRS | EPSG:4326 |
| Processing performed | Pending |
| Verification status | Not acquired. Do not use a vector AOI until it is confirmed to represent the expanded CMA. |

### Candidate assessed and rejected for the master AOI

The community file at [india-geodata `chennai/CMA.geojson`](https://github.com/yashveeeeeeer/india-geodata/raw/main/data/urban/municipal-boundaries/chennai/CMA.geojson) has a bounding extent of approximately 80.0039–80.3453° E and 12.8515–13.2924° N. A spherical ring-area estimate is approximately 1,193 km², which matches the old CMA size and is inconsistent with the expanded 5,904 km² target. Treat it as an unverified legacy candidate only; do not use it for final cropping, model evaluation, or paper claims.

The community repository's Chennai README attributes the municipal data to the Transparent Chennai team and states CC BY-SA 2.5 India for that dataset. This provenance does not establish that the polygon represents the expanded 2022 CMA.

## Satellite imagery and supporting datasets

For each scene or product, record provider, product ID, acquisition time, spatial resolution, bands/variables, cloud information if provided, CRS, license/terms, query parameters, and local path. Keep credentials out of this file.

Do not mark a dataset as acquired until the files have been downloaded and checked.
