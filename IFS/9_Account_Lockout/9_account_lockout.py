import hashlib

# Mock User Database tracking lockout states
# "locked": False indicates active account, True indicates a permanent lock until an admin clears it.
user_db = {
    "john_doe": {
        "password": hashlib.sha256("password123".encode('utf-8')).hexdigest(),
        "failed_attempts": 0,
        "locked": False
    }
}

MAX_FAILED_ATTEMPTS = 3

def login():
    """Handles the login process and tracks failed attempts per user."""
    print("\n--- System Login ---")
    username = input("Username: ").strip()
    
    if username not in user_db:
        print("[FAILED] Invalid credentials.")
        return
        
    # Check if account is already locked
    if user_db[username]["locked"]:
        print("\n[ERROR] Account is LOCKED. Please contact the administrator.")
        return
        
    password = input("Password: ")
    input_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    if user_db[username]["password"] == input_hash:
        # Reset failed attempts upon successful login
        user_db[username]["failed_attempts"] = 0
        print(f"\n[SUCCESS] Welcome back, {username}!")
    else:
        # Increment failed attempts
        user_db[username]["failed_attempts"] += 1
        current_fails = user_db[username]['failed_attempts']
        
        print("\n[FAILED] Incorrect password.")
        
        # Check if lockout threshold is reached
        if current_fails >= MAX_FAILED_ATTEMPTS:
            user_db[username]["locked"] = True
            print(f"[SECURITY ALERT] {MAX_FAILED_ATTEMPTS} failed attempts reached.")
            print("[SECURITY ALERT] Account has been persistently LOCKED.")
        else:
            remaining = MAX_FAILED_ATTEMPTS - current_fails
            print(f"Warning: Account will lock in {remaining} more failed attempt(s).")

def admin_unlock():
    """Simulates an admin clearing a lock state."""
    print("\n--- Admin Override ---")
    username = input("Enter username to unlock: ").strip()
    
    if username in user_db:
        user_db[username]["locked"] = False
        user_db[username]["failed_attempts"] = 0
        print(f"[SUCCESS] Lock state cleared for user: {username}.")
    else:
        print("User not found.")

if __name__ == "__main__":
    print("Hint: User account is john_doe / password123")
    while True:
        print("\n1. Login")
        print("2. Admin: Unlock Account")
        print("3. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            login()
        elif choice == '2':
            admin_unlock()
        elif choice == '3':
             break
