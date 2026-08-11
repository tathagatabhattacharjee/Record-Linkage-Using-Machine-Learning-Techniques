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
<img src="images/Clipboard_08-11-2026_01.jpg" alt="Project Banner" width="600" height="1500" align="center">
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
<img src="images/Clipboard_08-11-2026_02.jpg" alt="Project Banner" width="600" height="1500" align="center">
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
<img src="images/Clipboard_08-11-2026_04.jpg" alt="Project Banner" width="600" height="1500" align="center">
<BR><BR>
<B>What is Being Standardised?</B><BR><BR>
The OMOP CDM provides a common structure and vocabulary framework for representing observational health data.
<BR><BR>
The standardisation process addresses several dimensions of heterogeneous source data:
<TABLE>
   <tr>
      <th>Area</th>
      <th>Standardisation Approach</th>
   </tr>
   <tr>
      <td>Data Structure</td>
      <td>Transform source data into appropriate OMOP CDM tables</td>
   </tr>
      <tr>
      <td>Variable Definitions</td>
      <td>Map source variables to standard OMOP concepts and fields</td>
   </tr>
      <tr>
      <td>Clinical Concepts</td>
      <td>Map local clinical codes to standard OMOP concepts where applicable</td>
   </tr>
      <tr>
      <td>Dates & Times</td>
      <td>Harmonise date and datetime representations</td>
   </tr>
      <tr>
      <td>Demographics</td>
      <td>Standardise person-level demographic information</td>
   </tr>
      <tr>
      <td>Geography</td>
      <td>Harmonise geographic and location-related information</td>
   </tr>
      <tr>
      <td>Identifiers</td>
      <td>Manage source identifiers and person identifiers appropriately</td>
   </tr>
      <tr>
      <td>Observation Periods</td>
      <td>Represent longitudinal periods consistently</td>
   </tr>
      <tr>
      <td>Events</td>
      <td>Organise clinical and observational events according to the CDM structure</td>
   </tr>
      <tr>
      <td>Vocabulary</td>
      <td>Use standardised OMOP vocabularies where appropriate</td>
   </tr>
      <tr>
      <td>Data Quality</td>
      <td>Identify inconsistencies, missing values, invalid values, and structural problems</td>
   </tr>
</TABLE>
<BR><BR>
<B>Source-to-OMOP Transformation</B>
<BR><BR>
The ETL process can be conceptualised as:
<BR>
<img src="images/Clipboard_08-11-2026_05.jpg" alt="Project Banner" width="600" height="1500" align="center">
<BR>
* The data need to be transformed and harmonised before being incorporated into an OMOP-oriented analytical environment.
<BR><BR>
<B>OMOP CDM as an Interoperability Layer</B>
<BR><BR>
One of the major advantages of using the OMOP CDM is that it separates source-specific data structures from the common analytical representation.
<BR>
<img src="images/Clipboard_08-11-2026_06.jpg" alt="Project Banner" width="600" height="1500" align="center">
<BR>
Instead of developing every analysis separately for every source system, data can be transformed into a common representation.
<BR><BR>
This supports:
<BR><BR>
<UL>
<LI>Cross-dataset interoperability</LI><BR>
<LI>Consistent analytical definitions</LI><BR>
<LI>Reusable research workflows</LI><BR>
<LI>Standardised observational research</LI><BR>
<LI>Cross-site data harmonisation</LI><BR>
<LI>Improved data quality</LI><BR>
<LI>More reproducible analyses</LI><BR>
</UL>
<BR>
<B>OMOP CDM and Record Linkage</B>
<BR><BR>
Data standardisation and record linkage are complementary components of the overall research workflow.
<BR><BR>
Standardisation provides a consistent representation of the data, while record linkage addresses the question of whether observations from different sources correspond to the same underlying individual.
<BR>
<img src="images/Clipboard_08-11-2026_07.jpg" alt="Project Banner" width="600" height="1500" align="center">
<BR>
Importantly, OMOP standardisation does not itself perform record linkage. Instead, it establishes a common data structure and vocabulary that can support subsequent integration, analysis, and linkage workflows.
<BR><BR>
<B>OMOP CDM and Population Health Research</B><BR><BR>
The standardised data environment can support downstream research activities such as:<BR><BR>
<UL>
<LI>Population-level descriptive analyses</LI><BR>
<LI>Longitudinal cohort construction</LI><BR>
<LI>Epidemiological studies</LI><BR>
<LI>Health outcome research</LI><BR>
<LI>Cross-site observational research</LI><BR>
<LI>Data quality assessment</LI><BR>
<LI>Record linkage and data integration</LI><BR>
<LI>Reproducible population-health analyses</LI><BR>
</UL>
<BR>
<B>OMOP Vocabulary Standardisation</B>
<BR><BR>
Where applicable, source-specific codes can be mapped to standard OMOP concepts.
<BR><BR>
The ETL process transforms source data into the OMOP Common Data Model by sequentially mapping native terminology to standardised medical concepts. It begins with Local Source Code, which represents the raw, unstandardised clinical data in its native format (such as local lab codes or proprietary diagnoses). This data is then extracted to construct the Source Vocabulary, cataloging all unique native terms used within the source database. Next, Vocabulary Mapping takes place, utilising tools like USAGI or standardised crosswalks to systematically translate each native source term into its corresponding Standard OMOP Concept within the OHDSI standardised vocabularies (e.g., SNOMED CT for conditions or RxNorm for medications). Finally, these standardised concepts, along with their structured domain attributes, are loaded into the target OMOP CDM tables, completing the transition from disparate local data to a globally unified, analytics-ready schema.
<BR><BR>
This vocabulary standardisation is particularly important when combining information from multiple systems that use different coding schemes.
<BR><BR>
<B>Data Quality Before and After ETL</B>
<BR><BR>
An important part of the standardisation workflow is documenting data-quality issues before and after transformation.<BR>
Examples include:
<BR><BR>
<UL>
<LI>Missing demographic information</LI><BR>
<LI>Invalid dates</LI><BR>
<LI>Inconsistent categorical values</LI><BR>
<LI>Duplicate records</LI><BR>
<LI>Inconsistent identifiers</LI><BR>
<LI>Unmapped source codes</LI><BR>
<LI>Invalid concept mappings</LI><BR>
<LI>Unexpected values</LI><BR>
<LI>Inconsistent geographic classifications</LI><BR>
</UL>
<BR>
The goal is not simply to move data into OMOP tables, but to create a well-documented and quality-assessed research dataset.
<BR><BR>
<B>Role in the Overall Research Pipeline</B>
   <BR><BR>
The OMOP CDM data standardisation stage establishes a foundation by converting raw source data into a unified format, which sequentially enables synthetic data generation, validation, and record linkage feature engineering. This structured pipeline then supports machine learning model development for record linkage, rigorous evaluation, and reproducible research—ultimately driving impactful population health applications.
<BR><BR>
The use of OMOP CDM provides a common foundation for transforming heterogeneous population and health data into interoperable, research-ready datasets suitable for reproducible observational and population-health research.
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
<img src="images/Clipboard_08-11-2026_03.jpg" alt="Project Banner" width="600" height="1500" align="center">
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
