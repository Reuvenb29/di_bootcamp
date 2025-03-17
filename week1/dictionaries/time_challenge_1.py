# Step 1: Take user input
reverse_inp = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = reverse_inp.split()

# Step 3: Reverse the order of words
reversed_sentence = " ".join(words[::-1])

# Step 4: Print the result
print(reversed_sentence)
