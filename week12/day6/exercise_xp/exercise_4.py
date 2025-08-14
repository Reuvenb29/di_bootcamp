# exercise_4.py
# Reads product sales data, groups by product, plots chart, writes report to Excel.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# ==== CONFIG ====
INPUT_FILE = "productSales.xlsx"
OUTPUT_FILE = "sales_report.xlsx"
PRODUCT_COL = "product"
SALES_COL = "sales"

# ==== RESOLVE PATHS ====
here = Path(__file__).parent
input_path = here / INPUT_FILE
output_path = here / OUTPUT_FILE

if not input_path.exists():
    sys.exit(f"ERROR: Input file not found: {input_path}")

# ==== READ DATA ====
try:
    df = pd.read_excel(input_path)
except Exception as e:
    sys.exit(f"ERROR reading Excel file: {e}")

if df.empty:
    sys.exit("ERROR: Input file is empty.")

# ==== CLEAN COLUMN NAMES ====
df.columns = [c.strip().lower() for c in df.columns]
if PRODUCT_COL not in df.columns or SALES_COL not in df.columns:
    sys.exit(f"ERROR: Required columns '{PRODUCT_COL}' and '{SALES_COL}' not found. "
             f"Columns present: {list(df.columns)}")

# ==== GROUP & SUM ====
grouped = df.groupby(PRODUCT_COL, as_index=False)[SALES_COL].sum()

print("\nGrouped sales data:")
print(grouped)

# ==== PLOT CHART ====
plt.figure(figsize=(8, 5))
plt.bar(grouped[PRODUCT_COL], grouped[SALES_COL], color="skyblue")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as PNG (optional)
chart_path = here / "sales_chart.png"
plt.savefig(chart_path)
print(f"\nChart saved as: {chart_path}")

# ==== EXPORT TO EXCEL ====
try:
    with pd.ExcelWriter(output_path, engine="openpyxl", mode="w") as writer:
        grouped.to_excel(writer, index=False, sheet_name="Summary")
        writer.save()
        writer.close()
    print(f"\nSales report written to: {output_path}")
except Exception as e:
    sys.exit(f"ERROR writing Excel file: {e}")
