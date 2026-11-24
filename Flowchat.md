                  GEOSENTINEL
                       |
         +-------------+-------------+
         |                           |
  EXISTING DATASETS             BHOONIDHI
         |                           |
  Weather Intelligence       Authentication
  Rainfall                    STAC Product Search
  Groundwater                 AOI and Date Filtering
  Flood and Hydrology         Product Availability
  Waterbodies                 Data Download
  Air Quality                       |
  Administrative Data               |
         |                           |
         +-------------+-------------+
                       |
             DATA VALIDATION
                       |
       Format / CRS / Geometry / Time
       Missing Values / Duplicates
       Provenance / Quality Assessment
                       |
             PREPROCESSING
                       |
        Spatial and Temporal Alignment
        Feature Engineering
        Normalisation / Quality Masks
                       |
          MULTIMODAL DATASET
                       |
             DATA PARTITIONING
           Spatial and Temporal Splits
                       |
                JEPA MODEL
                       |
        +--------------+--------------+
        |              |              |
   Context Encoder  Target Encoder  Predictor
        |              |              |
        +--------------+--------------+
                       |
            REPRESENTATION LEARNING
                       |
           DOWNSTREAM EVALUATION
                       |
        Baselines / Ablations / Metrics
                       |
           EXPLAINABILITY ANALYSIS
                       |
             GEOSENTINEL DASHBOARD
                       |
             IEEE RESEARCH PAPER
