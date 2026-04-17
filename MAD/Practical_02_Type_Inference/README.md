# Practical 2: Type Inference using `var`

## The Smart Robot Assistant
In the previous practical, we had to strictly tell the computer what type of data we were storing (like putting text exclusively in a `String` box). 

But Dart has a very smart feature called **Type Inference**. 

Imagine you hand an apple to a robot sorting assistant. You don't need to yell, "THIS IS A FRUIT!" The robot looks at it, recognizes it's an apple, and automatically puts it in the fruit basket.

When we use the word **`var`** (short for variable) instead of typing `String` or `int`, we are letting the computer guess the type of box needed based on what we put inside it.

If we write `var age = 20;`, the computer sees the `20` and secretly thinks, "Aha! That's a whole number. I'll make this an `int` box behind the scenes." 

This saves us time and makes our code quicker to write, without losing the safety of properly labeled boxes!
