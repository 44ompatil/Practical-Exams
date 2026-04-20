import secrets
import string

def generate_random_password(length):
    """Generates a secure random alphanumeric password."""
    if length < 4:
         return "Error: Password length must be at least 4."
         
    # Define the pool of characters. 
    # For this basic version, we'll use upper, lower, and digits.
    alphabet = string.ascii_letters + string.digits
    
    # Generate the password using secrets.choice for cryptographic security
    # The secrets module is used for generating cryptographically strong
    # random numbers suitable for managing data such as passwords.
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    
    return password

if __name__ == "__main__":
    print("-" * 40)
    print("   Secure Random Password Generator")
    print("-" * 40)
    
    try:
        pw_length = int(input("Enter desired password length (e.g. 12): "))
        
        generated_password = generate_random_password(pw_length)
        print(f"\nGenerated Password: {generated_password}")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")
