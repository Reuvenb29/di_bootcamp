import re

# Exercise: Define the matrix as a 2D list
matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# Step 1: Read column by column
rows = len(matrix)
cols = len(matrix[0])

decoded_text = ""

for col in range(cols):
    for row in range(rows):
        decoded_text += matrix[row][col]

# Step 2: Replace non-alphabetic groups between letters with a space
clean_text = re.sub(r'[^a-zA-Z]+', ' ', decoded_text)

# Step 3: Trim unnecessary spaces and print the message
decoded_message = clean_text.strip()
print(decoded_message)
