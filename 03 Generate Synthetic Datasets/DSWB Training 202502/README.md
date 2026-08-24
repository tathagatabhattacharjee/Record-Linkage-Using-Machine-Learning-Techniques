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
<H3>Training Presentations</H3>
<B>Bootcamp — Synthetic Data Creation</B><BR>
The Bootcamp - Synthetic Data Creation.pptx.pdf presentation provides the primary bootcamp material for synthetic-data creation.
<BR><BR>
It is intended to be used as the conceptual and practical introduction to the synthetic-data generation exercises.
<H3>Platform Presentation — Synthetic Data</H3>
The Platform Presentation - Synthetic Data - I.pdf provides additional presentation material covering synthetic-data concepts and the broader context in which synthetic data can be used.
<BR><BR>
Together, the presentation materials provide background before proceeding to the practical case study.
<BR>
<H3>Case Study</H3>
The Case Study directory contains the practical case-study component of the training.
<BR><BR>
The case study is intended to bridge the gap between the concepts presented in the training material and an actual synthetic-data workflow.
<BR><BR>
A typical case-study workflow can include:
<br>
```text
1. Understand the source dataset
          |
          v
2. Identify relevant attributes
          |
          v
3. Prepare / clean the data
          |
          v
4. Select a synthetic-data approach
          |
          v
5. Train / configure the generation method
          |
          v
6. Generate synthetic records
          |
          v
7. Evaluate the generated data
          |
          v
8. Use the synthetic data for downstream analysis
```
<BR>
<H3>Recommended Learning Sequence</H3>
For someone working through this material for the first time, the following order is recommended:
<BR>
<H4>Step 1 — Understand Synthetic Data</H4>
Start with:
<UL>
        <LI>Platform Presentation - Synthetic Data - I.pdf</LI>
</UL>
This provides the conceptual background for synthetic data.
<H4>Step 2 — Review the Bootcamp Material</H4>
Continue with:
<UL>
        <LI>Bootcamp - Synthetic Data Creation.pptx.pdf</LI>
</UL>
This provides a more practical introduction to creating synthetic data.
<H4>Step 3 — Set Up Jupyter Notebook</H4>
Follow:
<UL>
    <LI>Installing Jupyter Notebook.pdf
</LI>
</UL>
You can then use the Jupyter environment for the practical exercises.
<H4>Step 4 — Complete the Case Study</H4>
Proceed to:
<UL>
   <LI>Case Study</LI>
</UL>
Apply the concepts from the presentations in a practical setting.
<h4>Relationship to the Main Project</h4>
This training folder forms part of the Generate Synthetic Datasets task of the broader project.
<BR><BR>
The training material provides the conceptual and practical foundation for the synthetic datasets subsequently used in record-linkage experiments.
<BR><BR>
The broader workflow can be viewed as:
```text
Training & Data Understanding
            |
            v
Synthetic Dataset Generation
            |
            v
Synthetic Data Quality Evaluation
            |
            v
Record Linkage Dataset Preparation
            |
            v
Feature Engineering
            |
            v
Machine Learning Models
            |
            v
Record Linkage Evaluation
```
<BR>
<H4>Prerequisites</H4>
For the practical exercises, the following environment is recommended:
<UL>
   <LI>Python</LI>
   <LI>Jupyter Notebook or JupyterLab</LI>
   <LI>pandas</LI>
   <LI>NumPy</LI>
   <LI>matplotlib</LI>
   <LI>scikit-learn</LI>
   <LI>Appropriate synthetic-data generation libraries required by the case study</LI>
  Additional dependencies may be required depending on the specific implementation used in the case study.      
</UL>
<H4>Important Considerations</H4>
Synthetic data should not automatically be considered completely anonymous or risk-free.
<BR>
When generating synthetic datasets, consider:
<UL>
        <LI>Statistical comparison to the source data.</LI>
        <LI>Preservation of important relationships.</LI>
        <LI>Potential memorisation of source records.</LI>
        <LI>Disclosure and re-identification risks.</LI>
        <LI>Utility for downstream machine-learning tasks.</LI>
        <LI>Whether sensitive attributes remain identifiable.</LI>
        <LI>The intended use and sharing requirements of the generated data.</LI>
</UL>
Synthetic-data quality should therefore be evaluated from both utility and privacy perspectives.
<H4>Related Project Material</H4>
More information is locaed under the folder ``` 03 Generate Synthetic Datasets  ```
<BR>
<HR>
