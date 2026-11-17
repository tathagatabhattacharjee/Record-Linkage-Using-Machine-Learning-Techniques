# Machine Learning Framework for Privacy-Preserving Record Linkage in African Population Health Surveillance

Official open-source repository containing code, synthetic data generation pipelines, error-injection frameworks, and machine learning models for the PhD thesis: **"Using Machine Learning Techniques for Record Linkage of Data from Health and Demographic Surveillance Systems and Health Facilities to Improve Health Monitoring in Africa"** (London School of Hygiene & Tropical Medicine, University of London, September 2026).

---

## 1. Executive Summary & Scientific Rationale

In many Low- and Middle-Income Countries (LMICs), routine health information systems (HIS) and civil registration and vital statistics (CRVS) lack universal unique personal identifiers (UPIs). Consequently, individual patient care records in health facilities remain isolated from population-based registries. This fragmentation presents a critical barrier to public health evaluation:
- **Clinic-based records** (e.g., HIV Care and Treatment Centres [CTC]) describe clinical encounters for patients attending care, but cannot establish population denominators required to measure true coverage, loss to follow-up, or regional disease burden.
- **Health and Demographic Surveillance Systems (HDSS)** continuously monitor defined populations (tracking births, deaths, and migrations over decades), but lack clinical encounter records.

Connecting these systems requires **retrospective entity resolution (record linkage)**. However, personal identifiers in routine health records—such as personal names, dates of birth, sex, and residential locations—are frequently affected by typographical errors, missingness, phonetic variations, and demographic mobility.

This repository provides an end-to-end, privacy-preserving, and reproducible computational framework for machine learning-based record linkage between HDSS population surveillance registries and health facility datasets in resource-constrained environments.

### Key Methodological Innovations

1. **Interoperable Data Harmonisation**: Standardisation of heterogeneous longitudinal surveillance microdata (INDEPTH/ALPHA Network specifications) into the Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM v5.4).
2. **Generative Privacy Preservation**: A Conditional Tabular Generative Adversarial Network (CTGAN) pipeline to synthesize multi-table longitudinal demographic surveillance records, coupled with sex-aware deterministic name masking to protect patient privacy while preserving linkage semantics.
3. **Controlled Noise Injection Framework**: An experimental benchmark evaluating entity resolution under four progressive data quality degradation tiers (*Light*, *Moderate*, *Substantial*, and *Heavy* noise).
4. **Dual Modeling Paradigms**:
   - **Unsupervised Entity Resolution**: Expectation–Conditional Maximisation (ECM) algorithm estimating latent match probabilities within the Fellegi–Sunter probabilistic framework.
   - **Supervised Pairwise Classification**: Evaluation of 17 engineered comparison features across Regularised Logistic Regression (RLR), Random Forest (RF), and Constrained Extreme Gradient Boosting (XGBoost) with monotonic constraints, operating on ~40 million candidate pairs.
5. **Explainable AI (XAI)**: Integration of global and local SHAP (SHapley Additive exPlanations) attribution to decompose matching logic into interpretable feature contributions.
6. **Class-Imbalance Evaluation**: Comprehensive benchmarking demonstrating the critical divergence between Receiver Operating Characteristic (ROC-AUC) and Precision–Recall (PR-AUC) metrics in sparse entity resolution settings.

---

## 2. System Architecture & Computational Pipeline

The complete entity resolution workflow is organized into eight sequential processing stages:

