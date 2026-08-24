
<H1>Generate Synthetic Datasets</H1>
This folder contains the synthetic data generation and privacy-preserving data preparation components used in the Record Linkage Using Machine Learning Techniques project.
<BR><BR>
The purpose of this task is to create realistic datasets for record-linkage experiments while preserving important characteristics of the source data. The workflows cover generative modelling with CTGAN, improved synthetic data generation with a better-distributed Date of Birth (DoB) field, and deterministic name masking for privacy-preserving experiments.
<HR>
<B>Onjectives</B>
<UL>
  <LI>Generate synthetic records that retain useful statistical relationships from source data</LI>
  <LI>Produce benchmark datasets suitable for record-linkage and machine-learning experiments.</LI>
  <LI>Improve the distribution of important demographic attributes such as Date of Birth.</LI>
  <LI>Replace personal names with deterministic, distribution-aware pseudonyms where required.</LI>
  <LI>Support reproducible experiments by keeping the data-generation and masking workflows structured and repeatable.</LI>
</UL>
<B>Folder Content</B><BR>
<TABLE>
  <TR>
    <TH>Folder</TH>
    <TH>Purpose</TH>
  </TR>
  <TR>
    <TD>02A Synthetic Data Generation Using CTGAN</TD>
    <TD>Generates synthetic records using CTGAN-based modelling.</TD>
  </TR>
  <TR>
    <TD>02B Synthetic Data Generation Using CTGAN with Well-Distributed DoB</TD>
    <TD>Extends CTGAN-based generation with additional attention to obtaining a well-distributed Date of Birth field.</TD>
  </TR>
   <TR>
    <TD>DSWB Training 202502</TD>
    <TD>Contains the related training/data-generation materials for the DSWB dataset workflow.</TD>
  </TR>
  <TR>
    <TD>Deterministic Name Masking</TD>
    <TD>Provides deterministic, distribution-aware pseudonymisation of first and last names using PostgreSQL-backed reference pools.</TD>
  </TR>
</TABLE>
<B>Synthetic Data Generation with CTGAN</B><BR>
The CTGAN workflows use Conditional Tabular Generative Adversarial Networks to learn relationships in tabular data and generate new synthetic records.
<BR>
The repository contains two related CTGAN implementations.
<H3>Workflow</H3>
<img src="Images\Image 1.jpg" alt="Workflow Image">
<H3>Environment</H3>
The exact dependencies depend on the workflow being executed. Typical components include:
<UL>
  <LI>Python 3.8+</LI>
  <LI>pandas</LI>
  <LI>NumPy</LI>
  <LI>CTGAN / SDV ecosystem packages for generative modelling</LI>
  <LI>SQLAlchemy</LI>
  <LI>psycopg2</LI>
  <LI>openpyxl</LI>
  <LI>Jupyter Notebook / JupyterLab for notebook-based workflows</LI>
  <LI>PostgreSQL</LI>
</UL>
<H3>Reproducibility</H3>
For reliable experiments:
<UL>
  <LI>Keep source-data preprocessing consistent across runs.</LI>
  <LI>Record the model and library versions used for synthetic-data generation.</LI>
  <LI>Use controlled random seeds where supported by the workflow.</LI>
  <LI>Preserve the same input/reference distributions when comparing experiments.</LI>
  <LI>For deterministic name masking, use the same record identifiers and name pools when reproducibility is required.</LI>
</UL>
<H3>Data Privacy</H3>
Synthetic data is intended for experimentation and benchmarking, but synthetic generation does not automatically guarantee privacy.<BR><BR>
Generated datasets should be evaluated for:
<UL>
  <LI>Unintended disclosure</LI>
  <LI>Re-identification risk</LI>
  <LI>Similarity to source records</LI>
  <LI>Preservation of sensitive attributes</LI>
</UL>
The deterministic name-masking workflow provides an additional pseudonymisation layer for names while retaining distributional characteristics useful for record-linkage research.
<H3>Role in the Overall Project</H3>
This folder represents the synthetic-data generation tasks of the broader project.
<BR><BR>
The resulting datasets can subsequently be used to:
<UL>
  <LI>Develop record-linkage models</LI>
  <LI>Train machine-learning algorithms</LI>
  <LI>Evaluate matching performance</LI>
  <LI>Compare different record-linkage techniques</LI>
  <LI>Conduct reproducible benchmarking experiments</LI>
</UL>
<HR>
