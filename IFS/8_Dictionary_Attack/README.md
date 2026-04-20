# Practical 8: Simple Dictionary Attack

## Concept
A dictionary attack is a common method used to break into a password-protected computer or server system by systematically entering every word in a dictionary as a password. In the context of offline password cracking, an attacker steals a database of hashed passwords and then repeatedly hashes words from a text file ("wordlist" or "dictionary") comparing the resulting hash to the stolen hash. If they match, the password is recovered.

## Objective
Create a simple dictionary attack: Try possible combinations from a given list to crack a password.

## Code Explanation (`8_dictionary_attack.py`)
1.  **Target Definition**: We define a hardcoded `leaked_target_hash`. In real scenarios, attackers extract these from insecure or breached databases.
2.  **Wordlist Processing**: The `dictionary_attack()` function opens `wordlist.txt`. It reads line by line using an enumerator to track the attempt number.
3.  **String Cleanup**: Calling `.strip()` removes trailing invisible characters (like `\n` newlines) that naturally occur when reading lines from a text file, which would completely corrupt the resulting hash.
4.  **Hash and Compare**: Each word is hashed. If a hash equality is caught, the script breaks out and declares success, revealing the plaintext string that generated the hash.
