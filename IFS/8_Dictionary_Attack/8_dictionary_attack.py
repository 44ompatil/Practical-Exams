import hashlib

def dictionary_attack(target_hash, wordlist_file):
    """
    Attempts to crack a target SHA-256 hash by hashing every word in a dictionary list.
    """
    print(f"[*] Starting dictionary attack targeting hash: {target_hash}")
    print(f"[*] Reading wordlist loosely from: {wordlist_file}")
    
    try:
        with open(wordlist_file, 'r') as file:
            # Enumerate through lines for counting attempts
            for attempt, line in enumerate(file, 1):
                # Remove newline characters and whitespace
                word = line.strip()
                
                # Hash the dictionary word
                word_hash = hashlib.sha256(word.encode('utf-8')).hexdigest()
                
                # Compare it against our target
                if word_hash == target_hash:
                    print(f"\n[SUCCESS] Password cracked on attempt {attempt}!")
                    print(f"[SUCCESS] The password is: '{word}'")
                    return True
                    
        print("\n[FAILED] Password not found in the dictionary.")
        return False
        
    except FileNotFoundError:
        print(f"\n[ERROR] Wordlist file '{wordlist_file}' not found.")
        return False

if __name__ == "__main__":
    # Let's say we retrieved this hash from a compromised database.
    # We know it's a SHA-256 hash.
    # The actual plaintext for this is "admin123"
    leaked_target_hash = '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'
    
    # Needs to match the wordlist file we created
    wordlist_path = 'wordlist.txt'
    
    dictionary_attack(leaked_target_hash, wordlist_path)
