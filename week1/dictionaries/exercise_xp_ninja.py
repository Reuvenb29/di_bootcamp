# Step 1: Define the string of manufacturers
manufacturers_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Step 2: Convert it into a list
manufacturers_list = manufacturers_string.split(", ")

# Step 3: Print the number of manufacturers
print(f"There are {len(manufacturers_list)} manufacturers in the list.")

# Step 4: Print the list in reverse (Z-A)
manufacturers_sorted_desc = sorted(manufacturers_list, reverse=True)
print("\nManufacturers in descending order (Z-A):")
print(manufacturers_sorted_desc)

# Step 5: Count manufacturers with the letter 'o'
count_with_o = sum(1 for manufacturer in manufacturers_list if 'o' in manufacturer.lower())
print(f"\nNumber of manufacturers containing the letter 'o': {count_with_o}")

# Step 6: Count manufacturers without the letter 'i'
count_without_i = sum(1 for manufacturer in manufacturers_list if 'i' not in manufacturer.lower())
print(f"Number of manufacturers without the letter 'i': {count_without_i}")

# Bonus 1: Remove duplicates
manufacturers_with_duplicates = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_manufacturers = list(set(manufacturers_with_duplicates))

# Convert back to a comma-separated string
unique_manufacturers_string = ", ".join(unique_manufacturers)
print(f"\nUnique manufacturers ({len(unique_manufacturers)} companies): {unique_manufacturers_string}")

# Bonus 2: Print manufacturers in ascending order (A-Z) with reversed names
manufacturers_reversed_names = sorted([manufacturer[::-1] for manufacturer in unique_manufacturers])
print("\nManufacturers sorted (A-Z) with reversed names:")
print(manufacturers_reversed_names)
