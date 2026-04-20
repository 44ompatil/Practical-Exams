# Practical 3: Secure Login System

## Concept
A fundamental rule of information security is **never store passwords in plaintext**. If a database is breached, the attacker will have immediate access to all passwords. Instead, systems use hashing.
When a user registers, their password is hashed, and only the hash is placed in the database. When the user tries to log in later, the login password is hashed through the same algorithm. If the resulting hash matches the one in the database, the password is correct, and access is granted.

## Objective
Create a secure login system with hashed passwords.

## Code Explanation (`3_secure_login.py`)
1.  **Mock Database (`user_db`)**: An in-memory python dictionary is used as our mock persistent storage to hold username-to-hash mappings.
2.  **`hash_password(password)`**: Standardizes the use of `hashlib.sha256()` to return the hexadecimal representation of the password.
3.  **`register()`**: Prompts for a username and a password. It verifies the username isn't taken, hashes the password, and maps the username to the hashed password in `user_db`.
4.  **`login()`**: Asks for credentials. It hashes the provided password. It accesses `user_db[username]` and compares the strings. If they match, access is granted.
