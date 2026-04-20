# Practical 9: Account Lockout System

## Concept
Unlike a temporary session block (seen in Practical 4), a persistent account lockout alters the state of the user's account in the database. If an automated script attempts to brute force an account and fails sequentially, modifying the database state to "Locked" ensures that even if the attacker re-connects or regains access to the login page later, the system will refuse service outright until an administrator intervenes. This mitigates distributed brute-force attacks.

## Objective
Write a program to lock an account persistently after 3 failed login attempts.

## Code Explanation (`9_account_lockout.py`)
1.  **State Flags**: The simulated database holds a `locked` boolean and a `failed_attempts` integer counter for each user.
2.  **State Verification**: The first step of `login()` is to check `if user_db[username]["locked"]`. If it is True, it immediately stops processing without checking passwords.
3.  **Counter Manipulation**: 
    - A correct password resets the `failed_attempts` to 0.
    - An incorrect password increments `failed_attempts`.
4.  **Lock Trigger**: When `failed_attempts >= MAX_FAILED_ATTEMPTS`, the script updates `user_db[username]["locked"] = True`. 
5.  **Admin Override**: The `admin_unlock()` function provides a way to reset the integer counter and the boolean locking flag back to safe defaults, simulating a support team verifying identity and unlocking the account.
