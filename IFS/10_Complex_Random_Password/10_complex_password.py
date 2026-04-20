import secrets
import string

def generate_complex_password(length=12):
    """
    Generates a secure random password containing at least:
    - 1 lowercase letter
    - 1 uppercase letter
    - 1 digit
    - 1 special symbol
    """
    if length < 4:
        return "Error: Password length must be at least 4 to meet constraints."
        
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters into one pool
    all_chars = lower + upper + digits + symbols
    
    # Ensure at least one character from each set is picked
    # This loop continues until a password meeting all conditions is generated
    while True:
        # Generate random password using secrets
        pwd = ''.join(secrets.choice(all_chars) for i in range(length))
        
        # Validation checks
        has_lower = any(c in lower for c in pwd)
        has_upper = any(c in upper for c in pwd)
        has_digit = any(c in digits for c in pwd)
        has_symbol = any(c in symbols for c in pwd)
        
        # If all constraints are met, break and return the password
        if has_lower and has_upper and has_digit and has_symbol:
            break
            
    return pwd

if __name__ == "__main__":
    print("-" * 50)
    print("   Complex Secure Password Generator")
    print("-" * 50)
    
    try:
        user_length = int(input("Enter password length (minimum 4): "))
        if user_length >= 4:
             password = generate_complex_password(user_length)
             print(f"\n[+] Generated Password: {password}")
        else:
             print("[-] Please enter a length of at least 4.")
    except ValueError:
        print("[-] Invalid input. Please enter an integer.")
