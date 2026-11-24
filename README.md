# Mini-Project

## GeoSentinel: A Joint-Embedding Predictive Architecture for Explainable Geospatial Change Detection

**GeoSentinel** is a research-oriented multimodal geospatial intelligence framework designed to learn meaningful representations of Earth's surface using satellite observations, meteorological information, terrain, hydrological data and other geospatial sources.

The central research component is a **Joint-Embedding Predictive Architecture (JEPA)** designed to learn spatial and temporal representations without relying exclusively on pixel-level reconstruction.

The framework aims to support explainable geospatial change detection and environmental intelligence through multimodal representation learning, downstream prediction and spatial decision support.

---

## 🎯 Project Objectives

- Develop a multimodal geospatial data processing pipeline.
- Integrate satellite observations through the Bhoonidhi data-access platform.
- Combine satellite, meteorological, hydrological and geospatial information.
- Investigate JEPA-based spatial and temporal representation learning.
- Develop explainable geospatial change-detection methods.
- Evaluate learned representations against conventional machine-learning baselines.
- Build an interactive GIS-based environmental intelligence dashboard.

---

# 🏗️ SYSTEM ARCHITECTURE

```text
                              🌍 EARTH
                                  |
                                  ▼
══════════════════════════════════════════════════════════════════
                   MULTI-SOURCE EARTH OBSERVATION
══════════════════════════════════════════════════════════════════

     SATELLITE DATA          ENVIRONMENTAL DATA       GEOSPATIAL DATA
          |                         |                       |
    ┌──────────────┐         ┌──────────────┐        ┌──────────────┐
    │ Bhoonidhi    │         │ Rainfall     │        │ Administrative│
    │ Sentinel-1   │         │ Temperature  │        │ Boundaries    │
    │ Sentinel-2*  │         │ Humidity     │        │ Waterbodies   │
    │ Resourcesat* │         │ Wind Speed   │        │ Rivers        │
    │ EOS-04*      │         │ Air Quality  │        │ Drainage      │
    │ NISAR*       │         │ Groundwater  │        │ Infrastructure│
    │ CartoDEM*    │         │ Reservoirs   │        │ Land Use      │
    └──────────────┘         └──────────────┘        └──────────────┘
          |                         |                       |
          └─────────────────────────┼───────────────────────┘
                                    |
                                    ▼
══════════════════════════════════════════════════════════════════
                       DATA ACQUISITION LAYER
══════════════════════════════════════════════════════════════════

                         BHOONIDHI CONNECTOR
                                  |
                   Authentication and Token Handling
                                  |
                       STAC Product Discovery
                                  |
                       AOI and Date Filtering
                                  |
                     Product Availability Check
                                  |
                       Satellite Data Download
                                  |
                         Metadata and Provenance

          Existing Dataset Collection + Weather Intelligence
                                  |
                                  ▼
══════════════════════════════════════════════════════════════════
                    DATA VALIDATION AND QUALITY CONTROL
══════════════════════════════════════════════════════════════════

       File Format Validation       CRS Validation
       Geometry Validation         Temporal Validation
       Missing Data Analysis       Duplicate Detection
       Spatial Coverage            Data Provenance
       Data Quality Assessment
                                  |
                                  ▼
══════════════════════════════════════════════════════════════════
                       DATA PREPROCESSING
══════════════════════════════════════════════════════════════════

       Raster Processing            Vector Processing
       Image Registration           Geometry Validation
       Spatial Alignment            CRS Harmonisation
       Cloud / Quality Masks        Feature Extraction
       Normalisation                Temporal Alignment
       Patch Generation             Missing Modality Masks
                                  |
                                  ▼
══════════════════════════════════════════════════════════════════
                  MULTIMODAL SPATIOTEMPORAL DATASET
══════════════════════════════════════════════════════════════════

       Satellite Representations
       Meteorological Features
       Hydrological Features
       Environmental Features
       Geospatial Features
       Spatial and Temporal Context
       Modality Availability Masks
                                  |
                                  ▼
══════════════════════════════════════════════════════════════════
                  GEOSENTINEL-JEPA RESEARCH MODEL
══════════════════════════════════════════════════════════════════

                     CONTEXT ENCODER
                            |
                     Context Embeddings
                            |
                            ▼
                       PREDICTOR
                            |
                  Predicted Target Embeddings
                            |
                            ▲
                     Target Embeddings
                            |
                      TARGET ENCODER
                            |
                   EMA Target Updates
                            |
                            ▼
                  JOINT EMBEDDING LOSS
                            |
                            ▼
                 LEARNED EARTH REPRESENTATIONS
                            |
                            ▼
══════════════════════════════════════════════════════════════════
                    DOWNSTREAM INTELLIGENCE
══════════════════════════════════════════════════════════════════

       Spatial Change Detection
       Temporal Change Analysis
       Environmental Classification
       Land-Cover Analysis
       Hydrological Pattern Analysis
       Geospatial Feature Understanding
                            |
                            ▼
══════════════════════════════════════════════════════════════════
                     MODEL EVALUATION
══════════════════════════════════════════════════════════════════

       Conventional ML Baselines
       JEPA Representation Evaluation
       Modality Ablation Studies
       Spatial Generalisation
       Temporal Generalisation
       Missing-Modality Robustness
       Precision / Recall / F1
       IoU / Dice (where applicable)
       MAE / RMSE (where applicable)
                            |
                            ▼
══════════════════════════════════════════════════════════════════
                    EXPLAINABLE AI MODULE
══════════════════════════════════════════════════════════════════

       Feature Attribution
       SHAP for Compatible Downstream Models
       Integrated Gradients
       Embedding Analysis
       Spatial Evidence Visualisation
       Confidence and Uncertainty Analysis
                            |
                            ▼
══════════════════════════════════════════════════════════════════
                    GEOSENTINEL DASHBOARD
══════════════════════════════════════════════════════════════════

       Interactive GIS Visualisation
       Study Area Exploration
       Satellite Data Viewer
       Temporal Comparison
       Environmental Indicators
       Model Evaluation
       Explainability Visualisation
       Reports and Data Export
       Decision-Support Outputs
                            |
                            ▼
══════════════════════════════════════════════════════════════════
                         FUTURE EXTENSIONS
══════════════════════════════════════════════════════════════════

       Multi-Task Geospatial Learning
       Land Suitability Analysis
       Agricultural Intelligence
       Infrastructure Suitability
       Disaster Risk Assessment
       Urban Growth Analysis
       Forest and Waterbody Monitoring
       Climate Pattern Analysis
       Natural Language Geospatial Assistant
       Earth Knowledge Graph
       GeoSentinel AI Assistant
```

