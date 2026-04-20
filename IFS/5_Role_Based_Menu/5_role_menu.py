import hashlib

# Mock User Database with Role Binding
# Format: "username": {"password": "hashed_password", "role": "admin/user"}
users = {
    "admin1": {
        "password": hashlib.sha256("adminpass".encode('utf-8')).hexdigest(),
        "role": "admin"
    },
    "guest1": {
        "password": hashlib.sha256("guestpass".encode('utf-8')).hexdigest(),
        "role": "user"
    }
}

def display_admin_menu():
    print("\n--- [Admin Control Panel] ---")
    print("1. View Server Logs")
    print("2. Manage Users")
    print("3. Restart Service")
    print("4. Logout")

def display_user_menu():
    print("\n--- [User Dashboard] ---")
    print("1. View Profile")
    print("2. Change Password")
    print("3. Logout")

def login():
    print("=== System Login ===")
    username = input("Username: ").strip()
    password = input("Password: ")
    
    input_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    if username in users and users[username]["password"] == input_hash:
        role = users[username]["role"]
        print(f"\n[SUCCESS] Logged in as {role.upper()}")
        
        # Route to appropriate menu based on role
        if role == "admin":
            display_admin_menu()
        elif role == "user":
            display_user_menu()
        else:
            print("Unknown role. Exiting.")
    else:
        print("\n[FAILED] Invalid credentials.")

if __name__ == "__main__":
    print("Hint:")
    print("- Admin account: admin1 / adminpass")
    print("- User account: guest1 / guestpass\n")
    login()
