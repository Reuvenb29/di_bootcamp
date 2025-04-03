# Exercise 1 – Random Sentence Generator
import random

# Function to get words from file
def get_words_from_file():
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()  # Read and split into a list of words
            return words
    except FileNotFoundError:
        print("Error: words.txt file not found.")
        return []

# Function to generate a random sentence
def get_random_sentence(length):
    words = get_words_from_file()
    if not words:
        return "No words available."
    sentence = random.sample(words, length)  # Pick random words
    return ' '.join(sentence).lower()  # Join and convert to lowercase

# Main function to interact with the user
def main():
    print("Welcome to the Random Sentence Generator!")
    print("You will get a random sentence with a length between 2 and 20 words.")

    try:
        length = int(input("Enter the number of words for your sentence (2-20): "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("Here is your random sentence:")
            print(sentence)
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

# Run the program
main()

# Exercise 2 – Working with JSON
import json

# Original JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Convert string to dictionary
data = json.loads(sampleJson)

# Step 2: Access and print the salary
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Ask user for birth_date and add it to the dictionary
birth_date = input("Enter birth date for the employee (YYYY-MM-DD): ")
data["company"]["employee"]["birth_date"] = birth_date

# Step 4: Save the updated dictionary to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Updated JSON with birth_date saved to data.json ")