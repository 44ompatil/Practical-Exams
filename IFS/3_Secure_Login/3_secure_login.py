import hashlib

# In-memory "database" simulating user storage
# Format: {"username": "hashed_password"}
user_db = {}

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register():
    """Handles new user registration."""
    print("\n--- Registration ---")
    username = input("Enter a new username: ").strip()
    
    if username in user_db:
        print("Username already exists. Please try another one.")
        return
        
    password = input("Enter a password: ")
    
    # Hash the password for secure storage
    hashed_pwd = hash_password(password)
    
    # Store only the hash, never the plaintext password
    user_db[username] = hashed_pwd
    print("Registration successful!")

def login():
    """Handles user login."""
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if username not in user_db:
         print("Login failed: Username not found.")
         return
         
    # Hash the input password to compare it against the stored hash
    input_hashed = hash_password(password)
    
    if user_db[username] == input_hashed:
        print(f"\n[SUCCESS] Welcome back, {username}!")
    else:
        print("\n[FAILED] Incorrect password.")

if __name__ == "__main__":
    while True:
        print("\n=== Secure System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
