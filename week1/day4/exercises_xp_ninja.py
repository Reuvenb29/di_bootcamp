import math

# Exercise 1: Formula Calculation
C = 50
H = 30

# Get user input
D_values = input("Enter comma-separated numbers: ").split(",")

# Calculate Q for each D
results = [str(int(math.sqrt((2 * C * int(D)) / H))) for D in D_values]

# Print results as a comma-separated string
print(",".join(results))

import random

# Exercise 2: List Analysis
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]  # Example list

# Printing results
print("Numbers:", numbers)
print("Sorted (Descending):", sorted(numbers, reverse=True))
print("Sum of numbers:", sum(numbers))
print("First and last number:", [numbers[0], numbers[-1]])
print("Numbers greater than 50:", [num for num in numbers if num > 50])
print("Numbers smaller than 10:", [num for num in numbers if num < 10])
print("Squared numbers:", [num**2 for num in numbers])
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers, "Total:", len(unique_numbers))
print("Average:", sum(numbers) / len(numbers))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# Bonus: Generate a list of 10 random numbers between -100 and 100
random_numbers = [random.randint(-100, 100) for _ in range(10)]
print("Randomly generated numbers:", random_numbers)

import string

# Exercise 3: Paragraph Analysis
paragraph = """Python is a widely used high-level programming language. 
It was created by Guido van Rossum and first released in 1991. Python's design philosophy 
emphasizes code readability and ease of use."""

# Character count
char_count = len(paragraph)

# Sentence count
sentence_count = paragraph.count(".") + paragraph.count("?") + paragraph.count("!")

# Word count
words = paragraph.split()
word_count = len(words)

# Unique word count
unique_words = set(words)
unique_word_count = len(unique_words)

# Bonus: Non-whitespace character count
non_whitespace_count = len(paragraph.replace(" ", "").replace("\n", ""))

# Bonus: Words per sentence (approximate)
words_per_sentence = word_count / sentence_count if sentence_count else 0

# Bonus: Non-unique words
non_unique_count = word_count - unique_word_count

# Print results
print(f"Characters: {char_count}")
print(f"Sentences: {sentence_count}")
print(f"Words: {word_count}")
print(f"Unique Words: {unique_word_count}")
print(f"Non-whitespace Characters: {non_whitespace_count}")
print(f"Average Words per Sentence: {words_per_sentence:.2f}")
print(f"Non-unique Words: {non_unique_count}")

# Exercise 4: Word Frequency Count
sentence = input("Enter a sentence: ")

# Convert sentence into a list of words
words = sentence.split()

# Count word occurrences
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Print sorted results
for word, count in sorted(word_freq.items()):
    print(f"{word}:{count}")
