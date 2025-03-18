#exercise1
from datetime import datetime

# Step 1: Calculate Age
# Updated to accept user input as dd/mm/yyyy

def get_age(day, month, year):
    current_year = 2025
    current_month = 3  # Hardcoded as March
    current_day = 17   # Hardcoded as 17th

    age = current_year - year

    # If the current month/day is before the user's birth month/day, subtract 1
    if (month > current_month) or (month == current_month and day > current_day):
        age -= 1

    return age

# Step 2: Check Retirement Eligibility
# Men retire at 67, women retire at 62

def can_retire(gender, date_of_birth):
    # Expecting date_of_birth in dd/mm/yyyy format
    day, month, year = map(int, date_of_birth.split('/'))
    age = get_age(day, month, year)

    if (gender == 'm' and age >= 67) or (gender == 'f' and age >= 62):
        return True
    return False

# Step 3: Ask for User Input
# Note: We now expect dd/mm/yyyy

gender = input("Enter your gender (m/f): ").strip().lower()
dob = input("Enter your date of birth (dd/mm/yyyy): ").strip()

if can_retire(gender, dob):
    print("Congratulations! You can retire.")
else:
    print("Sorry, you are not eligible for retirement yet.")

#exercise2
def calculate_sum(x):
    x_str = str(x)  # Convert to string
    return int(x_str) + int(x_str * 2) + int(x_str * 3) + int(x_str * 4)

# Test the function
x = int(input("Enter a number: "))
print(f"Result: {calculate_sum(x)}")

#exercise3
import random

def throw_dice() -> int:
    return random.randint(1, 6)

def throw_until_doubles() -> int:
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            return count

def main() -> None:
    results = [throw_until_doubles() for _ in range(100)]
    total_throws = sum(results)
    average_throws = round(total_throws / 100, 2)
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws}")

if __name__ == "__main__":
    main()
