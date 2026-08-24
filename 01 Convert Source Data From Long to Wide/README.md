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
### Long Format
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
