# 🔄 Data Standardisation Using OMOP CDM

## Harmonising Longitudinal Population Health Data for Interoperable Research

This study focuses on the **standardisation, harmonisation, and integration of longitudinal population-health data using the Observational Medical Outcomes Partnership Common Data Model (OMOP CDM)** and the **Observational Health Data Sciences and Informatics (OHDSI)** ecosystem.

The work builds on experience with African longitudinal population studies, Health and Demographic Surveillance Systems (HDSS), HIV/population-health datasets, and heterogeneous research data sources.

The central objective is to transform source-specific population-health data into a **standardised, interoperable, well-documented, and research-ready data environment**, while maintaining appropriate privacy, provenance, and data-governance practices.

---

## 📌 Overview

Population-health and longitudinal datasets are frequently collected using different:

- Data structures
- Variable definitions
- Coding systems
- Terminologies
- Date formats
- Geographic classifications
- Demographic representations
- Identifiers
- Metadata standards

These differences create substantial challenges for **data integration, cross-site comparison, reproducible research, and large-scale observational analysis**.

The OMOP CDM provides a common relational structure and standard vocabulary framework that can be used to harmonise heterogeneous observational data.

This project explores how OMOP CDM can be extended beyond conventional electronic health-record environments to support **longitudinal population-health and HDSS data**.

The work is closely aligned with the INSPIRE datahub approach, which demonstrates the use of OHDSI tools and OMOP CDM to harmonise longitudinal population-health data from African research settings.

---

# 🎯 Objectives

The primary objectives are to:

1. **Profile heterogeneous population-health datasets**
2. **Standardise source data structures and formats**
3. **Map source variables to OMOP CDM fields**
4. **Map source terminology to standard OMOP concepts**
5. **Develop reproducible ETL pipelines**
6. **Transform longitudinal population data into OMOP CDM**
7. **Apply data-quality assessment**
8. **Capture data provenance and metadata**
9. **Support interoperable observational research**
10. **Provide a foundation for downstream record linkage and population-health analytics**

---

# 🔬 Research Background

This work is informed by three complementary contributions.

### 1. INSPIRE Datahub

The INSPIRE datahub demonstrates a pan-African architecture for harmonising longitudinal population-health data using **OHDSI tools and OMOP CDM**.

The approach incorporates:

- Data profiling
- Source-to-standard mapping
- ETL
- Vocabulary harmonisation
- Metadata
- Provenance
- Data-quality assessment
- FAIR data principles
- Privacy-aware/federated approaches

The study demonstrates the application of OMOP CDM to longitudinal population data, including HDSS data, rather than limiting the model to conventional clinical/EHR datasets.

**Reference:**

Bhattacharjee T, Kiwuwa-Muyingo S, Kanjala C, Maoyi ML, Amadi D, Ochola M, Kadengye D, Gregory A, Kiragga A, Taylor A, Greenfield J, Slaymaker E, Todd J and INSPIRE Network (2024) INSPIRE datahub: a pan-African integrated suite of services for harmonising longitudinal population health data using OHDSI tools. Front. Digit. Health 6:1329630. doi: 10.3389/fdgth.2024.1329630

---

### 2. African Population Health Data and OMOP

The INSPIRE population-health work demonstrates how OMOP CDM and OHDSI tools can support data sharing and utilisation across African population-health settings.

The approach addresses the challenge of harmonising data across different localities while respecting data ownership and governance requirements.

The work highlights the value of OMOP CDM as a common framework for:

- Data harmonisation
- Data sharing
- Federated research
- FAIR data management
- Cross-site analysis
- Population-health research



**Reference:**

Kiwuwa-Muyingo S, Todd J, Bhattacharjee T, Taylor A and Greenfield J (2023) Enabling data sharing and utilization for African population health data using OHDSI tools with an OMOP-common data model. Front. Public Health 11:1116682. doi: 10.3389/fpubh.2023.1116682

---

### 3. ALPHA-to-OMOP Mapping

