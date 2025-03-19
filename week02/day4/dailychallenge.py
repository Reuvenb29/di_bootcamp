#challenge1
def sort_words_alphabetically(input_str):
    # 1 & 2: Split the string by commas
    # 3: Strip extra spaces
    words = [word.strip() for word in input_str.split(',')]
    
    # 4: Sort the list
    sorted_words = sorted(words)
    
    # 5 & 6: Join the sorted list and return or print
    return ",".join(sorted_words)

if __name__ == "__main__":
    input_str = input("Enter a comma-separated list of words: ")
    result = sort_words_alphabetically(input_str)
    print(result)

#challenge2
def longest_word(sentence):
    words = sentence.split()  # Split sentence into words
    longest = max(words, key=len)  # Find the longest word based on length
    return longest  # Return the longest word

# Ask the user for input
user_input = input("Enter a sentence: ")

# Call the function and print the result
print("Longest word:", longest_word(user_input))
