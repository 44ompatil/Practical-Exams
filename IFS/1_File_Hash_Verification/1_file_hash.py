import hashlib
import os

def generate_file_hash(filepath, algorithm='sha256'):
    """Generates a hash for the given file using the specified algorithm."""
    try:
        # Using hashlib.new() allows dynamic algorithm selection
        hasher = hashlib.new(algorithm)
        # Open file in binary mode for reading
        with open(filepath, 'rb') as f:
            # Read and update hash in chunks to handle large files efficiently
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except ValueError:
        print(f"Error: Unsupported hash algorithm '{algorithm}'.")
        return None

def verify_file_integrity(filepath, original_hash, algorithm='sha256'):
    """Verifies if the file's current hash matches the original hash."""
    current_hash = generate_file_hash(filepath, algorithm)
    if current_hash is None:
        return False
    
    print(f"\n[+] Original Hash: {original_hash}")
    print(f"[+] Current Hash:  {current_hash}")
    
    if current_hash == original_hash:
        print("\n[SUCCESS] The file has NOT been modified. Hashes match.")
        return True
    else:
        print("\n[WARNING] The file HAS BEEN MODIFIED! Hashes do not match.")
        return False

if __name__ == "__main__":
    test_file = "test_document.txt"
    
    # 1. Create a sample file
    print("--- 1. Creating Sample File ---")
    with open(test_file, 'w') as f:
        f.write("This is a highly confidential document.\nDo not share.")
    print(f"Created file: {test_file}")

    # 2. Generate the initial hash
    print("\n--- 2. Generating Initial Hash ---")
    initial_hash = generate_file_hash(test_file)
    if initial_hash:
         print(f"Generated SHA-256 Hash: {initial_hash}")
    
    # 3. Verify before modification (Should match)
    print("\n--- 3. Verifying File (Before Modification) ---")
    verify_file_integrity(test_file, initial_hash)

    # 4. Modify the file
    print("\n--- 4. Modifying the File ---")
    with open(test_file, 'a') as f:
        f.write("\nAdding some unauthorized content!")
    print("File modified.")

    # 5. Verify after modification (Should fail)
    print("\n--- 5. Verifying File (After Modification) ---")
    verify_file_integrity(test_file, initial_hash)
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
        print("\nCleaned up sample file.")