*Satellite collections marked with an asterisk are candidates, not guaranteed acquisitions. Their actual availability, spatial coverage, access permissions and suitability must be verified through Bhoonidhi.*

---

## 🛰️ 1. Data Acquisition Layer

GeoSentinel integrates multiple sources of Earth observation and environmental information.

### Bhoonidhi — Primary Satellite Data Gateway

The Bhoonidhi platform, operated by NRSC/ISRO, is used as the primary satellite-data discovery and acquisition interface.

Potential collections include:

| Collection | Potential application |
|---|---|
| Sentinel-1 SAR | Surface and flood-related observations |
| Resourcesat | Land-surface and vegetation analysis |
| EOS-04 | Radar-based surface observations |
| NISAR | Radar-based Earth observation |
| CartoDEM | Terrain and elevation analysis |
| Other available collections | Depending on coverage and access |

The system uses authentication, STAC search, AOI filtering, temporal filtering, product availability checks and controlled downloads.

### Environmental and Geospatial Datasets

Existing collected datasets include:

- Rainfall and meteorological records.
- Groundwater measurements.
- Reservoir and lake observations.
- Historical flood information.
- Waterbodies and drainage networks.
- Air-quality observations.
- Administrative boundaries.
- Environmental and civic infrastructure information.

### Weather Intelligence

