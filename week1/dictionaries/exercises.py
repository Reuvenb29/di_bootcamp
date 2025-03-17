#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

#exercise 2
print("\nBonus: User Input Version")

family = {}  # Empty dictionary
num_members = int(input("How many family members? "))

for _ in range(num_members):
    name = input("Enter name: ").strip()
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age  # Add to dictionary

total_cost = 0

for person, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{person.capitalize()} pays: ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")
