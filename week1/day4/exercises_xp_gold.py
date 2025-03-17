# Exercise 1: Concatenate lists without '+'
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)  # Extend list1 with elements from list2

print("Concatenated list:", list1)

# Exercise 2: Print multiples of 5 and 7 from 1500 to 2500
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercise 3: Check name index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    print(f"First occurrence of {user_name} is at index:", names.index(user_name))
else:
    print(f"{user_name} not found in the list.")

# Exercise 4: Greatest Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

greatest = max(num1, num2, num3)

print("The greatest number is:", greatest)

# Exercise 5: Alphabet Vowel/Consonant
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

# Exercise 6: Find letter in words
words = [input(f"Enter word {i+1}: ") for i in range(7)]
letter = input("Enter a single letter: ")

for word in words:
    if letter in word:
        print(f"Letter '{letter}' found in '{word}' at index {word.index(letter)}")
    else:
        print(f"Letter '{letter}' not found in '{word}'.")

# Exercise 7: Min, Max, Sum
numbers = list(range(1, 1_000_001))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

# Exercise 8: Convert input to list & tuple
numbers = input("Enter comma-separated numbers: ").split(",")

num_list = list(numbers)
num_tuple = tuple(numbers)

print("List:", num_list)
print("Tuple:", num_tuple)

import random

# Exercise 9: Guess the Random Number
wins = 0
losses = 0

while True:
    user_guess = input("Guess a number between 1 and 9 (or type 'quit' to stop): ")

    if user_guess.lower() == "quit":
        break

    user_guess = int(user_guess)
    random_number = random.randint(1, 9)

    if user_guess == random_number:
        print("Winner! 🎉")
        wins += 1
    else:
        print(f"Better luck next time! The number was {random_number}")
        losses += 1

print(f"Total Wins: {wins} | Total Losses: {losses}")
