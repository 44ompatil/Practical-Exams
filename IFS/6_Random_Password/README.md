# Practical 6: Random Password Generator

## Concept
Weak passwords (e.g., "password123", "qwerty") are highly susceptible to dictionary and brute-force attacks. Strong security practices require auto-generated, randomized passwords for accounts. 
In Python, generating passwords using the standard `random` module is highly discouraged for security purposes because standard mathematical pseudo-random number generators (PRNGs) can be predicted. Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs) provided by the `secrets` module should be used instead.

## Objective
Write a program to generate a secure random password of given length.

## Code Explanation (`6_random_password.py`)
1.  **`secrets` module**: Imported because it is designed for generating cryptographically strong random numbers suitable for passwords, account authentication, and security tokens.
2.  **`string` module**: Provides pre-defined string constants like `string.ascii_letters` (a-z, A-Z) and `string.digits` (0-9).
3.  **`generate_random_password(length)`**: 
    - Assembles the comprehensive alphabet by combining letters and numbers.
    - Utilizes list comprehension and `secrets.choice()` to pick random characters from the alphabet `length` times.
    - Returns the securely generated password string.
