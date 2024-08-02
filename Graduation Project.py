
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def text_to_morse(character):
    """
    Convert a single character to Morse code.
    """
    # Convert character to uppercase
    character = character.upper()
    # Use dictionary to get Morse code
    return morse_code_dict.get(character, '')

def string_to_morse(text):
    """
    Convert a string to Morse code using a loop.
    """
    morse_code_list = []
    for char in text:  # use loop
        morse_code = text_to_morse(char)
        if morse_code:  # use if
            morse_code_list.append(morse_code)
    # Join the list to form a single string
    return ' '.join(morse_code_list)

def main_menu():
    """
    Display the main menu and handle user choices.
    """
    print("\nMain Menu")
    print("1. Convert text to Morse code")
    print("2. Contact the developer")
    print("3. Exit")

def contact_developer():
    """
    Display contact information for the developer.
    """
    print("\nDeveloper Contact Information")
    print("Name: Mahmoud Amr")
    print("Email: mahmoud_amr2007@yahoo.com")

def main():
    """
    Main function to handle user input and convert to Morse code.
    """
    while True:  # استخدام الحلقة
        main_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':  # استخدام الشرط if
            input_text = input("Enter the text you want to convert to Morse code: ")
            morse_code = string_to_morse(input_text)
            print(f"Morse Code: {morse_code}")
        elif choice == '2':
            contact_developer()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Execute the main function
if __name__ == "__main__":
    main()
