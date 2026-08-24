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
<BR><BR>
