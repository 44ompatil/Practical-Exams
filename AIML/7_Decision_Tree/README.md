# Decision Trees

## What is it?
A Decision Tree is basically a giant game of "20 Questions." 

Imagine you are trying to guess an animal. 
- You ask: "Does it have fur?" (Yes)
- "Does it bark?" (No)
- "Does it meow?" (Yes)
--> Conclusion: It's a cat!

A Decision Tree is an AI model that looks at data and automatically figures out the best "Yes/No" questions to ask to arrive at an answer. 

## How does it work?
In our code example, we give the AI a dataset of past days, showing what the weather was like and whether or not people decided to play Golf. 
The AI builds a flowchart (a tree branch structure). The top of the tree is the most important question (e.g. "Is it windy?"). It branches down until it gives a final decision at the bottom.

## How to run this code?
Make sure `scikit-learn`, `pandas`, and `matplotlib` are installed in your virtual environment.
Run `python main.py` in your terminal! 
It will generate a cool image file called `decision_tree_output.png`!
