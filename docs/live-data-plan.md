# GeoSentinel Live and Periodically Updated Data Plan

GeoSentinel will distinguish **historical research data**, **periodically refreshed data**, and **near-real-time products**. These have different temporal and spatial characteristics and must not be treated as interchangeable.

## Historical and reproducible core (Version 1)

- Verified expanded Chennai Metropolitan Area boundary.
- Multi-temporal optical satellite imagery with acquisition dates and product IDs recorded.
- Supporting reference layers that have documented coverage, dates, CRS and terms of use.
- Reproducible catalogue queries and a metadata manifest.

The first JEPA experiments should use fixed historical scenes or versioned composites so results can be reproduced. A moving live feed should not silently change the benchmark between runs.

## Candidate near-real-time inputs (later integration)

| Input | Source to investigate | Update character | Intended role |
|---|---|---|---|
| Cloud / atmospheric satellite imagery | [INSAT products via MOSDAC](https://mosdac.gov.in/insat-3d-data-products) | Intraday / product-dependent | Weather context, cloud monitoring |
| Precipitation estimates | [MOSDAC download API](https://mosdac.gov.in/downloadapi-manual), IMD or NASA GPM products | Product-dependent; some near-real-time | Rainfall context and flood-related analysis |
| Air-quality station observations | CPCB / TNPCB services or published datasets | Station/API-dependent | Environmental context; verify access and refresh cadence |
| Flood alerts / event reports | Official disaster-management and meteorological channels | Event-driven | Context and alerts, not a substitute for satellite ground truth |
| Water level / reservoir observations | Relevant water-resource agencies | Often periodic; access varies | Hydrology context after validation |

### MOSDAC feasibility

MOSDAC's published download API manual describes a configuration-driven Python client for retrieving archived and near-real-time products. It requires Python 3+, the `requests` package, MOSDAC account credentials, and a dataset ID. The selected product's actual refresh rate, coverage, bounding-box support, licence/terms and latency must still be checked.

INSAT-3D products include atmospheric and meteorological variables such as quantitative precipitation estimation, cloud mask, cloud-motion vectors, outgoing longwave radiation, sea-surface temperature and humidity products. These provide weather context, but their spatial resolution is generally much coarser than Sentinel-2 imagery; they should not be treated as pixel-aligned inputs without a scientifically justified harmonization step.

Sources:
- [MOSDAC Data Download API manual](https://mosdac.gov.in/downloadapi-manual)
- [MOSDAC INSAT-3D data products](https://mosdac.gov.in/insat-3d-data-products)
- [ISRO MOSDAC overview](https://www.isro.gov.in/MOSDAC.html)

These are candidate sources, not promises that every dataset has a public endpoint or is continuously available. Before integration, verify authentication, licence/terms, spatial coverage, time resolution, latency and historical backfill.

## Data architecture

1. Boundary/AOI manager — defines the validated spatial extent used consistently by all source collectors.
2. Catalogue/search service — discover data and record query parameters.
3. Historical ingestion — retrieve fixed acquisitions and versioned products for experiments.
4. Near-real-time ingestion — optional scheduled polling/ingestion for products that officially support it.
5. Metadata/provenance register — capture acquisition time, publication time, source, product ID and processing version.
6. Common AOI and harmonization — crop/reproject/resample only where scientifically valid.
7. Quality checks — detect stale data, missing periods, duplicate scenes and invalid geometry.
8. Storage policy — keep raw data immutable; publish processed versions separately.

## Important distinction

Sentinel-2 is a periodically revisiting optical mission, not a continuous live camera. INSAT weather imagery can refresh much more frequently but is generally coarser than Sentinel-2. Live data are a separate operational extension; historical, versioned data should underpin the first publication's reproducible experiments.

The immediate task remains: download the CUMTA-boundary GeoJSON candidate, verify whether it matches the expanded CMA, and record provenance before collecting satellite scenes.
