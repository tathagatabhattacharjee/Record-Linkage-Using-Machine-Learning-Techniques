# Convert Source Data From Long to Wide

This folder contains the data-preparation workflow used to transform the original **Kisesa Health and Demographic Surveillance System (HDSS)** event-history data from **long format** into **wide format**.

This transformation is an important preprocessing step in the **Record Linkage Using Machine Learning Techniques** project. The resulting wide-format dataset provides a consolidated representation of each study participant's movement and residency history and is subsequently used as the basis for synthetic-data generation.

## Background

The original Kisesa HDSS source data is maintained in an **event-history / longitudinal format**, where individual events or movements are represented across multiple rows.

For example, a participant may have multiple records representing:

- Entry into the HDSS area
- Residence within the HDSS area
- Movement between locations
- Exit from the HDSS area
- Subsequent re-entry
- Other longitudinal events

Although the long format is useful for recording event histories, it is not always convenient for retrospective record-linkage and synthetic-data generation.

This workflow therefore converts the longitudinal event records into a **single consolidated row per participant**.

## Purpose of the Transformation

The primary objectives are to:

1. Read the original Kisesa HDSS event-history data.
2. Identify the records belonging to each study participant.
3. Organise the participant's longitudinal movement history.
4. Consolidate multiple event records into a single participant-level record.
5. Represent the participant's residency/movement history in a wide format.
6. Produce a structured dataset suitable for subsequent synthetic-data generation.
7. Provide a consistent data structure for retrospective record-linkage experiments.

## Long Format vs Wide Format

### Long Format

In the original event-history representation, a participant can appear on multiple rows.

```text
Participant ID | Event | Location | Start Date | End Date
---------------|-------|----------|------------|----------
10001          | Entry | Area A   | 2001-01-01 | 2003-05-10
10001          | Move  | Area B   | 2003-05-11 | 2007-08-20
10001          | Exit  | Area C   | 2007-08-21 | 2010-02-15
```
The participant is therefore represented by several records.
### Wide Format
The transformation consolidates the participant's information into a single row.
```text
Participant ID | Entry 1 | Exit 1 | Entry 2 | Exit 2 | Entry 3 | Exit 3
---------------|----------|--------|----------|--------|----------|-------
10001          | ...      | ...    | ...      | ...    | ...      | ...
```
The exact fields depend on the source data and transformation logic.
<BR>
This representation makes it easier to analyse the complete movement history of an individual as a single observation.
### Source Data
The transformation was developed around the Kisesa HDSS data used in the original PIRL-related record-linkage work.
<BR><BR>
The Pentaho transformation documentation identifies the source as the longitudinal Kisesa HDSS data and describes the transformation as converting the data from long format into wide format.
<BR><BR>
Important: The actual source dataset is not included in this repository. Users must have the appropriate authorised source-data access and permissions before attempting to reproduce the workflow.

### Pentaho Data Integration
The conversion is implemented using Pentaho Data Integration (PDI), also known as Kettle.
<BR>
The main transformation is:
```text
Data Preparation Longitudinal 1.ktr
```
The transformation reads the longitudinal source data and restructures it into a participant-level wide representation.
<BR><BR>
### Transformation Files
| File                                                                                         | Description                                                                                |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`Data Preparation Longitudinal 1.ktr`](./Data%20Preparation%20Longitudinal%201.ktr)         | Main Pentaho transformation for converting the longitudinal data from long to wide format. |
| [`Data Preparation Longitudinal 1 v1.ktr`](./Data%20Preparation%20Longitudinal%201%20v1.ktr) | Version 1 of the transformation.                                                           |
| [`Data Preparation Longitudinal 1 v2.ktr`](./Data%20Preparation%20Longitudinal%201%20v2.ktr) | Version 2 of the transformation containing subsequent changes/refinements.                 |
| [`Converting Long to Wide Format.pdf`](./Converting%20Long%20to%20Wide%20Format.pdf)         | Supporting documentation/presentation describing the long-to-wide conversion process.      |

