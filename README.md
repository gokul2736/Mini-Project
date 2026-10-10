# GeoSentinel

**Research framework:** A Joint Embedding Predictive Architecture for multimodal and explainable geospatial intelligence.

GeoSentinel is an evolving research project exploring self-supervised representation learning for Earth-observation imagery. The repository will be developed incrementally: data acquisition and validation first, preprocessing next, and model implementation only after the input data and evaluation protocol are defined.

> **Research integrity:** Architecture blocks and intended capabilities in this repository are plans until implemented and evaluated. Do not report performance metrics or claim a foundation model without experimental evidence.

## Initial study area

The target study area is the **expanded Chennai Metropolitan Area (CMA), Tamil Nadu, India**. CMDA's published materials describe the expansion from 1,189 km² to 5,904 km² and include parts of Tiruvallur, Kancheepuram, Chengalpattu, and Arakkonam taluk in Ranipet district. The AOI must follow the CMA boundary itself—not entire district boundaries. See the [CMDA reference document](https://cmdachennai.gov.in/pdfs/tenders/BlueGreenInfrastructure/TOR.pdf) and record the chosen boundary source in the provenance register.

## First milestone: AOI Manager

The first implementation milestone is to create a reproducible geospatial boundary workflow:

1. Acquire a documented CMA boundary.
2. Save it as GeoJSON.
3. Validate that the file has a non-empty polygon geometry and WGS 84 longitude/latitude coordinates (EPSG:4326).
4. Record provenance and source information.
5. Use the validated AOI for later satellite and supporting-data searches.

Satellite downloads, weather/DEM collection, JEPA training, multimodal fusion, and model evaluation are **not implemented by this first milestone**.

## Target time periods

The intended historical comparison years are 2018, 2020, 2022, 2024, and 2026. Exact acquisition dates, sensor selection, seasonal windows, cloud thresholds, and compositing choices must be documented before building the final dataset. Sentinel-2's mission began before 2018, so observations may be available for all listed target years; actual scene/product availability and cloud suitability must be checked for the selected AOI and season. Landsat provides a longer historical archive if the study is later extended to earlier years.

## Planned repository structure

```text
Mini-Project/
├── aoi/
├── configs/
│   └── study_area.yaml
├── data/
│   ├── raw/              # ignored by Git; large data stay local
│   ├── interim/
│   └── processed/
├── docs/
│   ├── data-provenance.md
│   └── milestones.md
├── src/geosentinel/aoi/
├── tests/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Data-source policy

- **Optical imagery:** begin with Sentinel-2 Level-2A as the primary candidate; verify coverage, cloud conditions, licensing, and service access before downloading.
- **Historical comparison:** evaluate Landsat where required to cover earlier periods consistently.
- **Weather / INSAT:** investigate MOSDAC after the core AOI and optical imagery workflow is proven.
- **Supporting data:** DEM, hydrology, vegetation indices, and GIS layers are later milestones.
- Never commit API credentials, access tokens, or large satellite scenes to Git.

See [data-sources.md](data-sources.md) for the initial dataset categories.

## Local development setup

Use Python 3.11 or 3.12 in an isolated virtual environment. Follow the setup commands in the project walkthrough and run the tests before making changes.

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
