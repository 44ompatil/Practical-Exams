# Practical 7: Salted Hash Login System

## Concept
A standard hashed login system (like Practical 3) has a major vulnerability: identical passwords will result in identical hashes. Attackers can use "Rainbow Tables" (massive pre-computed tables of hashes for common passwords) to reverse the hash instantly without brute-forcing it.

**Salting** fixes this. A "salt" is a random sequence of data generated for each specific user. This string is appended to the plaintext password *before* it is hashed. Because every user has a unique salt, even if two users have the exact same password ("password123"), their final stored hashes will look completely different, rendering Rainbow Tables useless.

## Objective
Write a program to hash passwords with a random salt. Store both salt and hash. Verify the password during login.

## Code Explanation (`7_salted_login.py`)
1.  **Random Salt Generation**: Uses `os.urandom(16).hex()` to generate 16 random bytes and formatting them as a hexadecimal string. This is done during registration.
2.  **Hashing**: The `create_salted_hash` function takes the plaintext password, prefixes it with the salt, and hashes the entire string (`hash(salt + password)`).
3.  **Storage**: The `user_db` must store *both* the generated salt and the generated hash for that specific user. The salt is generally not treated as a secret; it just needs to be unique.
4.  **Verification**: During login, the program accesses the database, pulls out the user's previously stored salt, appends it to the newly typed-in password attempt, hashes it, and checks if it matches the stored hash.
