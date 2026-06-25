# Password Validator

A simple Java console application that prompts the user to create a password and validates it against common security requirements.

## Features

- Requires a minimum length of 8 characters
- Requires at least one uppercase letter
- Requires at least one digit
- Requires at least one special character
- Prints feedback on why the password is invalid
- Repeats until a valid password is entered

## Requirements

- Java JDK 8 or newer
- A terminal or command prompt

## Project Structure

- `Main.java` - The entry point for the application and password validation logic

## Usage

1. Open a terminal in the `Password_Validator` folder.
2. Compile the program:

```bash
javac Main.java
```

3. Run the program:

```bash
java Main
```

4. Follow the prompt and enter a password.
5. If the password does not meet the required rules, the program displays a message and asks again.

## Password Validation Rules

A valid password must include:

- At least 8 characters
- At least one uppercase letter
- At least one number
- At least one special character (non-letter character)

## Example Output

```text
Create Password: hello
Password should contain at least 8 characters.
Please enter a stronger password.

Create Password: Hello123
At least one special character is required.
Please enter a stronger password.

Create Password: Hello@123
Password accepted successfully!
```

## Notes

This project is intended as a simple demonstration of input validation and Java console I/O.