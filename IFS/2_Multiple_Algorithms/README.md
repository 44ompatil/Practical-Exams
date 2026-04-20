# Practical 2: Multiple Hash Algorithms

## Concept
Different hashing algorithms provide varying levels of security and produce different lengths of output. 
- **MD5 (Message Digest 5)**: Produces a 128-bit hash (32 hexadecimal characters). It is mathematically broken and prone to collision attacks (where two different inputs produce the resulting hash). It is fast but insecure. 
- **SHA-1 (Secure Hash Algorithm 1)**: Produces a 160-bit hash (40 hexadecimal characters). It is also considered weak and vulnerable to collision attacks (e.g., SHAttered attack).
- **SHA-256 (Secure Hash Algorithm 256-bit)**: Belongs to the SHA-2 family. Produces a 256-bit hash (64 hexadecimal characters). Currently widely used and considered highly secure against collision and preimage attacks.

## Objective
Write a Python program to generate hashes of the same input using MD5, SHA-1, and SHA-256.

## Code Explanation (`2_multiple_hashes.py`)
1.  **Input Encoding**: The `hashlib` requires input as bytes, not basic strings. The program first takes the user string and runs `input_string.encode('utf-8')`.
2.  **Algorithm Initialization**: `hashlib.md5()`, `hashlib.sha1()`, and `hashlib.sha256()` generate the respective hash objects.
3.  **Returning Output**: Using `.hexdigest()` on each hash object transforms the byte data into a human-readable hexadecimal string. 
4.  **Display**: The code loops over the computed hashes and prints them out nicely aligned.