The **ALPHA-to-OMOP Data and Vocabulary Mapping** technical work describes the ETL requirements for bringing HIV/population-health data from the ALPHA Network into an OMOP-based environment.

The work emphasises that OMOP implementation requires both:

- Structural mapping to the OMOP CDM
- Semantic mapping to standard vocabularies

The technical document provides a prototype approach for an OMOP "on-ramp" service and demonstrates source-to-OMOP mapping as a core component of OHDSI-based data sharing.

**Reference:**

Bhattacharjee T, Greenfield J. *ALPHA to OMOP Data and Vocabulary Mapping.* ResearchGate. DOI: 10.13140/RG.2.2.24006.65607.

---

# 🔄 Data Standardisation Workflow

## 1. Data Profiling

The first step is to understand the source dataset before attempting transformation.

Profiling examines:

- Number of records
- Number of variables
- Data types
- Missingness
- Unique values
- Value distributions
- Date ranges
- Categorical values
- Identifier structure
- Duplicate records
- Relationships between variables

Source Dataset<BR>
      │<BR>
      ▼<BR>
Data Profiling<BR>
      │<BR>
      ├── Structure<BR>
      ├── Variables<BR>
      ├── Missingness<BR>
      ├── Values<BR>
      ├── Dates<BR>
      └── Identifiers<BR>
      │<BR>
      ▼<BR>
Data Understanding

The INSPIRE architecture incorporates profiling as an early stage of the data-harmonisation process.

---

# 🧩 2. Source-to-OMOP Mapping

Source variables must be mapped to their corresponding OMOP CDM fields.

Conceptually:
<BR><BR>
Source Variable<BR>
      │<BR>
      ▼<BR>
Source Definition<BR>
      │<BR>
      ▼<BR>
Mapping Specification<BR>
      │<BR>
      ▼<BR>
OMOP CDM Field<BR>
      │<BR>
      ▼<BR>
Standardised Representation<BR>


For example:

| Source Data | OMOP Representation |
|---|---|
| Local person identifier | `person_id` |
| Sex | `gender_concept_id` |
| Date of birth | `birth_datetime` |
| Observation period | `observation_period` |
| Geographic information | Appropriate location representation |
| Clinical/health concept | Appropriate standard OMOP concept |
| Source-specific code | `source_concept_id` / mapped standard concept |

The exact mapping depends on the characteristics of the source dataset and the information available.

---

# 📚 3. Vocabulary Mapping

Structural standardisation alone is not sufficient.

Different datasets may describe the same concept using different:

- Codes
- Labels
- Terminologies
- Abbreviations
- Local classifications

OMOP addresses this through its standardised vocabulary framework.
<BR><BR>
Local Code<BR>
    │<BR>
    ▼<BR>
Source Vocabulary<BR>
    │<BR>
    ▼<BR>
Vocabulary Mapping<BR>
    │<BR>
    ▼<BR>
Standard OMOP Concept<BR>
    │<BR>
    ▼<BR><BR>
OMOP CDM<BR>
<BR>
The ALPHA-to-OMOP work identifies vocabulary mapping as a core component of the ETL process.

The INSPIRE work also demonstrates source-to-OMOP vocabulary mapping for population-health data.

---

# 🛠️ 4. OHDSI Mapping Tools

The workflow can use tools from the OHDSI ecosystem to support different stages of standardisation.

### WhiteRabbit

Used for **source-data profiling** and understanding the structure and contents of source datasets.

### Rabbit-in-a-Hat

Used to develop and document **source-to-OMOP ETL specifications and mappings**.

### USAGI

Used to support **terminology and vocabulary mapping** between source concepts and standard OMOP concepts.

### ATHENA

Provides access to the OHDSI vocabulary ecosystem and standard concept information.

# 🔧 5. ETL — Extract, Transform, Load

The ETL process is the core technical mechanism for moving source data into the OMOP CDM.

## Extract

Data are obtained from the source system and placed into a controlled staging environment.

Potential source formats include:

- CSV
- Relational databases
- Research databases
- Longitudinal population datasets
- HDSS datasets

