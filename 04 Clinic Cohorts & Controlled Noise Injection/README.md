# Synthetic Clinic Cohort Construction & Controlled Noise Injection Engine

A privacy-preserving computational framework for constructing synthetic adult health facility cohorts from longitudinal demographic surveillance systems and simulating controlled field-level error injection across progressive data degradation tiers.

---

## 1. Overview & Epidemiological Design

In resource-constrained public health settings across Sub-Saharan Africa, routine clinical information systems and population-based Health and Demographic Surveillance Systems (HDSS) operate independently without shared, universal personal identifiers. Evaluating the performance, scalability, and robustness of machine learning record linkage algorithms under realistic operational conditions requires benchmark datasets where the underlying ground-truth linkage status is known, while reflecting real-world data quality degradation such as typographical errors, missing attributes, and administrative recording discrepancies.

This module provides a reproducible, end-to-end pipeline designed to:
1. **Extract a Synthetic Adult Clinic Cohort** from a baseline population surveillance database (specifically modeled on the Kisesa HDSS in Magu District, Mwanza Region, Tanzania).
2. **Inject External Non-Surveillance Patient Records** (`pseudo_idlong = NULL`) to simulate real-world facility dynamics where health centers serve individuals residing outside the surveillance catchment area.
3. **Execute Controlled, Field-Wise Probabilistic Noise Injection** across four progressive degradation tiers (*Light*, *Moderate*, *Substantial*, and *Heavy*), systematically introducing realistic corruption into personal names, dates of birth, sex, and sub-village geographic attributes while retaining a fixed, error-free blocking variable (`villagename`).

---

## 2. Cohort Construction & Dual-Population Architecture

The synthetic clinic dataset is derived from a de-identified, CTGAN-generated synthetic population representing 81,885 unique individuals and 108,660 longitudinal residency episodes.

```
+-----------------------------------------------------------------------+
|                 Synthetic Kisesa HDSS Database                        |
|             (81,885 Unique Individuals / 108,660 Episodes)            |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|             Adult Filter: Ages 18–60 at First Visit                   |
|                      (n = 25,461 Eligible Adults)                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|               10% Simple Random Sampling (SRS)                        |
|           n = 2,546 Matched Patients (pseudo_idlong != NULL)          |
+-----------------------------------------------------------------------+
                                   |
                                   +------------------------------------+
                                   |                                    |
                                   v                                    v
+------------------------------------+ +--------------------------------+
|    Matched Baseline Cohort         | |  External Clinic-Only Cohort   |
|   n = 2,546 HDSS Residents         | |  n = 500 Non-HDSS Patients   |
| (pseudo_idlong = Genuine Key)      | |  (pseudo_idlong = NULL)        |
+------------------------------------+ +--------------------------------+
                                   |                                    |
                                   +-----------------+------------------+
                                                     |
                                                     v
+-----------------------------------------------------------------------+
|                    Total Baseline Clinic Dataset                      |
|                  n = 3,046 Patient Registration Records               |
|            (1,318 Males / 1,728 Females; Ages 18–60 Years)            |
+-----------------------------------------------------------------------+
```

### Methodological Workflow & Parameters

1. **Eligibility Filtering**: Individuals aged 18 to 60 years at their first recorded surveillance episode are extracted from the synthetic HDSS database, producing an eligible pool of 25,461 adult residents.
2. **Matched Cohort Sampling**: A 10% simple random sample ($n = 2,546$) is selected to represent HDSS residents accessing outpatient clinical services. Each individual contributes a single clinical registration record containing an alphanumeric patient identifier (`patientid`), hidden longitudinal key (`pseudo_idlong`), masked first and last names, sex, date of birth, village, sub-village, and first visit date.
3. **Unmatched External Population Injection**: To simulate real-world facility encounters where clinics serve populations beyond the surveillance boundaries, 500 synthetic adult patient records are independently generated and merged into the clinic file. Their hidden longitudinal keys are assigned as `pseudo_idlong = NULL`. Names are sampled from sex-classified regional dictionaries to prevent accidental overlap with HDSS residents, while dates and geographic locations are sampled from plausible regional demographic distributions.
4. **Final Baseline Dataset Composition**: The resulting error-free baseline clinic dataset contains $n = 3,046$ unique patient registration records (2,546 true matched records + 500 non-matched external records). Demographically, the cohort comprises 1,318 males (43.3%) and 1,728 females (56.7%), with the highest patient density concentrated in the 18–24 and 25–34 age brackets.

