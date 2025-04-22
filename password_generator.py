import random
import string


letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = list(string.punctuation)

all_letters = letters + digits + punctuation


def password_generator():
    i = 1
    password = []

    try:
        user_input = int(input("Decide on the length of the password: "))
    except ValueError:
        print("Please enter a number.")


    while i <= user_input:
        x = random.choice(all_letters)
        password.append(x)
        i += 1

    res = "".join([str(s) for s in password])
    print("===New password===")
    print(res)
    print(f"password length is {len(res)}")

password_generator()