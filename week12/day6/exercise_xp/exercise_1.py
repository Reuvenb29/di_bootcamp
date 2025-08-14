# calculator_excel.py
from openpyxl import Workbook

# Create a new workbook and select active sheet
wb = Workbook()
ws = wb.active
ws.title = "Calculator"

# Add headers
ws.append(["Number 1", "Operator", "Number 2", "Result"])

# Add rows with values and formulas
ws.append([5, "+", 3, "=A2+C2"])
ws.append([8, "-", 2, "=A3-C3"])
ws.append([4, "*", 6, "=A4*C4"])
ws.append([10, "/", 2, "=A5/C5"])

# Save the workbook
wb.save("calculator.xlsx")

print("calculator.xlsx created successfully")
