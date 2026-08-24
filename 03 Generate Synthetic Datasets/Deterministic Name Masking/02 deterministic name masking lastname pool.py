#############
##This Python script extracts last-name data from an Excel spreadsheet, processes and
# deduplicates it, and uploads the final dataset into a PostgreSQL database.
#############

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import sys

# --- USER INPUTS ---
excel_file = r'D:\Deterministic Masking\Pool Name List.xlsx'
sheet_name = 'LastNames'   # <-- Sheet with last names

# Database connection details
db_user = 'postgres'
db_host = 'localhost'
db_port = 5432
db_name = 'PhD'
db_pass = 'password1234'   # <-- STATIC PASSWORD
# -------------------

print("\n\n" + "=" * 70)
print("PostgreSQL Data Upload Script — Load LastNames\n")
print("=" * 70 + "\n\n")
print(f"Database: {db_name} | Host: {db_host} | User: {db_user}")
print("=" * 70)

# --- VERIFY CONNECTION ---
try:
    print("[1] Attempting to connect to database...")
    engine = create_engine(
        f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    )
    with engine.connect() as conn:
        conn.execute(text("SELECT 1;"))
    print("[2] ✅ Database connection successful!\n")
except OperationalError:
    print("❌ Database connection failed. Please check credentials or PostgreSQL service.")
    sys.exit(1)
except Exception as e:
    print("❌ Unexpected error during connection:", e)
    sys.exit(1)

# --- LOAD EXCEL ---
try:
    print("[3] Loading Excel file...")
    df = pd.read_excel(excel_file, sheet_name=sheet_name, dtype=str, engine='openpyxl')
    df.columns = [c.strip().lower() for c in df.columns]  # normalize column names
    print(f"[4] ✅ Excel sheet '{sheet_name}' loaded successfully with {len(df)} rows.")
    print(f"    Available columns: {list(df.columns)}\n")
except Exception as e:
    print("❌ Error reading Excel file:", e)
    sys.exit(1)

# --- PROCESS DATA ---
try:
    print("[5] Processing DataFrame...")

    # Detect the lastname column (case-insensitive)
    lastname_col = None
    for col in df.columns:
        if "last" in col and "name" in col:
            lastname_col = col
            break

    if lastname_col is None:
        raise ValueError("Could not find a 'lastname' column in the Excel sheet!")

    num_read = len(df)

    # Deduplicate by detected lastname column
    df_unique = df.drop_duplicates(subset=[lastname_col]).reset_index(drop=True)
    num_unique = len(df_unique)
    num_dropped = num_read - num_unique

    print(f"    - Using column '{lastname_col}' for last names.")
    print(f"    - Unique lastnames: {num_unique}")
    print(f"    - Duplicates dropped: {num_dropped}")

    # Shuffle and add recnr
    df_shuffled = df_unique.sample(frac=1, random_state=42).reset_index(drop=True)
    df_shuffled['recnr'] = range(1, len(df_shuffled) + 1)

    # Identify optional columns
    final_cols = ['recnr', lastname_col]
    for optional_col in ['origin', 'source']:
        if optional_col in df_shuffled.columns:
            final_cols.append(optional_col)

    df_final = df_shuffled[final_cols]
    print(f"[6] ✅ Data prepared for upload with columns: {final_cols}\n")

except Exception as e:
    print("❌ Error processing DataFrame:", e)
    sys.exit(1)

# --- WRITE TO DATABASE ---
try:
    print("[7] Checking/creating schema 'synthetic_data_final'...")
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS synthetic_data_final;"))
    print("[8] ✅ Schema ready.\n")

    print("[9] Uploading DataFrame to PostgreSQL...")
    df_final.to_sql(
        name='deterministic_lastname_pool',
        con=engine,
        schema='synthetic_data_final',
        index=False,
        if_exists='replace'
    )
    print(f"[10] ✅ Successfully uploaded {len(df_final)} rows to 'synthetic_data_final.deterministic_lastname_pool' in database '{db_name}'.")
except Exception as e:
    print("❌ Error writing to PostgreSQL:", e)
    sys.exit(1)
