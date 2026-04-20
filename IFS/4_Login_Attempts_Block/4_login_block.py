import hashlib

# Pre-populated mock database
# In this practical, we'll give the user an account to test with.
# Password is "secret123"
user_db = {
    "admin": hashlib.sha256("secret123".encode('utf-8')).hexdigest()
}

MAX_ATTEMPTS = 3

def login():
    """Handles login with a maximum of 3 attempts before temporary block."""
    attempts = 0
    
    print("\n--- Secure System Login ---")
    
    while attempts < MAX_ATTEMPTS:
        username = input("Username: ").strip()
        password = input("Password: ")
        
        # Verify credentials
        if username in user_db:
             input_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
             if user_db[username] == input_hash:
                 print(f"\n[SUCCESS] Access Granted! Welcome, {username}.")
                 return True
                 
        # Increment attempt tracker on failure
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        
        print(f"[FAILED] Invalid credentials.")
        if remaining > 0:
            print(f"You have {remaining} attempt(s) left.\n")
        else:
             print("\n[BLOCKED] You have failed to login 3 times.")
             print("Your session is now temporarily blocked.")
             return False

if __name__ == "__main__":
    print("Hint: The username is 'admin' and the password is 'secret123'")
    login()
