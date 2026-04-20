# Practical 1: File Hash Verification

## Concept
Hashing is a mathematical algorithm that maps data of arbitrary size to a bit array of a fixed size (the "hash"). It is a one-way function, meaning you cannot normally retrieve the original data from the hash. 
In information security, hashes are used to verify **data integrity**. If a file is modified even slightly (a single bit changes), the resulting hash will be completely different. By comparing a previously calculated hash of a file against a newly calculated one, we can determine if the file has been tampered with.

## Objective
Write a python program to generate the hash of a file, then verify if the file has been modified using the hash.

## Code Explanation (`1_file_hash.py`)
1.  **`hashlib` module**: The script relies on Python's built-in `hashlib` library which provides access to secure hash and message digest algorithms (like SHA-256).
2.  **`generate_file_hash(filepath)`**: 
    - This function opens the target file in binary read mode (`rb`).
    - It reads the file in manageable chunks (4096 bytes) using `iter()` and a lambda function. This is critical because loading a massive file into memory all at once could crash the program.
    - It uses `hasher.update(chunk)` to update the algorithm's state with each chunk.
    - Finally, it returns the hexadecimal representation of the hash using `hasher.hexdigest()`.
3.  **`verify_file_integrity()`**: This calculates the hash of the file again and compares it to the original, provided hash.
4.  **Demonstration Flow**: The main execution block:
    - Creates a temporary configuration dummy file.
    - Hashes it.
    - Re-hashes and confirms it's unmodified.
    - Changes the file context.
    - Re-hashes and confirms it has been modified.
    - Deletes the temporary file.
