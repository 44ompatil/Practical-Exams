# Practical 4: Login System with Block (3 Attempts)

## Concept
Brute-force attacks involve an attacker continuously guessing passwords until they get one right. To mitigate this risk, security implementation guidelines require access controls on the number of sequential login attempts an individual can make. After a predefined number of failures (usually 3 to 5), the session is terminated or locked to drastically slow down an automated brute-force tool.

## Objective
Create a login system that allows only 3 attempts and blocks access after repeated failures.

## Code Explanation (`4_login_block.py`)
1.  **Configuration Constant**: We use `MAX_ATTEMPTS = 3` to store the maximum allowed failed login limit. This makes it easily configurable later if requirements shift.
2.  **`user_db` Pre-population**: An account (`admin`) with a hashed password (`secret123`) is pre-filled so the user can immediately test without needing to script a registration phase again.
3.  **Iteration Control**: A `while` loop checks if the `attempts` variable is less than `MAX_ATTEMPTS`.
4.  **Handling Success**: If the hash matches the database, it prints a success message and returns, effectively ending the loop.
5.  **Handling Failures**: If credentials are wrong or the username isn't found, the code increments `attempts`. Once `attempts` hits 3, the loop breaks out and triggers the "Account Blocked" state, refusing to take any more input.
