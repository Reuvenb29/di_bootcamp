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

def remove_employee():
    employees = load_employees()
    if not employees:
        print("\n⚠️ No employees to remove.\n")
        return

    print("\n=== Employees ===")
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. {emp['name']} - {emp['job']} - {emp['email']}")

    try:
        choice = int(input("\nEnter the number of the employee to remove: "))
        if 1 <= choice <= len(employees):
            removed = employees.pop(choice - 1)
            with open("employees.json", "w") as file:
                import json
                json.dump(employees, file, indent=4)
            print(f"\n✅ Removed {removed['name']} successfully!\n")
        else:
            print("\n❌ Invalid number entered.\n")
    except ValueError:
        print("\n❌ Please enter a valid number.\n")

def main():
    while True:
        print("\n=== Fake Employee Manager ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Remove Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            remove_employee()
        elif choice == '4':
            print("\n👋 Exiting. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
