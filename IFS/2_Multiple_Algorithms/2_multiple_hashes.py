import hashlib

def generate_hashes(input_string):
    """
    Generates MD5, SHA-1, and SHA-256 hashes for a given string.
    """
    # 1. Encode the string to bytes before hashing
    encoded_string = input_string.encode('utf-8')

    # 2. Calculate MD5 Hash
    # Note: MD5 is considered cryptographically broken and should not be used
    # for security-sensitive applications. Using it here for demonstration.
    md5_hash = hashlib.md5(encoded_string).hexdigest()

    # 3. Calculate SHA-1 Hash
    # Note: SHA-1 is also considered weak against well-funded attackers.
    sha1_hash = hashlib.sha1(encoded_string).hexdigest()

    # 4. Calculate SHA-256 Hash
    # SHA-256 is part of the SHA-2 family and is currently considered secure.
    sha256_hash = hashlib.sha256(encoded_string).hexdigest()

    return {
        'MD5': md5_hash,
        'SHA-1': sha1_hash,
        'SHA-256': sha256_hash
    }

if __name__ == "__main__":
    print("-" * 50)
    print("      Multiple Hash Algorithm Generator")
    print("-" * 50)

    # Get input from the user
    user_input = input("Enter a string to hash: ")

    if not user_input:
         print("Input cannot be empty. Exiting.")
    else:
        print("\nCalculating Hashes for:", user_input)
        print("-" * 50)
        
        # Call the function and get the dictionary of results
        results = generate_hashes(user_input)

        # Print the results beautifully
        # .ljust() aligns the text to the left
        print(f"{'Algorithm':<10} | {'Hash Value'}")
        print("-" * 50)
        for algo, hash_value in results.items():
             print(f"{algo:<10} | {hash_value}")
        print("-" * 50)
