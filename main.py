import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


password_length = int(input("Enter the desired password length: "))

generated_password = generate_password(password_length)

print(f"Your new password is: {generated_password}")

