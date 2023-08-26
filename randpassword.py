Can you create a GITHUB README file in markdown so I can copy paste it effortlessly?

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.special_chars = string.punctuation
        self.space = ' '  # Include space character

    def generate_password(self, length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True, use_space=True):
        if not any([use_uppercase, use_lowercase, use_digits, use_special, use_space]):
            raise ValueError("At least one character type should be selected")

        allowed_chars = ""
        if use_uppercase:
            allowed_chars += self.uppercase
        if use_lowercase:
            allowed_chars += self.lowercase
        if use_digits:
            allowed_chars += self.digits
        if use_special:
            allowed_chars += self.special_chars
        if use_space:
            allowed_chars += self.space

        password = ''.join(random.choice(allowed_chars) for _ in range(length))
        return password

if __name__ == "__main__":
    generator = PasswordGenerator()

    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_space = input("Include spaces? (y/n): ").lower() == 'y'

    password = generator.generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, use_space)
    print("Generated Password:", password)
