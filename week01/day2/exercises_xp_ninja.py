# Exercise 3: Predict the Output
print(3 <= 3 < 9)  # True

print(3 == 3 == 3)  # True

print(bool(0))  # False

print(bool(5 == "5"))  # False

print(bool(4 == 4) == bool("4" == "4"))  # True

print(bool(bool(None)))  # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)  # True
print("y is", y)  # False
print("a:", a)  # 5
print("b:", b)  # 10


# Exercise 4: Count Characters in a String
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print("Number of characters in my_text:", len(my_text))


# Exercise 5: Longest Sentence Without "A"
longest_sentence = ""

while True:
    user_sentence = input("Enter the longest sentence you can without the letter 'A': ")

    if "a" in user_sentence.lower():
        print("Your sentence contains 'A'. Try again.")
        continue

    if len(user_sentence) > len(longest_sentence):
        longest_sentence = user_sentence
        print("Congratulations! New longest sentence recorded!")

    print(f"Current longest sentence: {longest_sentence}")