```
[Raw HDSS & Clinic Data] 
          │
          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 1: Extraction & Preprocessing                     │
│ - SQL Person-Level Extraction (SELECT DISTINCT ON)      │
│ - Standardisation to ALPHA/iSHARE Specifications        │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 2: OMOP CDM v5.4 Harmonisation                    │
│ - OHDSI ETL Pipeline (Pentaho Data Integration)         │
│ - Mapping to PERSON, LOCATION, OBSERVATION, EPISODE     │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 3: Generative Synthetic Data & Name Masking       │
│ - CTGAN Architecture for Longitudinal Episode Modeling  │
│ - Sex-Preserving Deterministic Name Replacement         │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 4: Clinic Cohort & Controlled Noise Injection     │
│ - Sampling Adult Clinic Visits (Ages 18–60)             │
│ - Injecting Bernoulli Error Tiers (Light -> Heavy)       │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 5: Candidate Blocking & Feature Engineering       │
│ - Deterministic Blocking on Village Name (~40M Pairs)   │
│ - 17 Comparison Features (Levenshtein, Jaro-Winkler, DoB)│
└─────────────────────────┬───────────────────────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│ Stage 6A: Unsupervised RL     │ │ Stage 6B: Supervised ML       │
│ - Fellegi-Sunter + ECM        │ │ - 80:20 Train/Test Partition  │
│ - Jaro-Winkler & Gaussian Prob│ │ - RLR, Random Forest, XGBoost │
└───────────────┬───────────────┘ └───────────────┬───────────────┘
                │                                 │
                └─────────────────┬───────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 7: Model Interpretability & Explainable AI (XAI)  │
│ - SHAP TreeExplainer & LinearExplainer Attribution      │
│ - Local Waterfall Decision Logic Decomposition          │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Stage 8: Evaluation & Epidemiological Inference         │
│ - Confusion Matrices, Precision, Recall, F1-Score       │
│ - ROC-AUC vs PR-AUC Trade-off Analysis                  │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Methodological Details

### 3.1 OMOP Common Data Model (v5.4) Transformation
Source demographic surveillance data from the Kisesa HDSS (Magu District, Mwanza Region, Tanzania) and health facility HIV Care and Treatment Centre (CTC) records were transformed using the OHDSI open-science suite (WhiteRabbit, Rabbit-in-a-Hat, Usagi, and Pentaho Data Integration). 
- Person-level demographics mapped to `PERSON` and `LOCATION`.
- Longitudinal residency episodes, migration events, and clinical encounters mapped to `OBSERVATION`, `VISIT_OCCURRENCE`, `EPISODE`, and `EPISODE_EVENT`.
- Structural integrity validated via OHDSI Data Quality Dashboard (DQD) achieving a >98% pass rate across plausibility, conformance, and completeness checks.

### 3.2 Generative Synthetic Population & Name Masking
To enable privacy-preserving model development without exposing identifiable patient records:
- **CTGAN Generator**: Trained on 107,970 cleaned surveillance episodes representing 81,885 unique individuals. Replicated joint probability distributions, person-time distributions, and age-specific mortality rates (validated via Kolmogorov-Smirnov tests and Wasserstein distance).
- **Sex-Aware Masking**: Replaced personal names deterministically using curated Tanzanian name dictionaries while preserving sex-specific naming conventions and longitudinal consistency across repeated observations.

### 3.3 Experimental Noise Injection Framework
Synthetic clinic datasets were subjected to field-level Bernoulli error injection across five controlled experimental tiers:
1. **Baseline**: Error-free matching reference.
2. **Light Noise**: Typographical character transpositions and minor date shifts.
3. **Moderate Noise**: Character insertions/deletions, 1-month/1-year date errors, subvillage spelling variations.
4. **Substantial Noise**: Name swapping (first/last name transposition), multi-character edits, broader date shifts.
5. **Heavy Noise**: Truncations, severe string corruption, inverted sex categories, missing values (`NULL` fields).

### 3.4 Feature Engineering & Pairwise Vector Space
Candidate record pairs were generated by blocking on standardised village names, producing a fixed comparison space of **39,950,677 candidate pairs** in each noise scenario (linking 81,885 HDSS records with 3,046 clinic records). Each pair was transformed into a 17-dimensional engineered feature vector:
- **Exact Agreement Flags**: Binary indicators for first name, last name, date of birth, sex, village name, and subvillage.
- **Initial Matching Flags**: Binary indicators for first-name and last-name initials.
- **String Distance Metrics**: Levenshtein edit distance and Levenshtein similarity ratios for first name, last name, village name, and subvillage.
- **Phonetic String Metrics**: Jaro-Winkler similarity coefficients.
- **Temporal Metrics**: Absolute date-of-birth difference in days (`dob_diff_days`) and Gaussian similarity.
- **Interaction Terms**: Cross-field name/location consensus and age-difference penalties.

### 3.5 Machine Learning Paradigms
- **Unsupervised Fellegi–Sunter (ECM)**: Iteratively estimates field-specific *m*-probabilities (agreement given true match) and *u*-probabilities (agreement by chance) via Expectation-Conditional Maximisation, assigning posterior match probabilities resolved via a 1:1 post-hoc assignment rule.
- **Regularised Logistic Regression (RLR)**: Linear baseline with L2 (Ridge) penalty and feature standardization.
- **Random Forest (RF)**: Ensemble of 300 decision trees trained with balanced bootstrap subsampling to handle extreme class imbalance.
- **Constrained XGBoost**: Sequential gradient-boosted ensemble of 1,000 shallow decision trees (depth = 4) incorporating domain-informed monotonic constraints enforcing non-decreasing match probability with increasing identifier similarity.

---

## 4. Benchmark Results & Key Findings

### 4.1 Supervised Model Performance Across Degradation Tiers

Evaluated against the ground-truth golden dataset (2,496 true matches among ~40M candidate pairs), the supervised models exhibited distinct operational trade-offs as data quality deteriorated:

| Classifier | Noise Tier | True Positives (TP) | False Positives (FP) | False Negatives (FN) | Precision | Recall | F1-Score | PR-AUC |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Constrained XGBoost** | **Baseline** | 2,496 | 127 | 0 | 0.9516 | 1.0000 | **0.9752** | **1.0000** |
| | **Light** | 2,068 | 107 | 428 | 0.9508 | 0.8285 | **0.8855** | **1.0000** |
| | **Moderate** | 1,780 | 98 | 716 | 0.9478 | 0.7131 | **0.8139** | **0.9999** |
| | **Substantial** | 1,549 | 79 | 947 | 0.9515 | 0.6206 | **0.7512** | **0.9993** |
| | **Heavy** | 1,194 | 64 | 1,302 | 0.9491 | 0.4784 | **0.6361** | **0.9978** |
| **Random Forest** | **Baseline** | 2,496 | 1 | 0 | 0.9996 | 1.0000 | **0.9998** | **0.9998** |
| | **Light** | 1,844 | 1 | 652 | 0.9995 | 0.7388 | 0.8496 | 0.8968 |
| | **Moderate** | 1,437 | 1 | 1,059 | 0.9993 | 0.5757 | 0.7306 | 0.7979 |
| | **Substantial** | 1,172 | 1 | 1,324 | 0.9991 | 0.4696 | 0.6389 | 0.7160 |
| | **Heavy** | 761 | 0 | 1,735 | 1.0000 | 0.3049 | 0.4673 | 0.5859 |
| **Regularised Logistic Regression** | **Baseline** | 2,496 | 8,643 | 0 | 0.2241 | 1.0000 | 0.3661 | 0.5652 |
| | **Light** | 2,466 | 7,420 | 30 | 0.2494 | 0.9880 | 0.3983 | 0.5648 |
| | **Moderate** | 2,351 | 6,106 | 145 | 0.2780 | 0.9419 | 0.4293 | 0.5627 |
| | **Substantial** | 2,207 | 5,518 | 289 | 0.2857 | 0.8842 | 0.4319 | 0.5598 |
| | **Heavy** | 1,916 | 3,655 | 580 | 0.3439 | 0.7676 | 0.4750 | 0.5518 |

### 4.2 Unsupervised Fellegi–Sunter (ECM) Performance

| Noise Tier | True Positives (TP) | False Positives (FP) | False Negatives (FN) | Precision | Recall | F1-Score | PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline** | 2,496 | 550 | 0 | 0.8200 | 1.0000 | 0.9000 | 1.0000 |
| **Light** | 2,347 | 699 | 149 | 0.7700 | 0.9400 | 0.8500 | 0.9200 |
| **Moderate** | 2,242 | 804 | 254 | 0.7400 | 0.9000 | 0.8100 | 0.8700 |
| **Substantial** | 2,146 | 900 | 350 | 0.7000 | 0.8600 | 0.7700 | 0.8200 |
| **Heavy** | 1,868 | 1,178 | 628 | 0.6100 | 0.7500 | 0.6700 | 0.7300 |

### 4.3 Key Methodological Insights

1. **Constrained XGBoost is the Superior Model**: XGBoost maintains an exceptional balance between precision (~0.95) and recall across all noise scenarios, achieving the highest F1-score and preserving PR-AUC > 0.997 even under severe noise.
2. **Random Forest Conservatism & Recall Collapse**: Random Forest provides near-zero false-positive rates (Precision ≈ 1.0000), but its recall collapses from 1.0000 to 0.3049 under heavy noise because corrupted features fail rigid decision-tree split thresholds.
3. **Linear Model Limitation (RLR)**: Regularised Logistic Regression suffers from severe over-prediction of positive matches (Precision = 0.2241 at baseline) because a linear function cannot capture complex non-linear interaction terms among partially corrupted identifiers.
4. **ROC-AUC vs. PR-AUC Divergence**: Due to the immense non-match background (~40M candidate pairs), ROC-AUC values remain misleadingly optimistic (>0.98 across all models and noise levels). Precision–Recall AUC (PR-AUC) provides the true operational measure of matching quality in class-imbalanced entity resolution.

---

## 5. Repository Layout

```
Record-Linkage-Using-Machine-Learning-Techniques/
├── README.md                           <- Repository documentation
├── LICENSE                             <- Open-source license
├── requirements.txt                    <- Python dependency specification
│
├── etl/                                <- Data Extraction & OMOP CDM Migration
│   ├── sql/                            <- SQL extraction queries (SELECT DISTINCT ON)
│   ├── pentaho/                        <- Pentaho Data Integration (Kettle) ETL jobs
│   └── omop_mapping_spec.csv           <- Source-to-target OMOP CDM v5.4 mapping
│
├── synthetic_generation/               <- Generative AI & Privacy Preservation
│   ├── train_ctgan.py                  <- CTGAN model training script
│   ├── generate_synthetic_hdss.py      <- Batch synthetic residency generation
│   ├── deterministic_masking.py        <- Sex-aware Tanzanian name masking
│   └── validate_synthetic_fidelity.py  <- KS-test & Wasserstein distance validation
│
├── noise_injection/                    <- Controlled Error Framework
│   ├── inject_field_noise.py           <- Bernoulli field-wise error simulator
│   └── noise_config.json               <- Probability distributions for noise tiers
│
├── models/                             <- Record Linkage Engines
│   ├── unsupervised_ecm.py             <- Fellegi-Sunter model + ECM algorithm
│   ├── feature_engineering.py          <- 17-feature comparison matrix calculation
│   ├── train_supervised_classifiers.py <- RLR, Random Forest, & XGBoost pipelines
│   └── serialized/                     <- Pickle (.pkl) exported trained models
│
├── xai_shap/                           <- Explainable AI & Model Interpretability
│   ├── shap_global_attribution.py      <- TreeExplainer & LinearExplainer summary plots
│   └── shap_local_waterfall.py         <- Record-pair local decision logic decomposition
│
└── evaluation/                         <- Benchmarking & Performance Metrics
    ├── compute_metrics.py              <- Precision, Recall, F1, ROC-AUC, PR-AUC
    └── generate_figures.py             <- Publication-ready ROC & PR curve plots
