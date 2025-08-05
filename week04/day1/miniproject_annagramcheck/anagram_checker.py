# anagram_checker.py

class AnagramChecker:
    def __init__(self):
        # Load the word list into memory
        with open('sowpods.txt', 'r') as file:
            self.word_list = [line.strip().upper() for line in file]

    def is_valid_word(self, word):
        # Check if the word exists in the list
        return word.upper() in self.word_list

    def is_anagram(self, word1, word2):
        # Check if two words are anagrams
        return sorted(word1.upper()) == sorted(word2.upper())

    def get_anagrams(self, word):
        # Get all anagrams from the list, excluding the word itself
        word = word.upper()
        return [
            candidate.lower()
            for candidate in self.word_list
            if candidate != word and self.is_anagram(word, candidate)
        ]