The INSPIRE case study describes extracting INDEPTH core microdata and loading it into PostgreSQL for staging and validation.

---

## Transform

Transformation includes:

- Data cleaning
- Date standardisation
- Code harmonisation
- Vocabulary mapping
- Identifier transformation
- Anonymisation/pseudonymisation
- Structural transformation
- Source-to-OMOP mapping

The INSPIRE implementation used Pentaho Data Integration for transformation and ETL activities in its case study.

---

## Load

The transformed data are loaded into an OMOP CDM database.

# 🗃️ OMOP CDM Structure

OMOP CDM uses a standardised relational structure for observational health data.

A simplified conceptual structure is:

                    PERSON
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
   OBSERVATION    CONDITION    PROCEDURE
          │           │           │
          ▼           ▼           ▼
     MEASUREMENT   DRUG       VISIT
                      │
                      ▼
             OBSERVATION PERIOD

Not every OMOP table needs to be populated for every dataset.

The tables populated depend on the information actually available in the source data.

The INSPIRE case study demonstrates this principle: only the OMOP tables supported by the available population-health information were populated.

---

# 🏘️ OMOP for Longitudinal Population Data

Although OMOP CDM has strong roots in observational clinical data, the INSPIRE work demonstrates its applicability to **African longitudinal population studies and HDSS data**.

Population-health datasets can contain information such as:

- Demographics
- Births
- Deaths
- Migration
- Residence
- Household information
- Pregnancy
- HIV-related information
- Survey observations
- Health events
- Longitudinal observations

These datasets can be transformed into an OMOP-oriented structure while retaining the characteristics required for population-health research.

The INSPIRE datahub specifically demonstrates adapting OMOP CDM to longitudinal population studies and incorporating structured metadata and provenance into the data pipeline.

---

# 🔐 Privacy and Anonymisation

Data standardisation must be accompanied by appropriate privacy controls.

The ETL workflow can include:
<BR>
Identifiable Source Data<BR>
          │<BR>
          ▼<BR>
Controlled Environment<BR>
          │<BR>
          ▼<BR>
De-identification /
Pseudonymisation<BR>
          │<BR>
          ▼<BR>
Standardised OMOP Data<BR>
          │<BR>
          ▼<BR>
Controlled Research Access<BR>
<BR>
Participant identifiers should be managed carefully.

Where appropriate, the OMOP `person_id` can be generated as a study-specific or system-specific identifier rather than exposing the original source identifier.

The INSPIRE case study describes the use of sequential identifiers while retaining the original identifier mapping for provenance under appropriate controls.

---

# 🧾 Provenance and Metadata

Standardisation should not result in loss of information about where the data originated.

A robust ETL process should document:

- Source dataset
- Source variable
- Transformation rule
- Mapping rule
- Vocabulary mapping
- ETL version
- Data-quality checks
- Processing date
- Responsible organisation/team
- Data-access restrictions

<BR>
Source Data
    │
    ├── Metadata
    ├── Mapping
    ├── Transformation
    ├── Vocabulary
    └── Provenance
            │
            ▼
        OMOP CDM
            │
            ▼
    Reproducible Research


The INSPIRE datahub explicitly incorporates provenance and metadata through the ETL pipeline and describes an Implementation Guide to document the process in machine- and human-readable form.

---

# 📊 Data Quality Assessment

After ETL, the transformed OMOP database should undergo systematic quality assessment.

The **OHDSI Data Quality Dashboard (DQD)** provides checks across different dimensions of OMOP data quality.

These include checks related to:

- Completeness
- Conformance
- Plausibility
- Table structure
- Field-level validity
- Concept-level validity
- Referential integrity

Conceptually:

                 OMOP CDM
                    │
                    ▼
          Data Quality Dashboard
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Table       Field      Concept
      Checks      Checks      Checks
        │           │           │
        └───────────┼───────────┘
                    ▼
             Quality Report
                    │
                    ▼
             ETL Refinement

The INSPIRE work incorporates OHDSI data-quality assessment to evaluate the transformed datasets and support reliable downstream analysis.

---

# 🌐 FAIR Data Principles

