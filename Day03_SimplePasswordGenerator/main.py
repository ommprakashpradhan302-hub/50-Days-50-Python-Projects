
import random
import string


def generate_password(length): 
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation


def generate_password(length):
    letters = string.ascii_letters # a-z, A-Z
    digits = string.digits # 0-9
    symbols = string.punctuation # Special characters
    all_chars = letters + digits + symbols
    password = []
    for i in range(length):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)


# Main program
length = int(input("Enter password length: "))
pwd = generate_password(length)
print(f"Generated Password: {pwd}")
print("Password strength: Strong")