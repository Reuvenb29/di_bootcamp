from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text
        self.words = text.lower().split()

    def word_frequency(self, word):
        word = word.lower()
        count = self.words.count(word)
        return count if count > 0 else f"'{word}' does not appear in the text."

    def most_common_word(self):
        count = Counter(self.words)
        return count.most_common(1)[0][0]

    def unique_words(self):
        return list(set(self.words))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)

if __name__ == "__main__":
    # Part I (comment out as neccersary for testing)
   
    print("--- Hardcoded Text Test ---")
    text = Text("A good book would sometimes cost as much as a good house.")
    print("Frequency of 'good':", text.word_frequency("good"))
    print("Most common word:", text.most_common_word())
    print("Unique words:", text.unique_words())

    # Part II 
    print("\n--- The Stranger Text Analysis ---")
    stranger = Text.from_file("the_stranger.txt")
    print("Frequency of 'the':", stranger.word_frequency("the"))
    print("Most common word:", stranger.most_common_word())
    print("Number of unique words:", len(stranger.unique_words()))
