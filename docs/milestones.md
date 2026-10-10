# GeoSentinel Milestones

## M1 — Expanded CMA AOI
- [x] Define target study area and boundary policy.
- [x] Implement GeoJSON polygon validation.
- [x] Add tests for valid and invalid geometries.
- [x] Screen the community `CMA.geojson`; reject it as master AOI because its area is approximately 1,193 km², consistent with the old CMA.
- [ ] Download the OpenCity CUMTA boundary GeoJSON candidate.
- [ ] Verify geometry, CRS, extent and area against the CMDA expanded-CMA map.
- [ ] If confirmed, save as `aoi/Chennai_CMA.geojson` and complete the provenance register; otherwise request the expanded boundary from CMDA/TNGIS.

## M2 — Satellite catalogue search
- [ ] Choose the catalogue/service after confirming access requirements.
- [ ] Search for suitable imagery over the accepted AOI and planned time windows.
- [ ] Save a machine-readable metadata manifest.

## M3 — Small sample download
- [ ] Download a small number of test scenes.
- [ ] Check coverage, cloud quality, bands, resolution, CRS, and terms of use.
- [ ] Keep large data out of Git.

## M4 — Preprocessing
- [ ] Cloud/shadow masking.
- [ ] Spatial alignment and common grid.
- [ ] Normalization and patch extraction.

## M5 — Baselines and JEPA experiments
- [ ] Define leakage-safe train/validation/test split.
- [ ] Implement reproducible baselines.
- [ ] Implement/adapt JEPA and downstream tasks.
- [ ] Run quantitative evaluation and ablations.

## M6 — Near-real-time data extension
- [ ] Select one official near-real-time product (for example an INSAT/MOSDAC weather product).
- [ ] Verify credentials, dataset ID, resolution, refresh cadence, licence and spatial coverage.
- [ ] Implement a separate ingestion job with timestamps, freshness checks and immutable raw storage.
- [ ] Keep live-ingestion experiments separate from the fixed historical benchmark.

## M7 — Publication
- [ ] Use only verified references and measured results.
- [ ] Document limitations, data provenance, and reproducibility.
