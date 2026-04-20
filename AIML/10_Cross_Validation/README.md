# Cross Validation

## What is it?
Remember the "Train / Test Split" where we set aside 20% of our data for testing? 
Sometimes, 20% isn't enough to prove the AI is smart. What if the AI just got *lucky* on that specific 20%? 

**Cross Validation** fixes this by testing the AI multiple times, rotating the test material!

## How does it work? (5-Fold Example)
Imagine a pizza cut into 5 slices.
- **Round 1:** We feed the AI slices 1, 2, 3, 4. It takes the exam on slice 5.
- **Round 2:** We feed the AI slices 2, 3, 4, 5. It takes the exam on slice 1.
- **Round 3:** We feed the AI slices 3, 4, 5, 1. It takes the exam on slice 2.
...and so on!

By doing this, EVERY single piece of data is eventually used as a test. We take the average score of all 5 exams, giving us a highly accurate measure of how smart the AI actually is, without ever needing to find new data!

## How to run this code?
Make sure `scikit-learn` is installed.
Run `python main.py` in your terminal!
