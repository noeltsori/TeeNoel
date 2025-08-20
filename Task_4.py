import os

def modify_line(line, choice, old_word=None, new_word=None):
    """Modify a single line based on user's choice."""
    if choice == "1":
        return line.upper()
    elif choice == "2":
        return line.lower()
    elif choice == "3":
        if old_word is not None and new_word is not None:
            return line.replace(old_word, new_word)
    return line

def process_file():
    input_filename = input("Enter the input filename: ")
    output_filename = f"modified_{input_filename}"

    # Ask user how to modify the content
    print("\nChoose modification type:")
    print("1 - Convert all text to UPPERCASE")
    print("2 - Convert all text to lowercase")
    print("3 - Replace a word with another word")
    choice = input("Enter 1, 2, or 3: ")

    old_word = new_word = None
    if choice == "3":
        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")

    try:
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")

        if not os.access(input_filename, os.R_OK):
            raise PermissionError(f"The file '{input_filename}' cannot be read.")

        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified = modify_line(line, choice, old_word, new_word)
                outfile.write(modified)

        print(f"\nFile successfully processed! Modified content written to '{output_filename}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    process_file()
