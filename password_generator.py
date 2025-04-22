import random
import string

def get_password_length():
    """
    Prompt the user for the desired password length (positive integer).
    Keep asking until valid input is provided.
    """
    while True:
        try:
            value = input("Decide on the length of the password: ")
            length = int(value)
            if length <= 0:
                print("Please enter a number greater than zero.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise SystemExit


def generate_password(length):
    """
    Generate a random password of given length using letters, digits, and punctuation.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    try:
        length = get_password_length()
        password = generate_password(length)
        print("=== New Password ===")
        print(password)
        print(f"Password length is {len(password)} characters.")
    except SystemExit:
        print("Exiting password generator.")

if __name__ == '__main__':
    main()
