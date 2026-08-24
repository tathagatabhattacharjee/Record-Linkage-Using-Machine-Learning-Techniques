#############
##This Python script performs distribution-aware, deterministic name masking (anonymisation)
# on a synthetic dataset using real-world name frequency distributions from a source database.
#############



import pandas as pd
import numpy as np
import random
from sqlalchemy import create_engine, text
import time
from collections import Counter

# ==========================================================
# CONFIGURATION
# ==========================================================
DB_USER = "postgres"
DB_PASS = "password1234"   # static password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "PhD"

SCHEMA_NAME = "synthetic_data_final"
TABLE_CLEANED = "input_rdlinkageinputdatafinali_cleaned_v1"
TABLE_SYNTHETIC = "input_rdlinkageinputdatafinali_synthetic_v4"
OUTPUT_TABLE = "input_rdlinkageinputdatafinali_synthetic_masked_v4"

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================
def timer(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{msg}]...")
            start = time.time()
            result = func(*args, **kwargs)
            print(f"   → Done ({time.time() - start:.2f}s)")
            return result
        return wrapper
    return decorator


def deterministic_choice(options, seed_val):
    """
    Deterministically selects one element from 'options'
    based on stringified seed value.
    """
    random.seed(str(seed_val))
    return random.choice(options)


# ==========================================================
# MAIN SCRIPT
# ==========================================================
print("\n" + "=" * 70)
print("Deterministic Name Masking — Distribution-Aware")
print("=" * 70)

# 1. Connect to PostgreSQL
print("\n[1] Connecting to PostgreSQL database...")
try:
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    with engine.connect() as conn:
        conn.execute(text("SELECT 1;"))
    print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit(1)

# 2. Load input datasets
@timer("2. Loading cleaned (original) dataset")
def load_cleaned():
    query = f"SELECT idlong, firstname, lastname, sex FROM {SCHEMA_NAME}.{TABLE_CLEANED}"
    return pd.read_sql(query, engine)

@timer("3. Loading synthetic dataset")
def load_synthetic():
    query = f"SELECT * FROM {SCHEMA_NAME}.{TABLE_SYNTHETIC}"
    return pd.read_sql(query, engine)

df_cleaned = load_cleaned()
df_input = load_synthetic()

print(f"   → Cleaned data rows: {len(df_cleaned):,}")
print(f"   → Synthetic data rows: {len(df_input):,}")

# 3. Prepare name pools and distributions
print("\n[4] Preparing name frequency distributions...")

try:
    df_cleaned["firstname"] = df_cleaned["firstname"].astype(str).str.title()
    df_cleaned["lastname"] = df_cleaned["lastname"].astype(str).str.title()

    first_counts = Counter(df_cleaned["firstname"])
    last_counts = Counter(df_cleaned["lastname"])

    fnames = list(first_counts.keys())
    lnames = list(last_counts.keys())

    first_weights = np.array(list(first_counts.values())) / sum(first_counts.values())
    last_weights = np.array(list(last_counts.values())) / sum(last_counts.values())

    print(f"   → Unique firstnames: {len(fnames)}")
    print(f"   → Unique lastnames: {len(lnames)}")

except Exception as e:
    print(f"❌ Error preparing name lists: {e}")
    exit(1)

# 4. Deterministic masking generation
print("\n[5] Generating deterministic masked names...")

if "idlong" not in df_input.columns:
    print("❌ ERROR: Column 'idlong' not found in synthetic data!")
    exit(1)

unique_ids = df_input["idlong"].unique()
masked_records = []

for uid in unique_ids:
    # Pick first and last names deterministically, weighted by original name frequency
    random.seed(str(uid))
    masked_first = random.choices(fnames, weights=first_weights, k=1)[0]

    random.seed(str(uid) + "_L")
    masked_last = random.choices(lnames, weights=last_weights, k=1)[0]

    masked_records.append({
        "idlong": uid,
        "masked_firstname": masked_first,
        "masked_lastname": masked_last
    })

df_masked_map = pd.DataFrame(masked_records)
print(f"   → Created masked names for {len(df_masked_map):,} unique individuals")

# 5. Merge back into synthetic dataset
print("\n[6] Merging masked names into synthetic dataset...")

df_output = df_input.merge(df_masked_map, on="idlong", how="left")

if "pseudo_idlong" in df_output.columns:
    pseudo_idx = df_output.columns.get_loc("pseudo_idlong")
    before_cols = df_output.columns[:pseudo_idx + 1].tolist()
    after_cols = df_output.columns[pseudo_idx + 1:].tolist()
    new_order = before_cols + ["masked_firstname", "masked_lastname"] + \
                [c for c in after_cols if c not in ["masked_firstname", "masked_lastname"]]
    df_output = df_output[new_order]
else:
    df_output = df_output[[c for c in df_output.columns if c not in ["masked_firstname", "masked_lastname"]] +
                          ["masked_firstname", "masked_lastname"]]

# 6. Summary statistics
print("\n[7] Summary of masked name generation...")
unique_first = df_output["masked_firstname"].nunique()
unique_last = df_output["masked_lastname"].nunique()
print(f"   → Unique masked firstnames: {unique_first}")
print(f"   → Unique masked lastnames: {unique_last}")

print("\nSample masked firstnames:", random.sample(df_output["masked_firstname"].unique().tolist(), min(10, unique_first)))
print("Sample masked lastnames:", random.sample(df_output["masked_lastname"].unique().tolist(), min(10, unique_last)))

# 7. Save Output
print("\n[8] Saving masked dataset to database...")

try:
    df_output.to_sql(OUTPUT_TABLE, engine, schema=SCHEMA_NAME, if_exists="replace", index=False)
    print(f"✅ Masked dataset saved successfully as {SCHEMA_NAME}.{OUTPUT_TABLE}")
    print(f"   → Total records written: {len(df_output):,}")
except Exception as e:
    print(f"❌ Error saving masked dataset: {e}")
    exit(1)

print("\n🎉 Deterministic name masking completed successfully!")