```

---

## 6. Quick Start & Reproducibility Guide

### Prerequisites
- Python 3.12+
- PostgreSQL 14+ (for storing OMOP CDM schemas)
- CUDA-capable GPU (recommended for CTGAN training and XGBoost acceleration)

### Step 1: Environment Setup

```bash
git clone tathagatabhattacharjee/Record-Linkage-Using-Machine-Learning-Techniques
cd Record-Linkage-Using-Machine-Learning-Techniques

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Synthetic Data Generation & Masking

```bash
# Train CTGAN on preprocessed residency episodes
python synthetic_generation/train_ctgan.py --epochs 300 --batch_size 500

# Generate synthetic HDSS population and apply deterministic name masking
python synthetic_generation/generate_synthetic_hdss.py --num_records 81885
python synthetic_generation/deterministic_masking.py --input_file data/synthetic_hdss.csv
```

### Step 3: Error Injection & Scenario Versioning

```bash
# Construct synthetic clinic datasets across 4 degradation tiers
python noise_injection/inject_field_noise.py --scenario all
```

### Step 4: Execute Record Linkage Pipelines

```bash
# Run Unsupervised Fellegi-Sunter ECM Probabilistic Matching
python models/unsupervised_ecm.py --scenario heavy

# Train & Evaluate Supervised ML Models (RLR, Random Forest, XGBoost)
python models/train_supervised_classifiers.py --scenario all
```

