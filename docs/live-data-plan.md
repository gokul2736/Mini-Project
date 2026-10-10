# GeoSentinel Live and Periodically Updated Data Plan

GeoSentinel will distinguish **historical research data**, **periodically refreshed data**, and **near-real-time products**. These have different temporal and spatial characteristics and must not be treated as interchangeable.

## Historical and reproducible core (Version 1)

- Multi-temporal optical satellite imagery, with acquisition dates and product IDs recorded.
- Verified expanded Chennai Metropolitan Area boundary.
- Supporting reference layers that have documented coverage, dates, CRS and terms of use.
- Reproducible catalogue queries and a metadata manifest.

The first JEPA experiments should use fixed historical scenes or versioned composites so results can be reproduced. A moving live feed should not silently change the benchmark between runs.

## Candidate near-real-time inputs (later integration)

| Input | Possible source to investigate | Update character | Intended role |
|---|---|---|---|
| Cloud / atmospheric satellite imagery | INSAT products through MOSDAC | Intraday / product-dependent | Weather context, cloud monitoring |
| Precipitation estimates | MOSDAC, IMD, or NASA GPM products | Product-dependent; some near-real-time | Rainfall context and flood-related analysis |
| Air-quality station observations | CPCB / TNPCB services or published datasets | Station/API-dependent | Environmental context; verify access and refresh cadence |
| Flood alerts / event reports | Official disaster-management and meteorological channels | Event-driven | Context and alerts, not direct substitute for satellite ground truth |
| Water level / reservoir observations | Relevant water-resource agencies | Often periodic; access varies | Hydrology context after validation |

These are candidate sources, not promises of public APIs or guaranteed real-time availability. Before integration, verify API documentation, authentication, licence/terms, spatial coverage, time resolution, latency and historical backfill.

## Data architecture

1. Catalogue/search service — discover data and record query parameters.
2. Historical ingestion — retrieve fixed acquisitions and versioned products for experiments.
3. Near-real-time ingestion — optional scheduled polling/ingestion for products that officially support it.
4. Metadata/provenance register — capture acquisition time, publication time, source, product ID and processing version.
5. Common AOI and harmonization — crop/reproject/resample only where scientifically valid.
6. Quality checks — detect stale data, missing periods, duplicate scenes and invalid geometry.
7. Storage policy — keep raw data immutable; publish processed versions separately.

## Important distinction

Sentinel-2 is a periodically revisiting optical mission, not a continuous live camera. INSAT weather imagery can refresh much more frequently but is generally much coarser than Sentinel-2. Do not fuse them pixel-for-pixel without a scientifically justified temporal/spatial harmonization method.

The near-real-time dashboard is a later extension. The first milestone is to validate the expanded CMA AOI and build a small, reproducible satellite catalogue.
