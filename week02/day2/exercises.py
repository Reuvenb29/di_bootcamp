import random

# Exercise 1
def display_message():
    print("I am learning Python programming in this course!")

display_message()


# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")


# Exercise 3
def describe_city(city, country="France"):
    print(f"{city} is in {country}.")

describe_city("Paris")  
describe_city("Tokyo", "Japan")  


# Exercise 4
def check_random_number(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success! You guessed the correct number!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

check_random_number(42)  # Replace 42 with any number between 1 and 100


# Exercise 5
def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

make_shirt()  
make_shirt("Medium")  
make_shirt("Small", "Code is Life")  


# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] += " the Great"

make_great(magician_names)  
show_magicians(magician_names)  


# Exercise 7
def get_random_temp(season="spring"):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(10, 25)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(5, 20)

def main():
    season = input("Enter a season (winter, spring, summer, autumn): ").lower()
    temperature = round(get_random_temp(season), 1)
    
    print(f"The temperature right now is {temperature}°C.")
    
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 23:
        print("Nice and cool, perfect weather!")
    elif 24 <= temperature < 32:
        print("Warm and pleasant, enjoy your day!")
    else:
        print("It's really hot! Stay hydrated.")

main()


# Exercise 8
def star_wars_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]

    correct_answers = 0
    wrong_answers = []
    
    for entry in data:
        user_answer = input(entry["question"] + " ").strip()
        if user_answer.lower() == entry["answer"].lower():
            correct_answers += 1
        else:
            wrong_answers.append((entry["question"], user_answer, entry["answer"]))

    print(f"\nYou got {correct_answers} out of {len(data)} correct.")

    if wrong_answers:
        print("\nHere are the ones you got wrong:")
        for question, user_ans, correct_ans in wrong_answers:
            print(f"Q: {question}\nYour Answer: {user_ans}\nCorrect Answer: {correct_ans}\n")

    if len(wrong_answers) > 3:
        print("You got more than 3 wrong! Try again.")
        star_wars_quiz()

star_wars_quiz()
