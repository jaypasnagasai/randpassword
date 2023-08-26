# Password Generator

This is a simple Python script that generates random passwords based on the selected character types. You can customize the password length and include or exclude uppercase letters, lowercase letters, digits, special characters, and spaces.

## Usage

1. Make sure you have Python installed on your system.
2. Clone or download this repository.

```sh
git clone https://github.com/yourusername/password-generator.git
```

1. Navigate to the repository folder.

```sh
cd password-generator
```

2. Run the script.

```sh
python password_generator.py
```

3. Follow the prompts to customize the password generation.

## Script Explanation

The script uses the `random` and `string` modules to generate passwords. It defines a `PasswordGenerator` class with methods for generating passwords. The main logic of generating passwords is in the `generate_password` method.

You can customize the following parameters when generating a password:


`length`: The length of the password.
`use_uppercase`: Include uppercase letters (y/n).
`use_lowercase`: Include lowercase letters (y/n).
`use_digits`: Include digits (y/n).
`use_special`: Include special characters (y/n).
`use_space`: Include spaces (y/n).

## Example: 

Here's an example of how the script works:
``` sh
Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y
Include spaces? (y/n): n
Generated Password: H3#jklF9Q2Ab
```

License

This project is licensed under the MIT License.
