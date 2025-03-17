def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Only shift letters, leave other characters unchanged
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Keep spaces, punctuation, and numbers unchanged

    return result


# Step 1: Ask the user whether they want to encrypt or decrypt
mode = input("Do you want to encrypt or decrypt? ").strip().lower()

# Step 2: Validate the input
if mode not in ["encrypt", "decrypt"]:
    print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
else:
    # Step 3: Get user input for text and shift value
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    # Step 4: Perform encryption or decryption
    result = caesar_cipher(text, shift, mode)

    # Step 5: Display the result
    print(f"\nYour {mode}ed text: {result}")
