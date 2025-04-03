# --- Exercise 1
# currencies


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # String representation
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

    def __int__(self):
        # Allows conversion to int
        return self.amount

    def __repr__(self):
        # Developer-friendly representation, here we'll keep it similar to __str__
        return self.__str__()

    def __add__(self, other):
        # Adding int or another Currency
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
        return NotImplemented

    def __iadd__(self, other):
        # In-place add
        if isinstance(other, int):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
        return NotImplemented

# Example usage:
if __name__ == "__main__":
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(str(c1))       # '5 dollars'
    print(int(c1))       # 5
    print(repr(c1))      # '5 dollars'
    print(c1 + 5)        # 10
    print(c1 + c2)       # 15
    print(c1)            # '5 dollars'

    c1 += 5
    print(c1)            # '10 dollars'
    c1 += c2
    print(c1)            # '20 dollars'

    # This will raise TypeError
    # c1 + c3


# --- Exercise 2
# import ---

def sum_two_numbers(3, 5):
    print(3 + 5)

from func import sum_two_numbers
sum_two_numbers(5, 10)


# --- Exercise 3
# string module ---

import string
import random

def random_string_of_length_5():
    letters = string.ascii_letters  # Includes uppercase and lowercase
    result = ''.join(random.choice(letters) for _ in range(5))
    return result

print(random_string_of_length_5())


# --- Exercise 4
# current date ---
from datetime import datetime

def display_current_date():
    now = datetime.now()
    print(f"Today's date is: {now.strftime('%Y-%m-%d')}")

display_current_date()

# --- Exercise 5
# time left till jan
from datetime import datetime

def time_until_jan_first():
    now = datetime.now()
    # Decide the year for the next Jan 1
    next_year = now.year + 1 if now.month == 12 and now.day > 31 else now.year + 1
    jan_first = datetime(year=next_year, month=1, day=1)
    delta = jan_first - now
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    print(f"The 1st of January is in {days} days and {hours}:{minutes}:{secs} hours.")

time_until_jan_first()

# --- Exercise 6
# birthday and min ---

from datetime import datetime

def minutes_lived(birthdate_str):
    # Assume birthdate_str is in format 'YYYY-MM-DD'
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    now = datetime.now()
    diff = now - birthdate
    diff_minutes = diff.total_seconds() / 60
    print(f"You have lived {diff_minutes:.0f} minutes so far.")


# --- Exercise 7
# faker mod ---

from faker import Faker

fake = Faker()
users = []

def add_fake_user(users_list, n=1):
    for _ in range(n):
        user_info = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users_list.append(user_info)

add_fake_user(users, 3)
print(users)
