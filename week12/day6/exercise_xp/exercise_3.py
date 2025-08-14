# exercise_3.py
# Load an Excel file, filter rows where Sales > 1000, and write filtered data back into the same file.

from pathlib import Path
import sys
import shutil
import pandas as pd

# ==== CONFIG ====
EXCEL_FILENAME = "data.xlsx"   # Put this file next to the script
SOURCE_SHEET = 0                # 0 = first sheet; or use a string like "Sheet1"
OUTPUT_SHEET = "Filtered"       # The sheet we will write/replace with results
SALES_COL_NAME = "Sales"        # Column to filter on (case-insensitive match)

# ==== RESOLVE PATHS ====
here = Path(__file__).parent
excel_path = here / EXCEL_FILENAME

if not excel_path.exists():
    sys.exit(f"ERROR: Excel file not found at {excel_path}. "
             f"Place your workbook beside this script or update EXCEL_FILENAME.")

# ==== BACKUP (safety) ====
backup_path = excel_path.with_name(excel_path.stem + ".backup.xlsx")
try:
    shutil.copy2(excel_path, backup_path)
    print(f"Backup created: {backup_path}")
except Exception as e:
    print(f"WARNING: Could not create backup: {e}")

# ==== LOAD ====
try:
    df = pd.read_excel(excel_path, sheet_name=SOURCE_SHEET)
except Exception as e:
    sys.exit(f"ERROR reading Excel: {e}")

if df.empty:
    sys.exit("ERROR: The source sheet is empty.")

# ==== FIND 'Sales' COLUMN (case-insensitive, tolerant of spaces) ====
def normalize(col: str) -> str:
    return "".join(col.split()).lower()

norm_cols = {normalize(c): c for c in df.columns}
target_key = normalize(SALES_COL_NAME)

if target_key not in norm_cols:
    # Try to guess a sales-like column (e.g., 'sales_amount')
    candidates = [c for k, c in norm_cols.items() if "sales" in k]
    if not candidates:
        sys.exit(f"ERROR: Could not find a '{SALES_COL_NAME}' column. "
                 f"Columns present: {list(df.columns)}")
    sales_col = candidates[0]
    print(f"NOTE: Using detected column: '{sales_col}'")
else:
    sales_col = norm_cols[target_key]

# Ensure numeric for comparison
df[sales_col] = pd.to_numeric(df[sales_col], errors="coerce")

# ==== FILTER ====
filtered = df[df[sales_col] > 1000].copy()

print(f"Rows in source: {len(df)}")
print(f"Rows with {sales_col} > 1000: {len(filtered)}")

# ==== WRITE BACK (same file, replace/creates 'Filtered' sheet) ====
try:
    with pd.ExcelWriter(
        excel_path,
        engine="openpyxl",
        mode="a",                   # append to existing workbook
        if_sheet_exists="replace"   # replace the Filtered sheet if it exists
    ) as writer:
        filtered.to_excel(writer, sheet_name=OUTPUT_SHEET, index=False)
    print(f"Filtered data written to sheet: '{OUTPUT_SHEET}' in {excel_path.name}")
except FileNotFoundError:
    # If the file didn't exist (unlikely here), write a new one
    with pd.ExcelWriter(excel_path, engine="openpyxl", mode="w") as writer:
        filtered.to_excel(writer, sheet_name=OUTPUT_SHEET, index=False)
    print(f"Workbook created and filtered data written to '{OUTPUT_SHEET}'.")
except Exception as e:
    sys.exit(f"ERROR writing Excel: {e}")
