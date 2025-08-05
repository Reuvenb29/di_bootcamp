# anagrams.py

from anagram_checker import AnagramChecker

def clean_input(word):
    word = word.strip()
    if not word.isalpha():
        return None
    if len(word.split()) > 1:
        return None
    return word

def main():
    checker = AnagramChecker()

    while True:
        print("\n--- Anagram Checker ---")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == '2':
            print("Goodbye!")
            break
        elif choice != '1':
            print("Invalid choice. Try again.")
            continue

        user_word = input("Enter a single English word: ")
        cleaned_word = clean_input(user_word)

        if not cleaned_word:
            print("Invalid input. Only one word with alphabetic letters is allowed.")
            continue

        cleaned_word = cleaned_word.upper()

        print(f"\nYOUR WORD: \"{cleaned_word}\"")

        if checker.is_valid_word(cleaned_word):
            print("This is a valid English word.")
            anagrams = checker.get_anagrams(cleaned_word)
            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print("No anagrams found.")
        else:
            print("This is NOT a valid English word.")

if __name__ == "__main__":
    main()
