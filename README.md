# GeoSentinel

**Research framework:** A Joint Embedding Predictive Architecture for multimodal and explainable geospatial intelligence.

GeoSentinel is an evolving research project exploring self-supervised representation learning for Earth-observation imagery. The repository will be developed incrementally: data acquisition and validation first, preprocessing next, and model implementation only after the input data and evaluation protocol are defined.

> **Research integrity:** Architecture blocks and intended capabilities in this repository are plans until implemented and evaluated. Do not report performance metrics or claim a foundation model without experimental evidence.

## Initial study area

The target study area is the **Chennai Metropolitan Area (CMA), Tamil Nadu, India**, covering the relevant CMA portions of Chennai, Tiruvallur, Kanchipuram, and Chengalpattu districts. The project must use a documented, authoritative or clearly attributed CMA boundary rather than assuming that whole district boundaries equal the CMA.

## First milestone: AOI Manager

The first implementation milestone is to create a reproducible geospatial boundary workflow:

1. Acquire a documented CMA boundary.
2. Save it as GeoJSON.
3. Validate that the file has a non-empty polygon geometry and a declared coordinate reference system (WGS 84 / EPSG:4326 for GeoJSON coordinates).
4. Record provenance and source information.
5. Use the validated AOI for later satellite and supporting-data searches.

Satellite downloads, weather/DEM collection, JEPA training, multimodal fusion, and model evaluation are **not implemented by this first milestone**.

## Target time periods

The intended historical comparison years are 2018, 2020, 2022, 2024, and 2026. Exact acquisition dates, sensor selection, seasonal windows, cloud thresholds, and compositing choices must be documented before building the final dataset. Sentinel-2 cannot provide 2018 observations before its mission's data availability, so the source and temporal coverage should be verified per year.

## Planned repository structure

```text
Mini-Project/
├── aoi/
│   ├── README.md
│   └── .gitkeep
├── configs/
│   └── study_area.yaml
├── data/
│   ├── raw/              # ignored by Git; large data stay local
│   ├── interim/
│   └── processed/
├── docs/
│   ├── data-provenance.md
│   └── milestones.md
├── scripts/
├── src/
│   └── geosentinel/
│       ├── __init__.py
│       └── aoi/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Data-source policy

- **Optical imagery:** begin with Sentinel-2 Level-2A as the primary candidate; verify coverage, cloud conditions, licensing, and service access before downloading.
- **Historical comparison:** evaluate Landsat where required to cover earlier periods consistently.
- **Weather / INSAT:** investigate MOSDAC after the core AOI and optical imagery workflow is proven.
- **Supporting data:** DEM, hydrology, vegetation indices, and GIS layers are later milestones.
- Never commit API credentials, access tokens, or large satellite scenes to Git.

See [data-sources.md](data-sources.md) for the initial dataset categories.

## Development setup

Use Python 3.11 or 3.12 in an isolated virtual environment. Install packages from `requirements.txt`, then run tests and scripts as described in their module README files. The actual setup commands will be added alongside the first runnable AOI module.

## Research workflow

1. AOI Manager and source provenance
2. Satellite catalogue search and metadata capture
3. Small sample download and visual QA
4. Preprocessing and patch generation
5. Establish baselines and evaluation split
6. JEPA adaptation and downstream heads
7. Explainability, ablation, and paper results

## Citation and publication

The IEEE manuscript must distinguish proposed functionality from implemented functionality and report only measured results. Model comparisons should use compatible data splits and metrics. Follow source-specific terms of use and cite the datasets and methods used.
