#############
## This script evaluates and validates the effectiveness of a data anonymisation 
# process by comparing original personal names against masked equivalents.
#############

import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# ==========================================================
# CONFIGURATION (Static password as parameter)
# ==========================================================
DB_USER = "postgres"
DB_PASS = "password1234"   # ← Static password defined here
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "PhD"
SCHEMA_NAME = "synthetic_data_final"

TABLE_ORIGINAL = "input_rdlinkageinputdatafinali_cleaned_v1"
TABLE_MASKED = "input_rdlinkageinputdatafinali_synthetic_masked_v4"

# ==========================================================
# CONNECT TO DATABASE
# ==========================================================
print("[1] Connecting to database...")
try:
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print("✅ Connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit(1)

# ==========================================================
# LOAD DATA
# ==========================================================
query_orig = f"SELECT * FROM {SCHEMA_NAME}.{TABLE_ORIGINAL}"
query_mask = f"SELECT * FROM {SCHEMA_NAME}.{TABLE_MASKED}"

print("\n[2] Loading tables...")
df_orig = pd.read_sql(query_orig, engine)
df_mask = pd.read_sql(query_mask, engine)
print(f"   → Original table: {len(df_orig)} rows")
print(f"   → Masked table: {len(df_mask)} rows")

# ==========================================================
# JOIN TABLES
# ==========================================================
print("\n[3] Joining tables for comparison...")

join_key = 'pseudo_idlong' if 'pseudo_idlong' in df_orig.columns and 'pseudo_idlong' in df_mask.columns else 'idlong'
if join_key not in df_orig.columns or join_key not in df_mask.columns:
    print("❌ Error: Matching join key not found in both tables!")
    exit(1)

df_merged = pd.merge(df_orig, df_mask, on=join_key, how='inner', suffixes=('_orig', '_mask'))
print(f"   → Merged table: {len(df_merged)} rows (joined on {join_key})")

# ==========================================================
# COMPARE NAMES
# ==========================================================
print("\n[4] Comparing original vs. masked names...")

same_first = np.sum(df_merged['firstname'] == df_merged['masked_firstname'])
same_last = np.sum(df_merged['lastname'] == df_merged['masked_lastname'])
diff_first = len(df_merged) - same_first
diff_last = len(df_merged) - same_last

unique_masked_first = df_merged['masked_firstname'].nunique()
unique_masked_last = df_merged['masked_lastname'].nunique()
unique_orig_first = df_merged['firstname'].nunique()
unique_orig_last = df_merged['lastname'].nunique()

overlap_first = len(set(df_merged['masked_firstname']) & set(df_merged['firstname']))
overlap_last = len(set(df_merged['masked_lastname']) & set(df_merged['lastname']))

# ==========================================================
# REPORT SUMMARY
# ==========================================================
print("\n====== Masking Effect Statistics ======")
print(f"Total records compared: {len(df_merged)}")

print("\n--- Firstname Comparison ---")
print(f"Same firstname: {same_first}")
print(f"Different firstname: {diff_first}")
print(f"Unique original firstnames: {unique_orig_first}")
print(f"Unique masked firstnames: {unique_masked_first}")
print(f"Overlapping firstnames (original/masked): {overlap_first}")

print("\n--- Lastname Comparison ---")
print(f"Same lastname: {same_last}")
print(f"Different lastname: {diff_last}")
print(f"Unique original lastnames: {unique_orig_last}")
print(f"Unique masked lastnames: {unique_masked_last}")
print(f"Overlapping lastnames (original/masked): {overlap_last}")

pct_first_changed = 100 * diff_first / len(df_merged)
pct_last_changed = 100 * diff_last / len(df_merged)
print(f"\nPercent FIRSTNAMES changed: {pct_first_changed:.2f}%")
print(f"Percent LASTNAMES changed: {pct_last_changed:.2f}%")

print("\n--- Sample of changed names ---")
sample_changed = df_merged[
    (df_merged['firstname'] != df_merged['masked_firstname']) &
    (df_merged['lastname'] != df_merged['masked_lastname'])
].head(10)
for _, row in sample_changed.iterrows():
    print(f"Original: {row['firstname']} {row['lastname']} | Masked: {row['masked_firstname']} {row['masked_lastname']}")

print("\n====== Summary ======")
if pct_first_changed > 90 and pct_last_changed > 90:
    print("✅ Masking effective: Most names changed — privacy preserved.")
else:
    print("⚠️ Masking may need review: Significant overlap between original and masked names.")

# ==========================================================
# (1) VENN DIAGRAM — NAME OVERLAP
# ==========================================================
print("\n[5] Generating Venn diagram for name overlap...")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Venn for Firstnames ---
venn2(subsets=(unique_orig_first, unique_masked_first, overlap_first),
      set_labels=('Original Firstnames', 'Masked Firstnames'),
      ax=axes[0])
axes[0].set_title('Venn Diagram: Original vs. Masked Firstnames')

# --- Venn for Lastnames ---
venn2(subsets=(unique_orig_last, unique_masked_last, overlap_last),
      set_labels=('Original Lastnames', 'Masked Lastnames'),
      ax=axes[1])
axes[1].set_title('Venn Diagram: Original vs. Masked Lastnames')

plt.tight_layout()
plt.show()

# ==========================================================
# (2) DISTRIBUTION PLOTS — NAME FREQUENCY
# ==========================================================
print("\n[6] Generating name frequency distribution plots...")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ==========================================================
# --- Frequency Distribution for Firstnames ---
# ==========================================================
orig_first_freq = df_merged['firstname'].value_counts()
mask_first_freq = df_merged['masked_firstname'].value_counts()

axes[0].hist(
    orig_first_freq,
    bins=min(30, len(orig_first_freq.unique())),
    alpha=0.6,
    label='Original',
    color='skyblue',
    density=True
)
axes[0].hist(
    mask_first_freq,
    bins=min(30, len(mask_first_freq.unique())),
    alpha=0.6,
    label='Masked',
    color='lightcoral',
    density=True
)

axes[0].set_title('Firstname Frequency Distribution', fontsize=12)
axes[0].set_xlabel('Occurrences per Name', fontsize=10)
axes[0].set_ylabel('Density', fontsize=10)
axes[0].legend()
axes[0].set_xlim(left=0, right=max(orig_first_freq.max(), mask_first_freq.max()) + 1)
axes[0].set_ylim(bottom=0)

# ==========================================================
# --- Frequency Distribution for Lastnames ---
# ==========================================================
orig_last_freq = df_merged['lastname'].value_counts()
mask_last_freq = df_merged['masked_lastname'].value_counts()

axes[1].hist(
    orig_last_freq,
    bins=min(30, len(orig_last_freq.unique())),
    alpha=0.6,
    label='Original',
    color='skyblue',
    density=True
)
axes[1].hist(
    mask_last_freq,
    bins=min(30, len(mask_last_freq.unique())),
    alpha=0.6,
    label='Masked',
    color='lightcoral',
    density=True
)

axes[1].set_title('Lastname Frequency Distribution', fontsize=12)
axes[1].set_xlabel('Occurrences per Name', fontsize=10)
axes[1].set_ylabel('Density', fontsize=10)
axes[1].legend()
axes[1].set_xlim(left=0, right=max(orig_last_freq.max(), mask_last_freq.max()) + 1)
axes[1].set_ylim(bottom=0)

# ==========================================================
# --- Final Layout ---
# ==========================================================
plt.tight_layout()
plt.show()


print("\n🎉 Visualization complete: Venn and distribution plots displayed successfully.")
