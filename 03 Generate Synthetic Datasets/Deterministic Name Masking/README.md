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
<OL>
  <LI>Database Verification: Connects to PostgreSQL using SQLAlchemy and runs a simple query (SELECT 1;) to verify credentials before running.</LI>  
  <LI>Data Ingestion: Reads the FirstNames sheet from Pool Name List.xlsx, loading all values as strings. </LI> 
  <LI>Cleaning & Formatting: Drops duplicate (firstname, sex) entries, randomly shuffles the rows, and assigns sequential record IDs (recnr). </LI> 
  <LI>Database Export: Creates the target schema (synthetic_data_final) if missing and uploads the processed data to the deterministic_firstname_pool table.  </LI>
</OL>
<UL>
  <LI><B><I>02 deterministic name masking lastname pool.py</I></B></LI>
</UL>
This script extracts last-name data from an Excel spreadsheet, cleans and formats the data, and uploads it to a PostgreSQL database.<BR>
<B>Key Steps</B>
<OL>
  <LI>Database Verification: Connects to PostgreSQL using SQLAlchemy and executes SELECT 1; to confirm connectivity before running.</LI>  
  <LI>Data Ingestion: Reads the LastNames worksheet from Pool Name List.xlsx and normalizes all column headers to lowercase strings. </LI> 
  <LI>Dynamic Column Matching & Cleaning: Automatically detects the last-name column, drops duplicates based on that column, shuffles the rows randomly, and assigns sequential record numbers (recnr). </LI> 
  <LI>Database Export: Guarantees the existence of the synthetic_data_final schema and uploads the final dataset to the deterministic_lastname_pool table.</LI>
</OL>
<H2>Sequence Step 2: Deterministic Distribution-Aware Name Masking</H2>
<UL>
  <LI><B><I>03 deterministic name masking synthetic data.py</I></B></LI>
</UL>
This script performs distribution-aware, deterministic name masking on a synthetic dataset by drawing pseudonyms from real-world name distributions in PostgreSQL.<BR>
<B>Key Steps</B>
<OL>
  <LI>Dataset Ingestion: Loads baseline real-world data (TABLE_CLEANED) to capture name distributions and synthetic records (TABLE_SYNTHETIC) that need anonymization.</LI>  
  <LI>Frequency Analysis: Normalises names to title case and computes relative frequency weights using collections.Counter Python library.</LI> 
  <LI>Deterministic Masking: Iterates over unique individual IDs and uses them as random seeds (random.seed(str(uid))) to sample pseudonyms with random.choices. This preserves statistical distributions while ensuring reproducible outputs without lookup tables.</LI> 
  <LI>Merging & Export: Joins masked_firstname and masked_lastname back to the synthetic dataset, prints sample statistics, and overwrites the output table in PostgreSQL.</LI>
</OL>
