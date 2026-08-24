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
