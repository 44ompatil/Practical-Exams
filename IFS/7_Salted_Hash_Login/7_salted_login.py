import hashlib
import os

# Format: {"username": {"salt": "hex_salt", "hash": "hex_hash"}}
user_db = {}

def create_salted_hash(password, salt=None):
    """Creates a salted SHA-256 hash. Generates a new salt if None is provided."""
    if salt is None:
        # Generate a new 16-byte random salt and convert it to hex
        salt = os.urandom(16).hex()
    
    # Concatenate the salt and the password before hashing
    # Format: salt + password
    salted_password = salt + password
    
    # Generate the hash
    hashed = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    
    return salt, hashed

def register():
    """Registers a new user and stores BOTH salt and hash."""
    print("\n--- Registration ---")
    username = input("Enter new username: ").strip()
    
    if username in user_db:
         print("Username exists!")
         return
         
    password = input("Enter password: ")
    
    # Generate salt and hashed password
    salt, hashed_pw = create_salted_hash(password)
    
    # Store BOTH the salt and the hash in the database
    user_db[username] = {
        "salt": salt,
        "hash": hashed_pw
    }
    print("[SUCCESS] User registered gracefully. Salt and Hash stored.")

def login():
    """Retrieves user salt, hashes input password, and compares hashes."""
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
    
    if username not in user_db:
         print("[FAILED] Username not found.")
         return
         
    # 1. Retrieve the specific salt for this user from the database
    stored_salt = user_db[username]["salt"]
    stored_hash = user_db[username]["hash"]
    
    # 2. Hash the input password using the retrieved salt
    _, input_hash = create_salted_hash(password, salt=stored_salt)
    
    # 3. Compare the newly generated hash with the stored hash
    if input_hash == stored_hash:
         print(f"\n[SUCCESS] Authentication verified! Welcome {username}.")
    else:
         print("\n[FAILED] Incorrect password.")

if __name__ == "__main__":
    while True:
        print("\n=== Salted Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. View Database (For Demo Purposes)")
        print("4. Exit")
        
        choice = input("Choice: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("\nDatabase State:")
            print(user_db)
        elif choice == '4':
            break