The standardisation approach is closely aligned with the **FAIR principles**:

### 🔎 Findable

Data and metadata should be discoverable through appropriate catalogues and metadata services.

### 🔓 Accessible

Access should be governed appropriately while enabling legitimate research use.

### 🔄 Interoperable

Standard structures and vocabularies allow datasets to work together.

### ♻️ Reusable

Well-documented data, metadata, provenance, and transformations improve research reuse.

                FAIR
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
  Findable   Accessible  Interoperable
                 │
                 ▼
              Reusable

FAIR principles are an important component of the INSPIRE datahub architecture.

---

# 🌍 Federated Data Architecture

For sensitive population-health data, centralising individual-level records may not always be appropriate.

A federated OMOP architecture can allow participating organisations to maintain control of their local data while using a common CDM structure.

                 Central Research Network
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
        Site A         Site B       Site C
        OMOP CDM      OMOP CDM     OMOP CDM
            │            │            │
            ▼            ▼            ▼
       Local Data     Local Data    Local Data
            │            │            │
            └────────────┼────────────┘
                         ▼
                  Aggregated Results

This approach can support collaborative research while allowing participating institutions to maintain control over sensitive individual-level data.

The INSPIRE architecture describes federated OMOP implementations in which partners can retain local control of their data while contributing to distributed analyses.

---

# 🔗 Relationship to Record Linkage

Data standardisation and record linkage are related but distinct processes.

### Data Standardisation

Answers:

> **How should information from different sources be represented consistently?**

### Record Linkage

Answers:

> **Which records from different sources refer to the same individual or entity?**

The two processes can therefore work together:

Source A ──┐
           │
Source B ──┼──► OMOP / Standardisation
           │             │
Source C ──┘             ▼
                   Harmonised Data
                          │
                          ▼
                   Record Linkage
                          │
                          ▼
                Integrated Longitudinal
                       Population
                          │
                          ▼
                 Population Health
                     Research

This distinction is particularly important when developing machine-learning-based record linkage workflows.

---

# 🧪 Reproducibility

A key objective is to make the complete standardisation workflow reproducible.

The research pipeline should preserve:

- Source-data specifications
- Data dictionaries
- Mapping specifications
- Vocabulary mappings
- ETL logic
- Transformation scripts
- Database schemas
- Quality-assessment results
- Provenance metadata
- Documentation

Source Specification
        │
        ▼
Data Profile
        │
        ▼
Mapping Specification
        │
        ▼
Vocabulary Mapping
        │
        ▼
ETL
        │
        ▼
OMOP CDM
        │
        ▼
Quality Assessment
        │
        ▼
Documented Research Dataset

The INSPIRE methodology emphasises documenting ETL provenance and metadata to improve transparency, reproducibility, and reuse.

---

# 🛠️ Technology Stack

| Technology / Tool | Purpose |
|---|---|
| **OMOP CDM** | Common data model for standardised observational data |
| **OHDSI** | Open-source ecosystem supporting OMOP-based research |
| **WhiteRabbit** | Source-data profiling |
| **Rabbit-in-a-Hat** | ETL design and source-to-OMOP mapping |
| **USAGI** | Vocabulary mapping |
| **ATHENA** | OMOP/OHDSI vocabulary repository |
| **Pentaho Data Integration** | ETL and data transformation |
| **PostgreSQL** | Relational database and OMOP implementation |
| **OHDSI Data Quality Dashboard** | OMOP data-quality assessment |
| **ATLAS** | Cohort definition and observational analytics |
| **Python** | Supporting data processing and research workflows |

The specific combination of tools should be adapted to the characteristics, governance requirements, and infrastructure of each participating research site.

---

# 📈 Research Pipeline

The complete methodology can be summarised as:

