import random  # Import shuffle function for the bonus step

# Step 1: Ask the user for a string of exactly 10 characters
user_input = input("Enter a string of exactly 10 characters: ")

# Step 2: Check the length of the string
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string!")

    # Step 3: Print the first and last characters
    print("\nFirst and last character:")
    print(user_input[0])  # First character
    print(user_input[-1])  # Last character

    # Step 4: Print the string character by character
    print("\nBuilding the string character by character:")
    for i in range(1, len(user_input) + 1):
        print(user_input[:i])  # Print progressively longer substrings

    # Bonus: Shuffle the string and print it
    shuffled_string = list(user_input)  # Convert string to list
    random.shuffle(shuffled_string)  # Shuffle the characters
    shuffled_string = ''.join(shuffled_string)  # Convert list back to string

    print("\nJumbled string:")
    print(shuffled_string)
