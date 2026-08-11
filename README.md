<h1>Record Linkage Using Machine Learning Techniques</h1>
<p align="center"><b>
A reproducible research workflow for synthetic data generation, longitudinal data preparation, and machine learning–based record linkage
</b>  </p>
<hr>
📌<b> Overview</b>
<BR><Br>
<B>Record linkage</B> is the process of determining whether records from different datasets refer to the same underlying individual or entity.
<BR><BR>
This repository presents a research-oriented workflow for developing and evaluating <b>>machine learning–based record linkage methods, particularly in the context of population health, longitudinal studies, and health and demographic surveillance data</b>.
<BR><BR>
The project follows a synthetic-to-real-data strategy:<BR><BR>
<img src="images/Clipboard_08-11-2026_01.jpg" alt="Project Banner" width="250" height="950" align="center">
<BR><BR>
The central idea is to <b>develop and validate linkage methodology in a controlled environment before applying it to complex real-world population and health datasets</b>.
<hr>
<br>
🎯 <b>Research Objectives</b><BR><BR>
The repository is designed to investigate the following questions:<BR><BR>
<UL>
<LI>Can realistic synthetic population data be generated while preserving important source-data characteristics?</LI><BR>
<LI>How can synthetic datasets be used to develop and benchmark record linkage methods?</LI><BR>
<LI>Which data-quality and similarity features are most informative for identifying matching records?</LI><BR>
<LI>How can machine learning improve linkage beyond simple deterministic rules?</LI><BR>
<LI>How can validated linkage approaches be transferred from synthetic data to real-world longitudinal datasets?</LI><BR>
</UL>
<HR>
<BR><BR>
🧬 <B>Why Record Linkage?</B>
<BR><BR>
Population health research frequently requires information from multiple data sources.
<BR>
For example:<BR><BR>
<img src="images/Clipboard_08-11-2026_02.jpg" alt="Project Banner" width="250" height="950" align="center">
<BR>
The quality of downstream epidemiological analyses depends heavily on the quality of this integration.
<BR><BR>
Incorrect linkage can introduce:<BR><BR>
<UL>
<LI>False matches — records belonging to different individuals are linked.</LI><BR>
<LI>False non-matches — records belonging to the same individual are not linked.</LI><BR>
<LI>Selection bias — linkage errors are not distributed uniformly across populations.</LI><BR>
<LI>Loss of longitudinal information — repeated observations may fail to connect.</LI><BR>
<LI>Reduced statistical power — fragmented records can lead to incomplete trajectories.</LI><BR>
</UL>
<HR>
🔬 <B>Methodology</B>
<BR><BR>
<B>1. Longitudinal Data Preparation</B>  
<BR><BR>
The repository includes <B>Pentaho Data Integration (.ktr)</B> transformations for converting source longitudinal data from long format into a structure suitable for subsequent processing.
<BR><BR>
The current repository contains multiple versions of the transformation:
<BR><BR>
The file <B>Converting Long to Wide Format.pdf</B> in the folder <B>01 Convert Source Data From Long to Wide/</B> describes the process of converting the data from Long to Wide
<BR><BR>
This stage provides a reproducible ETL foundation for longitudinal population data. This conversion is only done to convert the records from events to episodes and therefore make it easy for record linkage, as only the individual's details are needed for the purpose. 
<BR><BR>
<B>2. 🔄 Data Standardisation</B>
<BR><BR>
Data standardisation is a foundational component of this research workflow. Population-health, HDSS, clinical, and longitudinal datasets are often collected using different structures, variable definitions, coding systems, and data formats. These differences make it difficult to integrate datasets and perform reliable downstream analyses.
<BR><BR>
This project explores the use of the <B>OMOP Common Data Model (CDM)</B> as a standardised framework for transforming heterogeneous health and population data into a common structure.
<BR><BR>
The objective is to create <B>standardised, interoperable, and research-ready data </B>while preserving the information required for longitudinal analysis and record linkage.
<BR><BR>
<B>OMOP CDM Standardisation Workflow</B><BR>
<img src="images/Clipboard_08-11-2026_04.jpg" alt="Project Banner" width="250" height="950" align="center">
<BR><BR>
<B>3. 🧬 Synthetic Data Generation</B>
<BR><BR> 
Synthetic data generation is a central component of this research workflow. It provides a controlled environment for developing and evaluating record linkage methods while reducing the need to expose identifiable individual-level population data during methodological development.
<BR><BR>
The project explores <B>CTGAN (Conditional Tabular Generative Adversarial Network)</B> for generating synthetic tabular population data while attempting to preserve important characteristics of the underlying source data.
<BR><BR>
The current experiments focus particularly on demographic, geographic, and date-related variables that may subsequently contribute to record linkage.
<BR><BR>
<B>Variables Considered</B>
<BR><BR>
The synthetic-data experiments include distributions for:
<UL>
<LI>Date of birth — day</LI><BR>
<LI>Date of birth — month</LI><BR>
<LI>Date of birth — year</LI><BR>
<LI>Sex</LI><BR>
<LI>Village</LI><BR>
<LI>Sub-village</LI><BR>
</UL>
<BR>
The repository contains separate CTGAN experiments, including an experiment specifically designed to investigate <B>well-distributed Date-of-Birth</B> data. The generated outputs include distribution plots, HTML analysis, PDF reports, and comparison results.
<img src="images/Clipboard_08-11-2026_03.jpg" alt="Project Banner" width="250" height="950" align="center">
<BR>
<B>Why Synthetic Data?</B><BR><BR>
Synthetic data is particularly useful for this research because record linkage requires controlled experiments in which the researcher can understand the underlying relationships between records.
<BR><BR>
It provides opportunities to:
<BR><BR>
<UL>
<LI>Develop methodology without exposing identifiable records.</LI><BR>
<LI>Create controlled matching and non-matching scenarios.</LI><BR>
<LI>Introduce realistic data variation.</LI><BR>
<LI>Investigate the effect of missing or inconsistent information.</LI><BR>
<LI>Benchmark alternative linkage approaches.</LI><BR>
<LI>Repeat experiments under controlled conditions.</LI><BR>
<LI>Study the behaviour of linkage methods at different scales.</LI><BR>
</UL>
<BR>