The existing Weather Intelligence module provides:

- Open-Meteo integration.
- IMD public observations and weather warnings.
- Current weather conditions.
- Hourly and daily forecasts.
- Soil and environmental variables.
- Weather data storage and visualisation.

---

## 🧹 2. Data Engineering and Preprocessing

The preprocessing pipeline converts heterogeneous Earth observation datasets into consistent model-ready inputs.

### Processing operations

- Format and schema validation.
- Coordinate reference system harmonisation.
- Spatial geometry validation.
- Raster quality inspection.
- Image registration where required.
- Cloud and quality masking where applicable.
- Temporal alignment.
- Feature extraction.
- Normalisation.
- Spatial patch generation.
- Missing-modality handling.

All datasets retain source information and processing provenance.

Original raw data is preserved separately from processed datasets.

---

## 🧠 3. GeoSentinel-JEPA — Core Research Contribution

The central research objective is to investigate JEPA-based representation learning for multimodal geospatial data.

### Model components

**Context Encoder**

Extracts representations from available spatial and temporal context.

**Target Encoder**

Generates target representations and is updated using an exponential moving average of the context encoder parameters.

**Predictor**

Predicts target representations from contextual embeddings and relevant spatial or temporal information.

**JEPA Objective**

The model learns to predict latent representations instead of reconstructing the original input data directly.

### Research directions

- Spatial representation learning.
- Temporal representation learning.
- Multimodal representation learning.
- Spatial and temporal masking.
- Missing-modality robustness.
- Downstream geospatial change analysis.

The implementation will be developed incrementally and evaluated against conventional baselines.

---

## 🌏 4. Geospatial Intelligence Layer

The learned representations can be evaluated through downstream environmental and geospatial tasks.

Initial research priorities:

1. Spatial representation analysis.
2. Temporal change analysis.
3. Environmental feature understanding.
4. Land-cover or environmental classification where suitable labels exist.
5. Flood-related analysis where reliable reference labels are available.

Potential future capabilities include:

- Land suitability analysis.
- Agricultural recommendations.
- Infrastructure suitability assessment.
- Disaster-risk assessment.
- Urban growth analysis.
- Forest monitoring.
- Waterbody monitoring.
- Environmental health assessment.

These are planned applications, not claims of currently implemented functionality.

---

## 📊 5. Model Training and Evaluation

Model development and experimentation will use Google Colab with an NVIDIA T4 GPU, accessed through VS Code.

### Training infrastructure

- PyTorch.
- CUDA-enabled GPU runtime.
- Mixed-precision training where supported.
- Checkpoint management.
- Experiment configuration.
- Training and validation logging.
- Reproducible random seeds.

### Evaluation metrics

| Metric | Application |
|---|---|
| Precision | Classification |
| Recall | Classification |
| F1-score | Classification |
| AUROC / PR-AUC | Classification where appropriate |
| IoU | Segmentation |
| Dice Score | Segmentation |
| MAE / RMSE | Regression |
| Cohen's Kappa | Classification agreement |

Additional research experiments:

- Baseline comparisons.
- Modality ablation.
- Spatial generalisation.
- Temporal generalisation.
- Missing-modality experiments.
- Hyperparameter sensitivity.

Metrics will only be reported after the corresponding experiments have been completed.

---

## 🔍 6. Explainable AI

GeoSentinel aims to provide interpretable evidence alongside its downstream predictions.

Potential methods include:

- SHAP for compatible downstream predictive models.
- Integrated Gradients.
- Feature attribution.
- Embedding-space analysis.
- Spatial evidence visualisation.
- Confidence and uncertainty analysis.

The objective is to help users understand which inputs and spatial patterns contribute to a prediction.

