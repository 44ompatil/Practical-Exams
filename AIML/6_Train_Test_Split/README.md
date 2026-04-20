# Train / Test Split

## What is it?
Imagine you are a teacher preparing a student for an exam. You have a textbook with 10 math problems. 
Do you let the student study all 10 problems, and then give them an exam using those EXACT same 10 problems? 
No! Because you wouldn't know if they actually learned how to do math, or if they just memorized the answers!

Instead, you do a **Train / Test Split**:
1. You give them 8 problems to study at home (**The Training Set**).
2. You hide the remaining 2 problems and use them for the actual exam (**The Testing Set**).

## Why do we do this in AI?
Artificial Intelligence learns exactly like a student. If we give an AI 100% of our data to learn from, it might just memorize the data instead of finding patterns. When it faces a real-world scenario it has never seen, it will fail.

So, we forcefully split our data (usually an 80% / 20% split) before we even begin.

## How to run this code?
Make sure `scikit-learn` and `pandas` are installed in your virtual environment.
Then run `python main.py` in your terminal!
