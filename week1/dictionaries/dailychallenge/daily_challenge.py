#challenge 1
print("\nChallenge 1: Letter Index Dictionary")

# Ask for a word
word = input("Enter a word: ").lower()

# Create dictionary to store indexes
letter_dict = {}

for index, letter in enumerate(word):
    if letter not in letter_dict:
        letter_dict[letter] = []
    letter_dict[letter].append(index)

print("Result:", letter_dict)

#challenge 2
print("\nChallenge 2: What Can You Afford?")

# Store items with prices
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# Convert wallet amount to a number
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# Find affordable items
affordable_items = []

for item, price in items_purchase.items():
    item_price = int(price.replace("$", "").replace(",", ""))
    if item_price <= wallet_amount:
        affordable_items.append(item)

# Sort alphabetically
affordable_items.sort()

# Print result
print("Affordable items:", affordable_items if affordable_items else "Nothing")
