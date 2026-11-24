# GeoSentinel

## A Joint-Embedding Predictive Architecture for Explainable Geospatial Change Detection

<p align="center">
  <img src="https://images.openai.com/static-rsc-4/S15lz4PBf4oBGDUNKfPZfGA1sSlLipzh_RFSe73MmgQ2NgnKw_XKMy_PIE8ml9lXielbnHRwyviP5JdVLCvcCsCilcn5vbzqg-7_QEw8AvKupHSYVt5pl8zA4MhR1wHaT2Z6Qta7TMI2tqiKbiyVcVIBIMa9takHUS5YpWjJKTK6120NvbL7WwIRsivJ_r0D?purpose=fullsize" width="100%">
</p>

<p align="center">
  <strong>Multimodal Geospatial Intelligence • Self-Supervised Representation Learning • Explainable AI</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Research%20Software-blue">
  <img src="https://img.shields.io/badge/Architecture-JEPA-purple">
  <img src="https://img.shields.io/badge/Language-Python-yellow">
  <img src="https://img.shields.io/badge/Framework-PyTorch-red">
  <img src="https://img.shields.io/badge/Interface-Streamlit-orange">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

# Table of Contents

1. [Document Control](#document-control)
2. [System Identification](#system-identification)
3. [Purpose and Scope](#purpose-and-scope)
4. [System Overview](#system-overview)
5. [System Architecture](#system-architecture)
6. [System Boundaries](#system-boundaries)
7. [Functional Requirements](#functional-requirements)
8. [Non-Functional Requirements](#non-functional-requirements)
9. [Data Requirements and Specifications](#data-requirements-and-specifications)
10. [External System Interfaces](#external-system-interfaces)
11. [JEPA Model Specification](#jepa-model-specification)
12. [Training and Experimental Specifications](#training-and-experimental-specifications)
13. [Explainability and Decision Support](#explainability-and-decision-support)
14. [Application and User Interface](#application-and-user-interface)
15. [Security and Data Governance](#security-and-data-governance)
16. [Technology Stack](#technology-stack)
17. [Software Architecture and Repository Structure](#software-architecture-and-repository-structure)
18. [Verification and Validation](#verification-and-validation)
19. [Deployment and Execution Environment](#deployment-and-execution-environment)
20. [Implementation Status](#implementation-status)
21. [Future System Extensions](#future-system-extensions)
22. [Research References](#research-references)

---

<a id="document-control"></a>
# 1. Document Control

| Attribute | Specification |
|---|---|
| Project Name | GeoSentinel |
| Project Classification | Research-oriented geospatial software system |
| Research Domain | Artificial Intelligence, Remote Sensing and Geospatial Analytics |
| Core Architecture | Joint-Embedding Predictive Architecture (JEPA) |
| Primary Language | Python |
| Deep Learning Framework | PyTorch |
| Application Interface | Streamlit |
| Study Area | Expanded Chennai Metropolitan Area, Tamil Nadu, India |
| Target Computing Environment | Google Colab NVIDIA T4 |
| Development Environment | Visual Studio Code |
| Documentation Type | Software Requirements and Architecture Specification |
| Version | 1.0 — Development Specification |
| Last Updated | 24 November 2026 |

**Document purpose:** Define the system requirements, architecture, interfaces, data specifications, operational constraints and verification criteria governing GeoSentinel development.

---

<a id="system-identification"></a>
# 2. System Identification

## 2.1 System Name

**GeoSentinel: A Joint-Embedding Predictive Architecture for Explainable Geospatial Change Detection**

## 2.2 System Classification

GeoSentinel is a modular, multimodal geospatial intelligence system intended to process heterogeneous Earth observation data and learn spatial-temporal representations using self-supervised predictive learning.

The system combines:

- Satellite observations.
- Meteorological observations.
- Hydrological measurements.
- Terrain and elevation information.
- Environmental datasets.
- Administrative and infrastructure GIS layers.

## 2.3 Intended Users

| User Category | Intended Interaction |
|---|---|
| Researcher | Model development, experimentation and evaluation |
| Geospatial Analyst | Spatial data exploration and change analysis |
| Environmental Analyst | Environmental indicator assessment |
| Agricultural Researcher | Land and vegetation analysis |
| Decision-Support User | Interpretation of validated spatial outputs |
| Developer | Integration, testing and maintenance |

---

<a id="purpose-and-scope"></a>
# 3. Purpose and Scope

## 3.1 Purpose

The purpose of GeoSentinel is to establish a unified software architecture for learning and analysing spatial and temporal environmental patterns from heterogeneous geospatial observations.

The system investigates the use of JEPA-based representation learning to predict latent representations of spatial or temporal targets from contextual observations.

Unlike conventional pixel-reconstruction approaches, the proposed learning framework focuses on predictive consistency in representation space.

## 3.2 Primary Objectives

The system shall:

1. Acquire satellite observations through the Bhoonidhi data-access interface.
2. Ingest existing environmental and geospatial datasets.
3. Validate and preprocess heterogeneous spatial and temporal data.
4. Construct aligned multimodal training datasets.
5. Develop a JEPA-based representation learning architecture.
6. Evaluate learned representations through downstream geospatial tasks.
7. Provide interpretable evidence for compatible model predictions.
8. Expose analytical outputs through a GIS-oriented dashboard.

## 3.3 Project Scope

**In scope**

- Satellite data discovery and acquisition.
- Geospatial data engineering.
- Spatial and temporal harmonisation.
- Multimodal dataset construction.
- Self-supervised JEPA implementation.
- Downstream model evaluation.
- Explainability.
- GIS-based visualisation.
- Reproducible experimentation.

**Out of scope for the initial release**

- Autonomous regulatory or government decision-making.
- Unverified agricultural recommendations.
- Operational disaster-warning guarantees.
- Nationwide real-time environmental surveillance.
- A general-purpose Earth foundation model trained at planetary scale.
- Fully autonomous infrastructure approval or land-use decisions.

---

<a id="system-overview"></a>
# 4. System Overview

## 4.1 Operational Concept

GeoSentinel follows a modular data-to-intelligence workflow.

```text
EARTH OBSERVATION SOURCES
          |
          v
DATA ACQUISITION AND INGESTION
          |
          v
DATA VALIDATION AND QUALITY CONTROL
          |
          v
SPATIAL AND TEMPORAL PREPROCESSING
          |
          v
MULTIMODAL DATASET CONSTRUCTION
          |
          v
JEPA REPRESENTATION LEARNING
          |
          v
DOWNSTREAM GEOSPATIAL ANALYSIS
          |
          v
MODEL EVALUATION AND EXPLAINABILITY
          |
          v
GIS VISUALISATION AND DECISION SUPPORT
```

## 4.2 Operating Environment

The system is designed to operate in two environments:

**Local development environment**

Responsible for data management, preprocessing, application development, testing and repository maintenance.

**Remote training environment**

Google Colab with an NVIDIA T4 GPU, accessed through VS Code, is the intended model-training environment.

---

<a id="system-architecture"></a>
# 5. System Architecture

## 5.1 Architectural Overview

The system shall be divided into the following logical layers.

```text
┌─────────────────────────────────────────────────────────────────────┐
│                       GEOSENTINEL SYSTEM                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 01 — DATA SOURCE AND ACQUISITION                             │
│                                                                     │
│  Bhoonidhi API | Weather Providers | Existing GIS Datasets          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 02 — DATA VALIDATION AND MANAGEMENT                          │
│                                                                     │
│  Inventory | Metadata | Provenance | Quality Control               │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 03 — SPATIOTEMPORAL PREPROCESSING                            │
│                                                                     │
│  Raster | Vector | Tabular | Temporal | Feature Engineering        │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 04 — MULTIMODAL DATASET                                      │
│                                                                     │
│  Spatial Alignment | Temporal Alignment | Modality Masks           │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 05 — JEPA REPRESENTATION LEARNING                            │
│                                                                     │
│  Context Encoder | Target Encoder | Predictor | JEPA Loss           │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 06 — GEOSPATIAL INTELLIGENCE                                 │
│                                                                     │
│  Change Analysis | Classification | Environmental Analysis         │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 07 — EVALUATION AND EXPLAINABILITY                           │
│                                                                     │
│  Baselines | Ablations | Metrics | Feature Attribution             │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 08 — PRESENTATION AND APPLICATION                            │
│                                                                     │
│  GIS Dashboard | Spatial Visualisation | Reports | API              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 5.2 Detailed Data Flow

### A. Earth Observation and Environmental Data

| Data Category | Input Information | Acquisition Interface |
|---|---|---|
| Satellite | SAR and optical observations | Bhoonidhi |
| Meteorological | Rainfall, temperature, humidity, wind | Existing weather providers and datasets |
| Hydrological | Reservoirs, lakes and groundwater | Collected datasets |
| Terrain | Elevation, slope and drainage | Available geospatial datasets |
| Environmental | Air quality and environmental indicators | Collected datasets |
| GIS | Administrative boundaries, rivers, waterbodies and infrastructure | Existing GIS datasets |

Satellite collection availability shall be verified before inclusion in the processing pipeline.

### B. Data Processing

The preprocessing layer shall support:

- Raster validation.
- Vector geometry validation.
- Coordinate reference system transformation.
- Spatial intersection and clipping.
- Temporal standardisation.
- Missing-data assessment.
- Raster quality masking.
- Image registration where required.
- Feature extraction.
- Normalisation.
- Spatial patch generation.

### C. Multimodal Representation Learning

The processed datasets shall be converted into a common spatiotemporal representation suitable for model input.

The system shall retain modality identity, spatial location, observation time and source provenance.

### D. Intelligence and Presentation

The trained representation model shall support downstream geospatial analytical tasks through separately evaluated prediction heads.

---

<a id="system-boundaries"></a>
# 6. System Boundaries

## 6.1 Included Components

- GeoSentinel application and processing code.
- Bhoonidhi integration.
- Dataset registry and preprocessing.
- Weather Intelligence module.
- JEPA model implementation.
- Experiment and checkpoint management.
- Evaluation and explainability.
- Dashboard.

## 6.2 External Dependencies

- Bhoonidhi authentication and API availability.
- Availability of satellite products.
- External weather services.
- Original dataset publishers.
- Google Colab runtime availability.
- External storage for large datasets and checkpoints.

GeoSentinel shall not assume that external services are continuously available.

---

<a id="functional-requirements"></a>
# 7. Functional Requirements

Requirements are assigned unique identifiers to support implementation tracking and verification.

Priority classification:

- **P0:** Essential for the initial research release.
- **P1:** Important supporting capability.
- **P2:** Future extension.

## FR-01 — Data Acquisition

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | The system shall support Bhoonidhi API authentication. | P0 |
| FR-002 | The system shall support authentication token management and refresh. | P0 |
| FR-003 | The system shall search available satellite products using spatial and temporal constraints. | P0 |
| FR-004 | The system shall retrieve product metadata. | P0 |
| FR-005 | The system shall identify online and downloadable products. | P0 |
| FR-006 | The system shall download selected products with controlled retries. | P0 |
| FR-007 | The system shall record acquisition provenance. | P0 |
| FR-008 | The system should support additional data providers through modular interfaces. | P2 |

## FR-02 — Dataset Management

| ID | Requirement | Priority |
|---|---|---|
| FR-009 | The system shall discover files in configured dataset directories. | P0 |
| FR-010 | The system shall generate a dataset inventory. | P0 |
| FR-011 | The system shall identify duplicate files using content hashes. | P0 |
| FR-012 | The system shall inspect supported file formats and schemas. | P0 |
| FR-013 | The system shall record dataset spatial coverage. | P0 |
| FR-014 | The system shall record temporal coverage where applicable. | P0 |
| FR-015 | The system shall preserve original datasets. | P0 |
| FR-016 | The system shall maintain source and processing metadata. | P0 |

## FR-03 — Preprocessing

| ID | Requirement | Priority |
|---|---|---|
| FR-017 | The system shall validate vector geometries. | P0 |
| FR-018 | The system shall harmonise coordinate reference systems. | P0 |
| FR-019 | The system shall support raster metadata inspection. | P0 |
| FR-020 | The system shall standardise temporal fields. | P0 |
| FR-021 | The system shall identify missing and invalid observations. | P0 |
| FR-022 | The system shall support spatial filtering using the study-area boundary. | P0 |
| FR-023 | The system shall generate reproducible preprocessing manifests. | P0 |
| FR-024 | The system should support configurable feature extraction. | P1 |

## FR-04 — Multimodal Dataset Construction

| ID | Requirement | Priority |
|---|---|---|
| FR-025 | The system shall support multiple data modalities. | P0 |
| FR-026 | The system shall maintain spatial and temporal associations. | P0 |
| FR-027 | The system shall identify unavailable modalities. | P0 |
| FR-028 | The system shall support modality masks. | P0 |
| FR-029 | The system shall implement reproducible data splits. | P0 |
| FR-030 | The system shall prevent future observations from leaking into historical training samples. | P0 |
| FR-031 | The system should support configurable spatial and temporal sampling. | P1 |

## FR-05 — JEPA Model

| ID | Requirement | Priority |
|---|---|---|
| FR-032 | The model shall implement a context encoder. | P0 |
| FR-033 | The model shall implement a target encoder. | P0 |
| FR-034 | The target encoder shall support EMA updates. | P0 |
| FR-035 | The model shall implement a predictor network. | P0 |
| FR-036 | The model shall calculate a latent representation prediction loss. | P0 |
| FR-037 | The model shall support spatial or temporal context masking. | P0 |
| FR-038 | The model shall support checkpoint saving and restoration. | P0 |
| FR-039 | The training process shall record experiment configurations and metrics. | P0 |
| FR-040 | The model should support multimodal input fusion. | P1 |

## FR-06 — Evaluation and Explainability

| ID | Requirement | Priority |
|---|---|---|
| FR-041 | The system shall support comparison against baseline models. | P0 |
| FR-042 | The system shall calculate task-appropriate evaluation metrics. | P0 |
| FR-043 | The system shall support modality ablation experiments. | P1 |
| FR-044 | The system should support feature attribution for compatible downstream models. | P1 |
| FR-045 | The system should provide spatial visualisation of model outputs. | P1 |
| FR-046 | The system shall distinguish model confidence from validated accuracy. | P1 |

## FR-07 — Application Interface

| ID | Requirement | Priority |
|---|---|---|
| FR-047 | The system shall provide a dashboard for dataset and model exploration. | P1 |
| FR-048 | The system shall display weather information through the existing module. | P1 |
| FR-049 | The system should support geospatial result visualisation. | P1 |
| FR-050 | The system should support report and data export. | P2 |

---

<a id="non-functional-requirements"></a>
# 8. Non-Functional Requirements

## NFR-01 — Maintainability

- Modular architecture.
- Separation of data, model, application and integration layers.
- Type hints for public interfaces.
- Documented public functions and classes.
- Consistent naming conventions.
- Minimal duplicated logic.

## NFR-02 — Code Quality

| Quality Attribute | Acceptance Criterion |
|---|---|
| Pylint | Score greater than 8.9/10 |
| Unit Testing | Applicable tests pass |
| Regression Testing | Existing completed modules remain functional |
| Formatting | Consistent project formatting |
| Type Checking | Critical type errors resolved |
| Security | No committed credentials |
| Documentation | Public interfaces documented |

## NFR-03 — Reproducibility

- Fixed random seeds where supported.
- Versioned experiment configurations.
- Recorded dataset versions.
- Recorded model parameters.
- Saved checkpoints.
- Documented preprocessing procedures.
- Traceable evaluation results.

## NFR-04 — Reliability

- External API failures shall be handled explicitly.
- Interrupted downloads shall not be treated as successful.
- Training shall support checkpoint recovery.
- Original data shall remain protected.
- Data validation failures shall be recorded.

## NFR-05 — Performance

- Processing shall support configurable batch sizes.
- Training shall support mixed precision where compatible.
- Large raster processing shall avoid unnecessary full-memory loading.
- Data loaders shall support efficient batch preparation.
- Training configurations shall be compatible with the available NVIDIA T4 resources.

No fixed throughput or latency guarantee is established until benchmark testing is performed.

## NFR-06 — Security

- Credentials shall be stored outside source code.
- Environment files containing secrets shall be excluded from Git.
- API tokens shall not appear in application logs.
- External service failures shall not expose credentials.
- Access to downloaded data shall respect provider restrictions.

---

<a id="data-requirements-and-specifications"></a>
# 9. Data Requirements and Specifications

## 9.1 Study Area

The target study area is the expanded Chennai Metropolitan Area, Tamil Nadu, India.

Approximate study-area extent: 5,904 km².

The authoritative expanded-CMA boundary must be validated before spatial clipping, sampling or model training.

## 9.2 Data Categories

| Category | Data Types | Processing Requirements |
|---|---|---|
| Satellite | SAR, optical, elevation products | Raster validation, quality checks, spatial alignment |
| Meteorological | Rainfall, temperature, humidity, wind | Timestamp validation, temporal alignment |
| Hydrological | Reservoir, groundwater, lake observations | Unit validation, time-series processing |
| Terrain | DEM, slope, elevation | Spatial harmonisation, terrain derivation where supported |
| Environmental | Air quality and related indicators | Missing-value and temporal validation |
| GIS | Rivers, roads, boundaries, waterbodies | Geometry validation, CRS harmonisation |
| Agriculture | Soil and vegetation information where available | Spatial and temporal validation |

## 9.3 Data Quality Requirements

Each dataset shall have a corresponding metadata record containing:

- Dataset identifier.
- Original filename.
- Source organisation.
- Acquisition date.
- Observation period.
- Spatial coverage.
- Coordinate reference system.
- File format.
- Data licence.
- Processing history.
- Validation status.

## 9.4 Data Integrity

Original collected data shall remain immutable.

Processed outputs shall be stored separately.

Content hashes shall be used to identify duplicate files without assuming that files with different names are different datasets.

## 9.5 Temporal Integrity

Observed data, forecasts and derived features shall be identified separately.

Forecast values shall not be inserted into historical observation records as if they were measurements.

Training samples shall respect their prediction or representation-learning time constraints.

---

<a id="external-system-interfaces"></a>
# 10. External System Interfaces

## 10.1 Bhoonidhi Interface

**Purpose:** Satellite product discovery and acquisition.

Expected operations:

| Operation | Description |
|---|---|
| Authentication | Obtain access credentials and tokens |
| Product Search | Search satellite collections |
| Spatial Filter | Filter by bounding box or AOI intersection |
| Temporal Filter | Filter by acquisition date |
| Metadata Retrieval | Retrieve product information |
| Availability Check | Determine download eligibility |
| Download | Retrieve selected products |

Base API endpoints documented for the integration:

```text
Authentication:
https://bhoonidhi-api.nrsc.gov.in/auth/token

Data Search:
https://bhoonidhi-api.nrsc.gov.in/data/search

Product Download:
https://bhoonidhi-api.nrsc.gov.in/download
```

The connector shall handle authentication, rate limits, pagination, retry behaviour and provider-side access restrictions.

## 10.2 Weather Interface

Existing providers:

- Open-Meteo.
- IMD public observations and warning feeds.

The WeatherManager shall remain the primary orchestration interface for the weather module.

## 10.3 Storage Interface

The system shall support local storage for:

- Raw data.
- Processed data.
- Weather data.
- Metadata.
- Experiment results.
- Model checkpoints.

Large datasets and checkpoints shall not be committed to the source repository.

---

<a id="jepa-model-specification"></a>
# 11. JEPA Model Specification

## 11.1 Model Objective

GeoSentinel-JEPA shall investigate predictive representation learning for geospatial observations.

The model objective is to predict target representations from contextual representations rather than directly reconstructing all input pixels or features.

## 11.2 Architectural Components

### Context Encoder

Maps contextual input into a latent representation.

\[
z_c = f_{\theta}(x_c)
\]

### Target Encoder

Maps target observations into latent representations.

\[
z_t = f_{\bar{\theta}}(x_t)
\]

### Predictor

Predicts target embeddings using context embeddings and target positional or temporal information.

\[
\hat z_t = g_{\phi}(z_c, p_t)
\]

### JEPA Objective

A representative latent prediction objective is:

\[
\mathcal{L}_{JEPA}
=
\frac{1}{N}
\sum_{i=1}^{N}
\left\|
\hat z_{t,i}-z_{t,i}
\right\|_2^2
\]

The final objective shall specify the chosen normalisation, masking strategy and any additional regularisation.

### Target Encoder Update

The target encoder shall support exponential moving average updates:

\[
\bar{\theta}
\leftarrow
\tau\bar{\theta}+(1-\tau)\theta
\]

Where \(\tau\) is the target-encoder momentum parameter.

## 11.3 Model Development Requirements

- Configurable encoder dimensions.
- Configurable predictor dimensions.
- Configurable spatial and temporal masking.
- Configurable optimisation parameters.
- Checkpoint support.
- Training and validation monitoring.
- Multimodal input handling.
- T4-compatible model configuration.

## 11.4 Downstream Applications

The initial research implementation shall prioritise tasks supported by available data and reference labels.

Potential applications include:

- Spatial change detection.
- Environmental classification.
- Land-cover analysis.
- Flood-related spatial analysis.
- Temporal environmental pattern analysis.

These tasks shall be activated only after their datasets and evaluation labels have been validated.

---

<a id="training-and-experimental-specifications"></a>
# 12. Training and Experimental Specifications

## 12.1 Training Environment

| Attribute | Specification |
|---|---|
| Framework | PyTorch |
| Runtime | Google Colab |
| GPU | NVIDIA T4 |
| Development Interface | VS Code |
| Checkpoint Format | PyTorch state dictionaries |
| Experiment Configuration | YAML |
| Experiment Logging | Structured logs and metrics |

## 12.2 Training Controls

The training system shall support:

- Configurable epochs.
- Configurable batch size.
- Gradient accumulation.
- Learning-rate scheduling.
- Mixed precision.
- Validation intervals.
- Checkpoint recovery.
- Random seed control.
- GPU memory monitoring.

## 12.3 Experimental Evaluation

Experiments shall compare the proposed architecture against appropriate baseline methods.

Potential evaluation metrics:

| Metric | Evaluation Context |
|---|---|
| Precision | Classification |
| Recall | Classification |
| F1-score | Classification |
| AUROC | Classification |
| PR-AUC | Imbalanced classification |
| IoU | Segmentation |
| Dice | Segmentation |
| MAE | Regression |
| RMSE | Regression |
| Cohen's Kappa | Classification agreement |

## 12.4 Research Ablations

The experimental design should investigate:

- Contribution of individual modalities.
- Contribution of spatial context.
- Contribution of temporal context.
- Impact of missing modalities.
- Context and target masking configurations.
- JEPA versus conventional representation learning baselines.

All experimental claims shall be supported by recorded runs.

---

<a id="explainability-and-decision-support"></a>
# 13. Explainability and Decision Support

## 13.1 Explainability Requirements

The system shall support interpretable analysis of downstream predictions.

Potential techniques:

- SHAP.
- Integrated Gradients.
- Feature ablation.
- Embedding analysis.
- Spatial evidence visualisation.
- Confidence and uncertainty analysis.

SHAP and feature-attribution techniques shall be applied to models and interfaces for which their assumptions are appropriate. Attribution outputs shall not automatically be interpreted as causal explanations.

## 13.2 Decision Support

The system may provide evidence-based analytical outputs for environmental and geospatial applications.

Potential decision-support domains:

- Environmental assessment.
- Agricultural analysis.
- Infrastructure suitability.
- Hydrological assessment.
- Disaster-related analysis.
- Land-use monitoring.

Recommendations shall be constrained by validated evidence, uncertainty and relevant domain rules.

---

<a id="application-and-user-interface"></a>
# 14. Application and User Interface

## 14.1 Application Framework

The initial application interface shall use Streamlit.

## 14.2 Application Modules

| Module | Responsibility |
|---|---|
| Dataset Explorer | Dataset inventory and quality |
| Satellite Explorer | Bhoonidhi product metadata and coverage |
| Weather Intelligence | Weather observations and forecasts |
| Study Area | Spatial boundary and GIS visualisation |
| Data Processing | Preprocessing status and reports |
| Model Training | Training configuration and experiment status |
| Model Evaluation | Metrics and baseline comparisons |
| Explainability | Feature and spatial evidence visualisation |

## 14.3 User Outputs

Where implemented and supported, the application shall expose:

- Interactive maps.
- Temporal comparisons.
- Spatial indicators.
- Model evaluation charts.
- Explainability visualisations.
- CSV and PDF reports.

---

<a id="security-and-data-governance"></a>
# 15. Security and Data Governance

## 15.1 Credential Management

All external service credentials shall be loaded from environment variables.

Example:

```env
BHOONIDHI_USER_ID=
BHOONIDHI_PASSWORD=
```

The actual `.env` file shall remain local and excluded from version control.

The `.env.example` file shall contain variable names and placeholders only.

## 15.2 Data Governance

- Preserve original datasets.
- Maintain data-source attribution.
- Respect provider licensing and download conditions.
- Record processing provenance.
- Avoid exposing restricted datasets.
- Keep credentials and tokens out of logs and Git history.

---

<a id="technology-stack"></a>
# 16. Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Deep Learning | PyTorch |
| Representation Learning | JEPA |
| Data Processing | NumPy, Pandas |
| Geospatial Processing | GeoPandas, Shapely, PyProj |
| Raster Processing | Rasterio, Xarray |
| Satellite Acquisition | Bhoonidhi API |
| Weather | Open-Meteo, IMD public interfaces |
| Visualisation | Plotly, Matplotlib, Folium |
| Dashboard | Streamlit |
| Explainability | SHAP, Captum |
| Experimentation | Google Colab NVIDIA T4 |
| Development | VS Code |
| Testing | Pytest |
| Static Analysis | Pylint |
| Version Control | Git, GitHub |

---

<a id="software-architecture-and-repository-structure"></a>
# 17. Software Architecture and Repository Structure

The following is the target logical structure. Existing modules shall be reused and extended wherever appropriate.

```text
GeoSentinel/
│
├── README.md
├── .env.example
├── .gitignore
├── config.yaml
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
├── notebooks/
├── experiments/
│   ├── configs/
│   ├── logs/
│   ├── metrics/
│   ├── checkpoints/
│   └── figures/
│
├── reports/
└── docs/
    ├── architecture.md
    ├── methodology.md
    └── data_dictionary.md
```

---

<a id="verification-and-validation"></a>
# 18. Verification and Validation

## 18.1 Software Verification

Each implemented module shall have appropriate unit and integration tests.

Required checks include:

- Bhoonidhi authentication and error handling.
- Dataset discovery and inventory.
- Geometry and CRS validation.
- Temporal data validation.
- Preprocessing correctness.
- JEPA forward pass.
- Target encoder EMA updates.
- Loss calculation.
- Checkpoint saving and restoration.
- Dashboard integration.

## 18.2 Model Validation

Model validation shall include:

- Training and validation loss monitoring.
- Appropriate downstream evaluation.
- Baseline comparisons.
- Ablation studies.
- Spatial and temporal leakage checks.
- Reproducibility checks.

## 18.3 Acceptance Criteria

| ID | Acceptance Criterion |
|---|---|
| AC-001 | Bhoonidhi connector handles authentication and API errors correctly. |
| AC-002 | Dataset inventory is generated from available source files. |
| AC-003 | Original datasets remain unmodified. |
| AC-004 | Preprocessing produces validated, traceable outputs. |
| AC-005 | Multimodal samples preserve spatial and temporal associations. |
| AC-006 | JEPA components pass their unit tests. |
| AC-007 | Training can save and resume checkpoints. |
| AC-008 | Evaluation metrics are generated from actual model predictions. |
| AC-009 | The application displays verified outputs. |
| AC-010 | Pylint score exceeds 8.9/10 on the designated project source. |

---

<a id="deployment-and-execution-environment"></a>
# 19. Deployment and Execution Environment

## 19.1 Local Setup

```bash
git clone https://github.com/gokul2736/Mini-Project.git

cd Mini-Project

python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local environment file from the template and configure the required credentials.

## 19.2 Application Execution

```bash
streamlit run src/geosentinel/dashboard/app.py
```

## 19.3 Testing

```bash
python -m pytest tests/ -q
```

## 19.4 Static Analysis

```bash
python -m pylint src/geosentinel --score=y
```

## 19.5 Model Training

Model training shall be executed through the configured Google Colab runtime using VS Code.

Training configurations, checkpoints and experiment logs shall be stored separately from source code.

---

<a id="implementation-status"></a>
# 20. Implementation Status

The following table distinguishes completed components from planned capabilities.

| Component | Status |
|---|---|
| Initial dataset collection | Completed |
| Weather schema | Completed |
| Open-Meteo adapter | Implemented |
| IMD adapter | Implemented |
| Weather storage | Implemented |
| Weather manager | Implemented |
| Weather dashboard | Implemented |
| Weather offline tests | 43 previously reported passing |
| Bhoonidhi API integration | Pending verification and implementation |
| Dataset inventory and quality pipeline | Next development phase |
| Expanded CMA boundary validation | Pending verification |
| Multimodal dataset construction | Planned |
| GeoSentinel-JEPA | Research implementation pending |
| T4 training experiments | Pending |
| Baseline and ablation studies | Pending |
| Explainability integration | Pending |
| Final dashboard integration | In progress/planned |

Implementation status shall be updated as modules are developed and verified.

---

<a id="future-system-extensions"></a>
# 21. Future System Extensions

The following capabilities are outside the initial implementation scope and are retained as future research directions.

## 21.1 Advanced Geospatial Intelligence

- Multi-task geospatial learning.
- Land suitability assessment.
- Crop and vegetation analysis.
- Infrastructure suitability.
- Urban growth analysis.
- Forest monitoring.
- Waterbody monitoring.
- Carbon-related environmental analysis.
- Climate trend assessment.

## 21.2 Natural Language Geospatial Interface

A future version may integrate:

- Large Language Models.
- Earth Knowledge Graph.
- Natural-language spatial queries.
- Evidence-grounded geospatial recommendations.
- GeoSentinel AI Assistant.

Example queries:

```text
How has this region changed since 2018?

Which environmental factors are associated
with groundwater decline?

What are the land characteristics of this location?

What evidence supports this environmental
risk assessment?
```

---

<a id="research-references"></a>
# 22. Research References

The research implementation shall be grounded in established work on self-supervised learning, JEPA and geospatial representation learning.

Initial reference:

1. Assran, M. et al. (2023). *Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture*. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

   https://arxiv.org/abs/2301.08243

Additional references on multimodal learning, remote sensing, geospatial representation learning and explainability shall be added after literature verification.

---

# Project Repository

**GitHub:** https://github.com/gokul2736/Mini-Project

---

<p align="center">
  <strong>GeoSentinel</strong><br>
  Multimodal Earth Observation • Predictive Representation Learning • Explainable Geospatial Intelligence
</p>
