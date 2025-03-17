from datetime import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Ask the user for their birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert string input to a datetime object
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

# Get the current year
current_year = datetime.now().year

# Calculate age
age = current_year - birthdate.year

# If they haven't had their birthday this year, subtract one
if (datetime.now().month, datetime.now().day) < (birthdate.month, birthdate.day):
    age -= 1

# Determine the number of candles (last digit of age)
candles = age % 10

# Define the cake template
cake_top = f"       {'i' * candles}       "
cake_body = """
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# Display the cake (twice if leap year)
if is_leap_year(birthdate.year):
    print("🎉 You were born in a leap year! Here's two cakes! 🎂🎂")
    print(cake_top + cake_body)
    print(cake_top + cake_body)
else:
    print(cake_top + cake_body)
