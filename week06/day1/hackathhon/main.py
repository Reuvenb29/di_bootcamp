# main.py

from database import save_employee, load_employees
from faker import Faker

fake = Faker()

def add_employee():
    employee = {
        'name': fake.name(),
        'job': fake.job(),
        'email': fake.email()
    }
    save_employee(employee)
    print("\n✅ Employee added successfully!\n")

def view_employees():
    employees = load_employees()
    if not employees:
        print("\n⚠️ No employees found.\n")
        return
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. {emp['name']} - {emp['job']} - {emp['email']}")

def main():
    while True:
        print("\n=== Fake Employee Manager ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            print("\n👋 Exiting. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