---

## 🖥️ 7. User Interaction and Decision Support

The Streamlit-based dashboard provides a common interface for exploring datasets and model outputs.

Planned capabilities:

- Interactive GIS dashboard.
- Study-area visualisation.
- Satellite product exploration.
- Timeline comparison.
- Environmental indicators.
- Model evaluation.
- Explainability visualisations.
- Spatial result maps.
- Data and report export.

Decision-support recommendations will be added only when supported by validated models, reliable evidence and appropriate domain constraints.

---

## 🚀 8. Future Extensions — Version 2

Potential long-term extensions include:

- Multi-task geospatial foundation models.
- Natural-language geospatial queries.
- Large Language Model integration.
- Earth Knowledge Graph.
- Agricultural decision support.
- Infrastructure planning support.
- Environmental risk assessment.
- GeoSentinel AI Assistant.

Example future interactions:

- "How has this region changed since 2018?"
- "Which environmental factors are associated with groundwater decline?"
- "What are the land characteristics of this location?"
- "What evidence supports this environmental risk assessment?"

---

## 💻 Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Deep Learning | PyTorch |
| Architecture | JEPA |
| Geospatial | GeoPandas, Rasterio, Shapely, PyProj |
| Satellite Data | Bhoonidhi API, STAC |
| Data Processing | NumPy, Pandas, Xarray |
| Visualisation | Matplotlib, Plotly, Folium |
| Dashboard | Streamlit |
| Explainability | SHAP, Captum |
| Training | Google Colab NVIDIA T4 |
| Development | VS Code |
| Testing | Pytest |
| Code Quality | Pylint |
| Version Control | Git and GitHub |

---

## 📁 Project Structure

```text
GeoSentinel/
│
├── config.yaml
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
│
├── config/
│   ├── study_area.yaml
│   └── model.yaml
│
├── data/
│   ├── inbox/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   ├── weather/
│   └── manifests/
│
├── src/
│   └── geosentinel/
│       │
│       ├── integrations/
│       │   └── bhoonidhi/
│       │       ├── auth.py
│       │       ├── client.py
│       │       ├── search.py
│       │       ├── downloader.py
│       │       └── metadata.py
│       │
│       ├── weather/
│       │   ├── schema.py
│       │   ├── locations.py
│       │   ├── manager.py
│       │   ├── storage.py
│       │   └── providers/
│       │
│       ├── preprocessing/
│       │   ├── vector/
│       │   ├── tabular/
│       │   ├── temporal/
│       │   └── raster/
│       │
│       ├── dataset/
│       │   ├── inventory.py
│       │   ├── validation.py
│       │   ├── alignment.py
│       │   ├── samples.py
│       │   └── splits.py
│       │
│       ├── models/
│       │   └── jepa/
│       │       ├── encoder.py
│       │       ├── predictor.py
│       │       ├── target_encoder.py
│       │       ├── masking.py
│       │       ├── loss.py
│       │       └── model.py
│       │
│       ├── training/
│       ├── explainability/
│       └── dashboard/
│
├── tests/
│
├── notebooks/
│
├── experiments/
│   ├── configs/
│   ├── logs/
│   ├── metrics/
│   ├── checkpoints/
│   └── figures/
│
├── reports/
│
└── docs/
    ├── architecture.md
    ├── methodology.md
    └── data_dictionary.md
```

*This is the intended logical structure. Existing directories and modules will be reused wherever possible rather than duplicated.*

---

## 📍 Study Area

**Expanded Chennai Metropolitan Area (CMA), Tamil Nadu, India.**

The study area covers approximately 5,904 km², subject to validation against the authoritative expanded-CMA boundary.

The research focuses on spatial and temporal environmental patterns across the study area.



## 🔬 Research and Reproducibility

GeoSentinel is developed as a research project. Its experimental results must be reproducible and supported by documented datasets, preprocessing procedures
```
