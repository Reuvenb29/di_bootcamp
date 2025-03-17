#exercise 1

# Step 1: Define a dictionary with birthdays
birthdays = {
    "Alice": "1995/07/21",
    "Bob": "1988/12/05",
    "Charlie": "1993/06/10",
    "Dana": "2000/03/15",
    "Eli": "1999/09/30"
}

# Step 2: Welcome message
print("Welcome to the Birthday Look-up!")
print("You can look up the birthdays of the people in the list.")

# Step 3: Ask the user for a name
name = input("Enter a person's name: ")

# Step 4: Print the birthday if found
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

#exercise 2
# Step 1: Define a dictionary with birthdays
birthdays = {
    "Alice": "1995/07/21",
    "Bob": "1988/12/05",
    "Charlie": "1993/06/10",
    "Dana": "2000/03/15",
    "Eli": "1999/09/30"
}

# Step 2: Welcome message & display all names
print("Welcome to the Birthday Look-up!")
print("Here are the people you can look up:")
for name in birthdays.keys():
    print(name)

# Step 3: Ask the user for a name
name = input("\nEnter a person's name: ")

# Step 4: Check if the name exists in the dictionary
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

#exercise 3
# Step 1: Define a dictionary with birthdays
birthdays = {
    "Alice": "1995/07/21",
    "Bob": "1988/12/05",
    "Charlie": "1993/06/10",
    "Dana": "2000/03/15",
    "Eli": "1999/09/30"
}

# Step 2: Welcome message & display all names
print("Welcome to the Birthday Look-up!")
print("Here are the people you can look up:")
for name in birthdays.keys():
    print(name)

# Step 3: Allow the user to add a new birthday
new_name = input("\nEnter a new person's name: ")
new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")
birthdays[new_name] = new_birthday

print(f"{new_name}'s birthday has been added!")

# Step 4: Ask the user for a name to look up
name = input("\nEnter a person's name to look up: ")

# Step 5: Check if the name exists in the dictionary
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

#exercise 4
# Step 1: Define the dictionary with item prices
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Step 2: Print all items and their prices
print("Available fruits and their prices:")
for fruit, price in items.items():
    print(f"- {fruit.capitalize()}: ${price}")

# Step 3: Define dictionary with stock information
items_stock = {
    "banana": {"price": 4 , "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5 , "stock": 24},
    "pear": {"price": 3 , "stock": 1}
}

# Step 4: Calculate total value of all stock
total_value = sum(item["price"] * item["stock"] for item in items_stock.values())

print(f"\nTotal cost to buy everything in stock: ${total_value:.2f}")