---

## 3. Controlled Field-Level Noise Injection Engine

Following baseline cohort construction, controlled noise is introduced exclusively into the clinic dataset, while the synthetic HDSS reference database remains completely uncorrupted. This isolates the effect of clinic data quality degradation on record linkage performance while preserving exact ground-truth identity keys.

### Fixed Blocking Anchor
To isolate identifier degradation from candidate pair generation, the `villagename` field is pre-cleaned and held error-free across all experimental scenarios. Blocking on `villagename` ensures an identical candidate search space ($N_{	ext{pairs}} = 39,950,677$) across all degradation tiers.

### Probabilistic Injection Mechanism
For each clinic record and each target linkage attribute, an independent Bernoulli trial ($p_{	ext{field\_scenario}}$) determines whether the field is selected for perturbation. If selected ($= 1$), exactly one field-specific error mechanism is applied based on predefined probability distributions:

* **Personal Names (`masked_firstname`, `masked_lastname`)**:
  * *Character Transposition*: Swapping adjacent characters (e.g., `Lugano` $ightarrow$ `Luagno`).
  * *Single-Character Omission*: Deleting a character (e.g., `Bulugu` $ightarrow$ `Bulgu`).
  * *Single-Character Insertion*: Inserting a plausible character (e.g., `Malaika` $ightarrow$ `Malaikah`).
  * *Substitution / Typo*: Replacing a character with an adjacent keyboard or phonetic character (e.g., `Chagula` $ightarrow$ `Chagulla`).
  * *Name Swapping*: Reversing first and last names (e.g., `Subira Chagula` $ightarrow$ `Chagula Subira`).
* **Dates (`dob`, `first_visit_date`)**:
  * *Day Shift*: Perturbing the day value by $\pm 1$ to $\pm 5$ days.
  * *Month Shift*: Perturbing the month value by $\pm 1$ to $\pm 3$ months.
  * *Year Shift*: Perturbing the birth year by $\pm 1$ to $\pm 5$ years.
  * *Logical Constraints*: All perturbed dates are validated to maintain calendar validity and chronological ordering (e.g., birth date preceding visit date).
* **Sex (`sex`)**:
  * *Category Flip*: Recoding `1` (Male) $ightarrow$ `2` (Female) or `2` $ightarrow$ `1` at low scenario-defined rates.
* **Sub-Village (`subvillagename`)**:
  * *Typographical Corruption / Abbreviation*: Dropping prefix modifiers or altering spelling (e.g., `Ng'wabulimi` $ightarrow$ `Ngwabulmi`).
  * *Missingness*: Probabilistic insertion of `NULL` values under heavy degradation.

---

## 4. Graded Degradation Tiers & Benchmark Quantitative Metrics

The noise engine generates four independent, progressively degraded clinic datasets (*Light*, *Moderate*, *Substantial*, and *Heavy*), establishing a quantitative benchmark hierarchy.