### Step 5: Generate Explainable AI (SHAP) Visualizations

```bash
# Compute global SHAP feature importance and local waterfall plots
python xai_shap/shap_global_attribution.py --model xgboost
python xai_shap/shap_local_waterfall.py --model xgboost --record_id 0
```

---

## 7. Citation & Academic References

If you use this codebase, synthetic datasets, or methodological framework in your research, please cite the thesis and associated publications:

```bibtex
@phdthesis{bhattacharjee2026recordlinkage,
  author       = {Tathagata Bhattacharjee},
  title        = {Using Machine Learning Techniques for Record Linkage of Data from Health and Demographic Surveillance Systems and Health Facilities to Improve Health Monitoring in Africa},
  school       = {London School of Hygiene \& Tropical Medicine (LSHTM), University of London},
  year         = {2026},
  month        = {September},
  department   = {Department of Population Health, Faculty of Epidemiology and Population Health}
}

@article{bhattacharjee2024inspire,
  title        = {INSPIRE datahub: A pan-African integrated suite of services for harmonising longitudinal population health data using OHDSI tools},
  author       = {Bhattacharjee, Tathagata and Kiwuwa-Muyingo, Sylvia and Kanjala, Chifundo and Maoyi, Mlamli L and Amadi, David and Ochola, Mercy and Kadengye, Felix and Gregory, Alex and Kiragga, Agnes and Taylor, Anna and Greenfield, Jim and Slaymaker, Emma and Todd, Jim and INSPIRE Network},
  journal      = {Frontiers in Digital Health},
  volume       = {6},
  pages        = {1329630},
  year         = {2024},
  doi          = {10.3389/fdgth.2024.1329630}
}

@article{bhattacharjee2026migrating,
  title        = {Migrating longitudinal African mental health data from staging to the OMOP common data model within the INSPIRE network datahub},
  author       = {Bhattacharjee, Tathagata and Mugotitsa, B and Ochola, M and Momanyi, R and Andeso, P and Amadi, D and Mailosi, D and Najjemba, L and Greenfield, J and Mabe, K and Slaymaker, E and Todd, J and Kiragga, A and INSPIRE Network},
  journal      = {Frontiers in Psychiatry},
  volume       = {17},
  pages        = {1751529},
  year         = {2026},
  doi          = {10.3389/fpsyt.2026.1751529}
}
```

---

## 8. Ethical Governance & Acknowledgments

- **Ethics Approval**: Granted by the London School of Hygiene & Tropical Medicine (LSHTM) Observational Research Ethics Committee (Ref: 29794) and the Lake Zone Institutional Review Board (LZIRB / NIMR Mwanza, Tanzania; Ref: MR/53/100/762).
- **Data Governance**: All experiments reported in this repository use non-identifiable synthetic data generated from the Kisesa HDSS and CTC clinic datasets. No real-world patient records are stored or exposed in this codebase.
- **Institutional Affiliations**: Population Studies Group, Department of Population Health, LSHTM; Kisesa HDSS / NIMR Mwanza, Tanzania; ALPHA Network; INDEPTH Network; INSPIRE Network; OHDSI Community.
