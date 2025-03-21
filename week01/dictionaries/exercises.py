#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)

#exercise 2
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

brand["number_stores"] = 2
print(f"Zara's clients include: {', '.join(brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print("Last international competitor:", brand["international_competitors"][-1])
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))
print("Total key-value pairs:", len(brand))
print("Keys in dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print("Updated number of stores:", brand["number_stores"])

#exercise 4
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
