# week 1 day 4 - python exercises

# excercise 1 - faveourite numbers
my_fav_numbers = {4, 29, 7, 13}

my_fav_numbers.add(5)
my_fav_numbers.add(7)

my_fav_numbers.remove(7)

friend_fav_numbers = {5, 87, 92}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("My fovourite numbers:", my_fav_numbers)
print("Friend's fovourite numbers:", friend_fav_numbers)
print("Our fovourite numbers:", our_fav_numbers)


# excercise 2 - tuples
# we can't add elements to a tuple because they are immutable


#excercise 3 - lists
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print("Final basket:", basket)  # Should be an empty list
print(f"Number of apples before clearing: {apple_count}")

# excercise 4 - floats
# floats are numbers with decimal points, Integers are whole numbers

float_sequence = [x * 0.5 for x in range(3, 11)]
print("Generated float sequence:", float_sequence)

# excercise 5 - for loop
print("Numbers from 1 to 20:")
for num in range(1, 21):
    print(num, end=" ")
print("\n")
print("Numbers with an even index:")
for num in range(1, 21, 2):
    print(num, end=" ")

# excercise 6 - while loop
my_name = "Reuven" 
while True:
    user_name = input("Enter your name: ")
    if user_name == my_name:
        print("That's my name too! Exiting loop.")
        break
    else:
        print("That's not my name, try again!")

# excercise 7 - favourite fruits
fav_fruits = input("Enter your favorite fruits (separated by spaces): ").split()
fruit_check = input("Enter a fruit name: ")
if fruit_check in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")

# excercise 8 - who ordered a pizza
toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip().lower()
    if topping == "quit":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza!")
total_price = 10 + len(toppings) * 2.5
print("\nYour pizza toppings:", toppings)
print(f"Total price: ${total_price:.2f}")

# excercise 9 - cinemax
ages = input("Enter the ages of all family members separated by spaces: ").split()
ages = [int(age) for age in ages]
total_cost = 0
for age in ages:
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
print(f"Total cost for the family: ${total_cost}")
teen_names = ["Jake", "Emma", "Lucas", "Sophia"]  
allowed_teens = []

for teen in teen_names:
    age = int(input(f"Enter the age of {teen}: "))
    if 16 <= age <= 21:
        print(f"{teen} is not allowed to watch this movie.")
    else:
        allowed_teens.append(teen)
print("Final list of teenagers who can watch the movie:", allowed_teens)

# excercise 10 - sandwich orders
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich.lower()}")
    finished_sandwiches.append(sandwich)
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
