# Confusion Matrix

## What is it?
A Confusion Matrix is a simple grid that tells us exactly *how* an AI is getting confused.

Imagine an AI guessing if an email is Spam or Not Spam. An accuracy score of "90%" sounds good, but we don't know *what* it's getting wrong. Is it accidentally deleting important emails? Or is it letting a few spam emails through to the inbox?

The Confusion Matrix splits the results into four boxes:
1. **True Positives**: It guessed it was Spam, and it WAS Spam! (Good)
2. **True Negatives**: It guessed it was Not Spam, and it WAS Not Spam! (Good)
3. **False Positives (Type 1 Error)**: It guessed Spam, but it was an Important Email! (Bad)
4. **False Negatives (Type 2 Error)**: It guessed Not Spam, but it WAS Spam! (Less Bad)

By looking at the grid, humans can decide if the AI is making "dangerous" mistakes.

## How to run this code?
Make sure `scikit-learn` and `matplotlib` are installed.
Run `python main.py` in your terminal! It will save an image of the matrix grid.