```text
                 SOURCE DATA
                      │
                      ▼
               DATA PROFILING
                      │
                      ▼
             DATA STANDARDISATION
                      │
                      ▼
              SOURCE MAPPING
                      │
                      ▼
            VOCABULARY MAPPING
                      │
                      ▼
                    ETL
                      │
                      ▼
                OMOP CDM
                      │
                      ▼
             DATA QUALITY CHECK
                      │
                      ▼
          PROVENANCE & METADATA
                      │
                      ▼
          INTEROPERABLE DATASET
                      │
             ┌────────┴────────┐
             ▼                 ▼
       Record Linkage      OHDSI Analytics
             │                 │
             └────────┬────────┘
                      ▼
             POPULATION HEALTH
                 RESEARCH

---

# 📚 Key Concepts

| Concept | Description |
|---|---|
| **OMOP CDM** | Common structure for representing observational health data |
| **OHDSI** | Open-source collaborative ecosystem built around OMOP |
| **ETL** | Extract, Transform, Load process |
| **Data Harmonisation** | Making heterogeneous data comparable |
| **Vocabulary Mapping** | Mapping source codes to standard concepts |
| **Data Profiling** | Systematic assessment of source data |
| **Data Quality** | Assessment of completeness, conformance, and plausibility |
| **Provenance** | Documentation of data origin and transformation |
| **FAIR Data** | Findable, Accessible, Interoperable, Reusable |
| **HDSS** | Health and Demographic Surveillance System |
| **Longitudinal Data** | Data containing observations across time |
| **Record Linkage** | Connecting records belonging to the same entity |
| **Federated Research** | Distributed research across independently controlled datasets |

---

# 🚀 Future Development

Future development of this project includes:

- [ ] Expand OMOP mappings for additional population-health variables
- [ ] Develop reusable source-to-OMOP mapping specifications
- [ ] Extend vocabulary mapping
- [ ] Automate ETL validation
- [ ] Improve provenance documentation
- [ ] Integrate automated data-quality assessment
- [ ] Develop reusable Pentaho ETL components
- [ ] Support additional HDSS datasets
- [ ] Integrate record-linkage workflows
- [ ] Explore privacy-preserving record linkage
- [ ] Support federated OMOP implementations
- [ ] Integrate OMOP CDM with longitudinal population-health analytics
- [ ] Develop reproducible research pipelines
- [ ] Strengthen FAIR metadata and data documentation

---

# 📖 Publications and Technical References

### 1. INSPIRE Datahub

**Bhattacharjee T, Kiwuwa-Muyingo S, Kanjala C, Maoyi ML, Amadi D, Ochola M, Kadengye D, Gregory A, Kiragga A, Taylor A, Greenfield J, Slaymaker E, Todd J, INSPIRE Network.**

*INSPIRE datahub: a pan-African integrated suite of services for harmonising longitudinal population health data using OHDSI tools.*

**Frontiers in Digital Health. 2024;6:1329630.**

DOI: **10.3389/fdgth.2024.1329630**

### 2. African Population Health Data and OMOP

**Kiwuwa-Muyingo S, Todd J, Bhattacharjee T, Taylor A, Greenfield J.**

*Enabling data sharing and utilization for African population health data using OHDSI tools with an OMOP-common data model.*

**Frontiers in Public Health. 2023;11:1116682.**

DOI: **10.3389/fpubh.2023.1116682**

### 3. ALPHA-to-OMOP Data and Vocabulary Mapping

**Bhattacharjee T, Greenfield J.**

*ALPHA to OMOP Data and Vocabulary Mapping.*

DOI: **10.13140/RG.2.2.24006.65607**

# 🌍 Research Vision
The broader research objective is to develop **scalable, interoperable, privacy-aware, and reproducible approaches for transforming heterogeneous population-health data into high-quality research resources**.

Heterogeneous Population Data
             │
             ▼
       Standardisation
             │
             ▼
          OMOP CDM
             │
             ▼
       Data Quality
             │
             ▼
       Interoperability
             │
             ▼
       Record Linkage
             │
             ▼
    Longitudinal Integration
             │
             ▼
      Population Health
          Research

This study aims to contribute to a reproducible and interoperable research infrastructure for **longitudinal population-health data**, building on OMOP CDM, OHDSI, FAIR principles, and experience from African population-health data harmonisation initiatives.