| Data Quality Metric | Baseline | Light Noise | Moderate Noise | Substantial Noise | Heavy Noise |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Total Records Compared** | 3,046 | 3,046 | 3,046 | 3,046 | 3,046 |
| **First Name Similarity (Mean Jaro–Winkler)** | 1.000 | 0.938 | 0.864 | 0.806 | 0.709 |
| **Last Name Similarity (Mean Jaro–Winkler)** | 1.000 | 0.933 | 0.865 | 0.798 | 0.707 |
| **Sex Mismatch Count (#)** | 0 | 67 | 143 | 196 | 244 |
| **Sex Mismatch Proportion** | 0.000 | 0.022 | 0.047 | 0.064 | 0.080 |
| **Mean Absolute DOB Difference (Days)** | 0.00 | 31.89 | 100.66 | 198.25 | 414.96 |
| **Mean Absolute Visit-Date Difference (Days)** | 0.00 | 30.18 | 94.17 | 209.24 | 390.19 |
| **Mean Absolute Age Difference (Years)** | 0.000 | 0.168 | 0.516 | 1.097 | 2.017 |
| **Village Similarity (Mean Jaro–Winkler)** | 1.000 | 0.954 | 0.912 | 0.863 | 0.798 |
| **Sub-Village Similarity (Mean Jaro–Winkler)** | 1.000 | 0.957 | 0.906 | 0.871 | 0.786 |
| **Records with $\ge 1$ Field Corruption (#)** | 0 | 1,223 | 1,830 | 2,198 | 2,655 |
| **Overall Record Degradation Rate (%)** | 0.0% | 40.2% | 60.1% | 72.2% | 87.2% |

### Key Degradation Characteristics
* **Light Noise**: Simulates routine clerical errors (40.2% record error rate). Personal name similarity remains high ($\ge 0.933$), and mean DOB discrepancy is small ($pprox 32$ days).
* **Moderate Noise**: Simulates operational data collection inconsistencies (60.1% record error rate). Name similarity drops to $pprox 0.864$, with mean DOB shift reaching $pprox 101$ days.
* **Substantial Noise**: Simulates significant field corruption and missingness (72.2% record error rate). Name similarity drops to $pprox 0.800$, and mean DOB discrepancy reaches $pprox 198$ days.
* **Heavy Noise**: Represents severe data degradation (87.2% record error rate). Nearly 9 out of 10 clinic records contain corrupted fields, name similarity falls to $pprox 0.708$, and DOB discrepancy averages over 414 days ($pprox 1.14$ years).

---

## 5. Sample Record-Level Data Degradation Matrix

The table below illustrates how four representative synthetic patient records (A, B, C, D) evolve across the five scenario tiers while maintaining invariant `patientid` and `pseudo_idlong` keys.

| Scenario | Rec. | patientid | pseudo_idlong | masked_firstname | masked_lastname | sex | dob | villagename | subvillagename |
| :--- | :---: | :--- | :---: | :--- | :--- | :---: | :---: | :--- | :--- |
| **Baseline** | **A** | `58-04-7192-330486` | 41207 | Malaika | Bulugu | 2 | 1979-04-22 | Kisesa | Ng'wabulimi |
| | **B** | `23-11-5048-712903` | 68314 | Lugano | Ng'humbi | 1 | 1968-02-09 | Welamasonga | Mwang'halala |
| | **C** | `09-07-2836-145720` | 15962 | Subira | Chagula | 2 | 1990-12-05 | Kitumba | Ilunda |
| | **D** | `71-05-9364-208517` | 30475 | Emanueli | Mgaya | 1 | 1955-08-27 | Igekemaja | Bugando |
| **Light** | **A** | `58-04-7192-330486` | 41207 | Malaikah | Bulugu | 2 | 1979-04-22 | Kisesa | Ng'wabulimi |
| | **B** | `23-11-5048-712903` | 68314 | Lugano | Ng'humbi | 1 | 1968-02-09 | Welamasonga | Mwang'halala |
| | **C** | `09-07-2836-145720` | 15962 | Subira | Chagula | 2 | 1990-12-05 | Kitumba | Ilunde |
| | **D** | `71-05-9364-208517` | 30475 | Emanueli | Mgaya | 1 | 1955-08-27 | Igekemaja | Bugando |
| **Moderate**| **A** | `58-04-7192-330486` | 41207 | Malaika | Bulugu | 2 | 1979-04-22 | Kisesa | Ng'wabulimi |
| | **B** | `23-11-5048-712903` | 68314 | Lugano | Nghumbi | 1 | 1968-05-09 | Welamasonga | Mwang'halala |
| | **C** | `09-07-2836-145720` | 15962 | Subira | Chagulla | 2 | 1990-12-05 | Kitumba | Ilunda |
| | **D** | `71-05-9364-208517` | 30475 | Emanueli | Mgaya | 1 | 1955-08-27 | Igekemaja | Bugandu |
| **Substantial**| **A** | `58-04-7192-330486` | 41207 | Malaika | Buluga | 2 | 1979-04-22 | Kisesa | Ngwabulmi |
| | **B** | `23-11-5048-712903` | 68314 | Lugano | Ng'humbi | 1 | 1968-02-09 | Welamasonga | Mwang'halala |
| | **C** | `09-07-2836-145720` | 15962 | Chagula | Subira | 2 | 1990-12-05 | Kitumba | Ilunda |
| | **D** | `71-05-9364-208517` | 30475 | Emmanueli | Mgaya | 1 | 1955-03-27 | Igekemaja | Bugando |
| **Heavy** | **A** | `58-04-7192-330486` | 41207 | mlaikha | Bulugu | 1 | 1979-04-22 | Kisesa | *NULL* |
| | **B** | `23-11-5048-712903` | 68314 | Lugano | ngumbi | 1 | 1966-02-09 | Welamasonga | Mwang'halala |
| | **C** | `09-07-2836-145720` | 15962 | Subira | Chagula | 2 | *NULL* | Kitumba | Ilunda |
| | **D** | `71-05-9364-208517` | 30475 | emnuali | Mgaya | 1 | 1955-08-27 | Igekemaja | bugndo |

---

## 6. Repository Layout & Software Architecture

```
clinic-cohort-injection/
├── config/
│   ├── noise_params.json         # Scenario probabilities (Light, Moderate, Substantial, Heavy)
│   └── dictionary_paths.json     # Regional name dictionaries for replacement
├── data/
│   ├── synthetic_hdss_base.parquet
│   ├── baseline_clinic_cohort.csv
│   └── graded_scenarios/
│       ├── clinic_light_noise.csv
│       ├── clinic_moderate_noise.csv
│       ├── clinic_substantial_noise.csv
│       └── clinic_heavy_noise.csv
├── src/
│   ├── cohort_builder.py         # Adult filtering, sampling & 500 external patient injection
│   ├── noise_engine.py           # Probabilistic field-wise corruption functions
│   └── utils_metrics.py          # Data quality calculation (Jaro-Winkler, Levenshtein, shifts)
├── tests/
│   ├── test_cohort_integrity.py  # Validates 3,046 records and pseudo_idlong integrity
│   └── test_noise_gradients.py   # Asserts monotonic degradation across scenarios
├── README.md                     # Module documentation
└── requirements.txt              # Environment dependencies (pandas, numpy, recordlinkage)
```

---

## 7. Execution & Data Processing Workflows

### Step 1: Construct the Baseline Synthetic Clinic Cohort

Run `cohort_builder.py` to sample eligible adult HDSS residents and inject external non-HDSS patient records:

```bash
python src/cohort_builder.py   --input-hdss data/synthetic_hdss_base.parquet   --sample-rate 0.10   --external-patients 500   --min-age 18   --max-age 60   --output-baseline data/baseline_clinic_cohort.csv
```

### Step 2: Generate Graded Data Degradation Scenarios

Execute `noise_engine.py` to generate the four noise tiers according to `config/noise_params.json`:

```bash
python src/noise_engine.py   --input-baseline data/baseline_clinic_cohort.csv   --config config/noise_params.json   --output-dir data/graded_scenarios/
```

### Step 3: Verify Data Quality Metrics & Error Gradients

Calculate dataset-level similarity metrics and verify monotonic degradation across scenarios:

```bash
python src/utils_metrics.py   --baseline data/baseline_clinic_cohort.csv   --scenarios-dir data/graded_scenarios/
```

---

## 8. Data Governance & Ethical Compliance

* **Synthetic Data Privacy**: All patient records and surveillance histories in this module are entirely synthetic, generated using Conditional Tabular GANs (CTGAN) and masked using deterministic name dictionaries. No identifiable personal health information (PHI) or real participant records are stored or processed.
* **Ethical Clearances**: The methodology and ethical framework supporting this research were approved by the London School of Hygiene & Tropical Medicine Observational Research Ethics Committee (LSHTM Ref: `29794` / Amendment Ref: `29794-1`) and the Lake Zone Institutional Review Board at the National Institute for Medical Research (NIMR), Mwanza Centre, Tanzania (Clearance Ref: `MR/53/100/762`).

---

## 9. Preferred Citation

If you utilize this clinic cohort construction pipeline, controlled noise injection framework, or benchmark dataset in your research, please cite:

```bibtex
@phdthesis{Bhattacharjee2026Thesis,
  author       = {Bhattacharjee, Tathagata},
  title        = {Using Machine Learning Techniques for Record Linkage of Data from Health and Demographic Surveillance Systems and Health Facilities to Improve Health Monitoring in Africa},
  school       = {London School of Hygiene \& Tropical Medicine (LSHTM), University of London},
  year         = {2026},
  month        = {September},
  type         = {Doctoral Dissertation},
  address      = {London, UK}
}
```
