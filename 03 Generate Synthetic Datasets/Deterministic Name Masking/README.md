<H1>Deterministic Name Masking for Synthetic Datasets</H1>
<P>This module provides a reproducible, distribution-aware pipeline for masking person names in synthetic linkage datasets. It forms part of the broader Record Linkage Using Machine Learning Techniques framework, ensuring privacy preservation without altering underlying statistical name distributions.</P>
<H2>Overview</H2>
When preparing benchmark or synthetic datasets for record linkage, replacing real names with purely random text strips away key statistical properties (e.g., common vs. rare name frequencies).
<BR><BR>
This set of Python programs achieves deterministic pseudonymization:
<UL>
  <LI>Distribution Preservation: Uses weighted random choices matching real-world first and last name frequencies from baseline data.</LI>
  <LI>Deterministic Reproducibility: Uses individual record identifiers to seed pseudorandom generation. Re-running the pipeline yields identical pseudonyms every time for a given record ID.</LI>
  <LI>PostgreSQL Integration: Reads source datasets directly from database tables and writes masked outputs into dedicated schemas.
</LI>
</UL>
<BR>
<H2>Pipeline Architecture</H2>
─> (Step 1: Upload Script) ─> [ Excel / Raw Data ] ─> [ Name Pool Table ]<BR>
─> (Step 2: Masking Engine) ─> [ Cleaned Dataset  ] + [ Synthetic Target ] ─> [ Masked Output Table ]<BR>
<H2>Getting Started</H2>
<B>Prerequisites</B><BR>
Ensure you have Python 3.8+ and PostgreSQL installed, along with the required libraries:<BR>
<I>
&nbsp;&nbsp;&nbsp;&nbsp;  pip install pandas numpy sqlalchemy psycopg2 openpyxl
</I>
<BR><BR>
<B>Database Setup</B><BR>
Modify the connection parameters in the scripts, wherever necessary, to match your database credentials:
<I>
<BR>&nbsp;&nbsp;&nbsp;&nbsp; DB_USER = "postgres"
<BR>&nbsp;&nbsp;&nbsp;&nbsp; DB_PASS = "your_password"
<BR>&nbsp;&nbsp;&nbsp;&nbsp; DB_HOST = "localhost"
<BR>&nbsp;&nbsp;&nbsp;&nbsp; DB_PORT = "5432"
<BR>&nbsp;&nbsp;&nbsp;&nbsp; DB_NAME = "PhD"
<BR>&nbsp;&nbsp;&nbsp;&nbsp; SCHEMA_NAME = "synthetic_data_final"
</I>
<BR>
<H2>Module Workflow Sequence</H2>
This folder contains Python programs that implement a two-stage data engineering pipeline designed to prepare reference data and execute deterministic, distribution-aware name masking for synthetic record linkage datasets.
<BR>
<H2>Step 1: Populate Reference Pools</H2>
<UL>
  <LI><B><I>01 deterministic name masking firstname pool.py</I></B></LI>
</UL>
This script reads an Excel file containing first names, cleans and formats the data, and uploads it to a PostgreSQL database.<BR>
<B>Key Steps</B>
<UL>
  <LI>Database Verification: Connects to PostgreSQL using SQLAlchemy and runs a simple query (SELECT 1;) to verify credentials before running.</LI>  
  <LI>Data Ingestion: Reads the FirstNames sheet from Pool Name List.xlsx, loading all values as strings. </LI> 
  <LI>Cleaning & Formatting: Drops duplicate (firstname, sex) entries, randomly shuffles the rows, and assigns sequential record IDs (recnr). </LI> 
  <LI>Database Export: Creates the target schema (synthetic_data_final) if missing and uploads the processed data to the deterministic_firstname_pool table.  </LI>
</UL>
