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
<BR>
<B>1. Longitudinal Data Preparation</B>  
<BR><BR>
The repository includes <B>Pentaho Data Integration (.ktr)</B> transformations for converting source longitudinal data from long format into a structure suitable for subsequent processing.
<BR><BR>
The current repository contains multiple versions of the transformation:
<BR><BR>
The file <B>Converting Long to Wide Format.pdf</B> in the folder <B>01 Convert Source Data From Long to Wide/</B> describes the process of converting the data from Long to Wide
<BR><BR>
This stage provides a reproducible ETL foundation for longitudinal population data. This conversion is only done to converte the records from events to episodes and therefor are easy for the record libkage as only the invididual's details are needed for the purpose. 
<BR><BR>

