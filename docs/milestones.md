# GeoSentinel Milestones

## M1 — AOI Manager
- [x] Define target study area and boundary policy.
- [x] Implement GeoJSON polygon validation.
- [x] Add tests for valid and invalid geometries.
- [ ] Acquire the authoritative/attributed Chennai CMA boundary.
- [ ] Validate the real boundary and record its provenance.

## M2 — Satellite catalogue search
- [ ] Choose the catalogue/service after confirming access requirements.
- [ ] Search for suitable imagery over the AOI and planned time windows.
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

## M6 — Publication
- [ ] Use only verified references and measured results.
- [ ] Document limitations, data provenance, and reproducibility.