### Transformation Workflow

The overall process can be represented as:
```text
Kisesa HDSS Longitudinal Data
              |
              v
       Read Source Data
              |
              v
     Identify Participant
              |
              v
    Order Longitudinal Events
              |
              v
   Consolidate Movement History
              |
              v
       Pivot / Restructure
              |
              v
     Wide Participant Dataset
              |
              v
   Synthetic Data Generation
              |
              v
    Record Linkage Experiments
```
### Why Convert to Wide Format?
The conversion is particularly useful for the subsequent synthetic-data generation stage.

A participant-level wide dataset provides a structured representation in which:

- Each participant can be represented by one row.
- Multiple residency episodes can be represented as separate columns.
- Longitudinal characteristics can be retained within the participant record.
- Participant-level attributes can be combined with movement history.
- Synthetic-data generation can be performed on a consistent tabular structure.
- Retrospective record-linkage experiments can use the complete participant history.

### Relationship to PIRL
The original data and methodology are associated with the Point-of-contact Interactive Record Linkage (PIRL) project and the use of Kisesa HDSS data for record-linkage research.

The original event-history representation was designed to support record linkage using a probabilistic approach followed by prospective confirmation.

The current project uses the transformed wide representation as a foundation for a retrospective record-linkage workflow and for generating synthetic datasets suitable for machine-learning experiments.

For background on the original PIRL software and methodology, see: https://github.com/LSHTM-ALPHAnetwork/PIRL_RecordLinkageSoftware

### Database Configuration

In this Project, the Pentaho transformation is configured to work with a PostgreSQL database.

The transformation metadata contains a PostgreSQL connection configuration for the development environment.

Before running the transformation, users should review and configure:

- Database server
- Database name
- Port
- Username
- Password
- Source schema
- Source table
- Output destination

### Security

The .ktr file contains credentials from a local/development environment, replace them with environment-specific configuration or Pentaho parameters before sharing the transformation.

The repository should contain only non-sensitive configuration.

### Prerequisites

To reproduce the transformation, the following are recommended:

- Pentaho Data Integration (PDI / Kettle)
- PostgreSQL
- Access to the authorised HDSS source data
- Appropriate database permissions
- Sufficient storage for the transformed dataset

The exact PDI version should be recorded when conducting reproducible research because transformation behaviour and database connectivity can vary between versions.

## Running the Transformation

### 1. Install Pentaho Data Integration
Install Pentaho Data Integration / Kettle on the system where the transformation will be executed.

### 2. Configure the Database
Configure the PostgreSQL connection to point to the authorised source database.

Do not use credentials committed to the repository.

### 3. Open the Transformation
Open the following transformation file using using Pentaho Data Integration.
```text
Data Preparation Longitudinal 1.ktr
```


### 4. Review the Transformation
Before execution, verify:

- Input database connection
- Input table
- Required fields
- Participant identifier
- Event/movement fields
- Date fields
- Output structure
- Database permissions

### 5. Execute the Transformation

Run the transformation through Pentaho Data Integration and monitor the execution log for:

- Input records
- Output records
- Rejected records
- Errors
- Processing time

### 6. Validate the Output

The output should be checked to ensure that:

- Each participant is represented correctly.
- Multiple longitudinal events have been consolidated.
- Dates remain consistent.
- Movement sequences are preserved.
- No unexpected records have been lost.
- No unintended duplicate participant records have been introduced.


### Data Quality Checks

After conversion, the resulting wide dataset should be validated before being used for synthetic-data generation.

Recommended checks include:

### Record Counts

Compare the number of unique participants in source vs. number of participant records in wide dataset

### Participant Uniqueness
Verify that the participant identifier is unique in the wide dataset.
COUNT(DISTINCT participant_id) = COUNT(*) 

### Date Consistency

Check that:

- Start dates precede end dates.
- Movement episodes are chronologically ordered.
- Missing dates are handled consistently.
- Impossible dates are identified.
