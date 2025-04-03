# --- Exercise 
# currency ---
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError("Unsupported addition type")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError("Unsupported addition type")
        return self

#  Test cases for Currency class

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)

# Print string representation
print(str(c1))      # '5 dollars'
print(int(c1))      # 5
print(repr(c1))     # '5 dollars'

# Addition with int
print(c1 + 5)       # 10

# Addition with same currency
print(c1 + c2)      # 15

# In-place addition
c1 += 5
print(c1)           # 10 dollars

c1 += c2
print(c1)           # 20 dollars

# Try adding different currencies (this will raise an error)
try:
    print(c1 + c3)
except TypeError as e:
    print(e)

# exercises.py

# --- Exercise 2 ---
from func import add_numbers

# Call the function with two numbers
add_numbers(5, 10)

# --- Exercise 3 ---
import string
import random

def generate_random_string(length=5):
    characters = string.ascii_letters  # a-z + A-Z
    result = ''.join(random.choices(characters, k=length))
    print("Random string:", result)

generate_random_string()

# --- Exercise 4 ---
from datetime import datetime

def show_current_date():
    today = datetime.now().date()  # Get only the date part
    print("Today's date is:", today)

show_current_date()

# --- Exercise 5 ---

def time_until_january_first():
    now = datetime.now()
    next_jan = datetime(year=now.year + 1, month=1, day=1)
    time_left = next_jan - now

    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60

    print(f"January 1st is in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

time_until_january_first()

# --- Exercise 6 ---
from datetime import datetime

def minutes_lived(birthdate_str):
    # Convert input string to a datetime object
    birth_date = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    minutes = int((now - birth_date).total_seconds() / 60)

    print(f"You have lived for about {minutes:,} minutes.")

# Example usage (mybday)
minutes_lived("2000-02-29")

# --- Exercise 7 ---
from faker import Faker

fake = Faker()
users = []

def add_fake_user():
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users.append(user)

# Create 5 fake users
for _ in range(5):
    add_fake_user()

# Print them out
for user in users:
    print(user)
    print()  # Extra line for readability
