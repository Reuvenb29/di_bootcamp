# database.py

import json
import os

FILE_PATH = "employees.json"

def load_employees():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_employee(employee):
    employees = load_employees()
    employees.append(employee)
    with open(FILE_PATH, "w") as file:
        json.dump(employees, file, indent=4)

