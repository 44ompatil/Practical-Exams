# Practical 4: Decision-Making Statements

## Making Choices
Programs would be boring if they only ever did the exact same steps in a row, unconditionally. Sometimes, we want a program to pause, look at the situation, and make a decision—just like arriving at a crossroads.

### The `If-Else` Statement
This is like giving the computer a condition. 
*"**If** it is raining, take an umbrella. **Else** (otherwise), wear sunglasses."*
In our code, we check the student's marks. 
If they have more than 90, we print Grade A. 
If they don't, we drop down to the `else if` (a secondary choice), checking if they have at least 80.
And finally, the `else` acts as the catch-all for anything left.

### The `Switch-Case` Statement
Imagine you are at a vending machine. You press button 1, you get a coke. You press button 2, you get water. 
A switch statement is exactly like a vending machine. We hand it a variable (like `day = 3`), and the code jumps straight to `case 3:` to execute what's there (printing "Wednesday"). It is a much cleaner way to write multiple "if" conditions that check the exact same variable!
