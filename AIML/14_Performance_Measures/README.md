# Performance Measures (Accuracy vs Precision vs Recall)

## What is it?
"Accuracy" is not always the best way to measure AI. Let's look at a hospital predicting a rare disease that only 1 in 1000 people have. 
If an AI just lazily guesses "Healthy" every single time, it will be right 999 times out of 1000. It has **99.9% Accuracy**, but it is a terrible AI because it didn't catch the 1 sick person!

Therefore, we have other ways to score AI:

## 1. Precision 
**"The Boy Who Cried Wolf" Score.**
When the AI *claims* it found the disease, how often is it actually right? If Precision is low, it means the AI is generating tons of annoying false alarms.

## 2. Recall
**"The Safety Net" Score.**
Out of all the *actually* sick people in the building, how many did the AI successfully flag? If Recall is low, it means the AI is dangerous because it is letting sick people walk out the door undiagnosed. 

In a hospital, doctors care about **Recall** the most. They would rather have a few false alarms (low precision) than miss a sick person (high recall). 

## How to run this code?
Make sure `scikit-learn` is installed.
Run `python main.py` in your terminal!
