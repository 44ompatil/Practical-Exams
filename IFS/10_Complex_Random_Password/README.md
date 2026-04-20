# Practical 10: Complex Random Password Generator

## Concept
A truly resilient password needs to have enough entropy to negate the possibility of guessing or brute-forcing within a reasonable timeframe. Relying purely on alphanumeric characters sometimes isn't enough; complexity rules enforce the inclusion of distinct sets of characters: lowercase letters, uppercase letters, numeric digits, and special symbols. Random generation with validation ensures these complexity requirements are mathematically met rather than relying on human creation.

## Objective
Write a program to generate a secure random password of given length that explicitly includes letters, numbers, and symbols.

## Code Explanation (`10_complex_password.py`)
1.  **Libraries**: The `secrets` module is imported for cryptographically secure random number generation, alongside `string` for easy access to character classes (`string.punctuation` holds symbols).
2.  **Constraint Enforcement via Loop**: The program enters an infinite `while True` loop. Inside this loop, it generates a fully random password of the requested length from the combined pool of all characters.
3.  **Validation Checkers**: The code uses the `any()` function combined with list comprehension (`any(c in lower for c in pwd)`) to verify that at least one character in the newly generated password matches a character in each of the predefined required subsets.
4.  **Acceptance**: If all validations return True (`has_lower and has_upper and has_digit and has_symbol`), it means the password is comprehensively complex. The loop `break`s and the string is safely returned.
