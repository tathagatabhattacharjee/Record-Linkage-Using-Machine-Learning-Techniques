# DSWB Training 202502

This folder contains training and supporting material related to **synthetic data generation**, prepared as part of the DSWB training activities in February 2025.

The material provides an introduction to synthetic data, practical guidance for setting up a Python/Jupyter environment, presentation material covering synthetic-data concepts and approaches, and a case-study area for hands-on experimentation.

## Contents

| Resource | Description |
|---|---|
| [`Bootcamp - Synthetic Data Creation.pptx.pdf`](./Bootcamp%20-%20Synthetic%20Data%20Creation.pptx.pdf) | Bootcamp presentation covering synthetic data creation concepts and practical approaches. |
| [`Platform Presentation - Synthetic Data - I.pdf`](./Platform%20Presentation%20-%20Synthetic%20Data%20-%20I.pdf) | Presentation material introducing synthetic data and related concepts. |
| [`Installing Jupyter Notebook.pdf`](./Installing%20Jupyter%20Notebook.pdf) | Installation and setup guide for Jupyter Notebook, used for the practical exercises. |
| [`Case Study`](./Case%20Study/) | Directory containing the case-study material and practical exercises associated with the training. |

## Training Objectives

The training material is intended to provide a practical introduction to synthetic data generation and its application in data science and machine-learning workflows.

Key objectives include:

- Understand the concept of synthetic data.
- Understand why synthetic data can be useful in data-intensive applications.
- Explore different approaches to generating synthetic datasets.
- Understand the difference between real, anonymised, masked, and synthetic data.
- Set up a Python-based environment for synthetic-data experimentation.
- Use Jupyter Notebook for interactive data-science workflows.
- Apply synthetic-data techniques to a practical case study.
- Understand how synthetic datasets can support machine-learning and record-linkage research.

## Synthetic Data

Synthetic data is artificially generated data designed to reproduce selected characteristics, patterns, relationships, or distributions found in real-world data.

Depending on the generation technique, synthetic data can be produced using approaches such as:

- Statistical sampling
- Rule-based generation
- Probabilistic models
- Machine-learning models
- Generative models
- Generative Adversarial Networks (GANs)
- Conditional Tabular GANs (CTGANs)

Synthetic data can be particularly useful when access to real data is restricted because of privacy, confidentiality, security, or data-sharing considerations.

## Synthetic Data in Record Linkage

Within this project, synthetic data is particularly useful for developing and evaluating **record-linkage techniques**.

Record linkage attempts to determine whether records from different datasets refer to the same real-world entity.

Synthetic datasets can provide a controlled environment in which researchers can:

1. Generate realistic records.
2. Introduce controlled variations and errors.
3. Create multiple representations of the same entity.
4. Generate matched and unmatched record pairs.
5. Test similarity measures.
6. Train machine-learning models.
7. Evaluate linkage performance without exposing sensitive source data.

A simplified workflow is:

```text
Source Data
        |
        v
Data Understanding & Preparation
        |
        v
Synthetic Data Generation
        |
        v
Synthetic Dataset
        |
        +----------------------+
        |                      |
        v                      v
Record Variations        Matching / Non-Matching
        |                      |
        +----------+-----------+
                   |
                   v
          Record Linkage Models
                   |
                   v
          Evaluation & Analysis
```
<H3>Jupyter Notebook Setup</H3>
The Installing Jupyter Notebook.pdf document provides guidance for setting up Jupyter Notebook.
<BR><BR>
Jupyter Notebook is useful for this training because it allows the user to:
<UL>
   <LI>Execute Python code interactively.</LI>
   <LI>Inspect datasets.</LI>
   <LI>Visualise distributions.</LI>
   <LI>Experiment with data-generation techniques.</LI>
   <LI>Document analysis alongside executable code.</LI>
   <LI>Reproduce individual steps of a data-science workflow.</LI> 
</UL>
Before starting the practical exercises, ensure that Python and Jupyter Notebook are installed and working correctly.
