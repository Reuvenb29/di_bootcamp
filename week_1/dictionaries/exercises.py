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

#exercise 3
print("\nExercise 3: Zara")

# Step 1: Create the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Step 2: Modify the dictionary

# 3. Change the number of stores to 2
brand["number_stores"] = 2

# 4. Print who Zara’s clients are
print(f"Zara's clients include: {', '.join(brand['type_of_clothes'])}")

# 5. Add a key called "country_creation" with value "Spain"
brand["country_creation"] = "Spain"

# 6. Check if "international_competitors" exists, then add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 7. Delete "creation_date"
del brand["creation_date"]

# 8. Print the last international competitor
print("Last international competitor:", brand["international_competitors"][-1])

# 9. Print the major clothes colors in the US
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))

# 10. Print the number of key-value pairs in the dictionary
print("Total key-value pairs:", len(brand))

# 11. Print all keys in the dictionary
print("Keys in dictionary:", list(brand.keys()))

# 12. Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 13. Merge more_on_zara into brand
brand.update(more_on_zara)

# 14. Print the updated "number_stores" value
print("Updated number of stores:", brand["number_stores"])

#exercise 4
print("\nExercise 4: Disney Characters")

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {name: index for index, name in enumerate(users)}
print("Dictionary A:", disney_users_A)

disney_users_B = {index: name for index, name in enumerate(users)}
print("Dictionary B:", disney_users_B)

disney_users_C = {name: index for index, name in enumerate(sorted(users))}
print("Dictionary C (sorted):", disney_users_C)

disney_users_I = {name: index for index, name in enumerate(users) if "i" in name.lower()}
print("Filtered (names containing 'i'):", disney_users_I)

disney_users_MP = {name: index for index, name in enumerate(users) if name.startswith(("M", "P"))}
print("Filtered (starting with 'M' or 'P'):", disney_users_MP)
