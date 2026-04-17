# Practical 11: Abstract Classes

## Rules and Concepts
An **Abstract Class** is a concept instead of a concrete object. 

Imagine someone tells you to "Draw an Animal." You would probably ask, "What kind of animal? A tiger? A bird?" 
"Animal" isn't a specific thing you can draw; it's a broad category.

In programming, we make `Animal` an Abstract Class. It means: "You cannot create a generic animal. It is physically impossible." It forces us to create a *specific* animal, like a `Dog`.

Why do we use it? Because Abstract classes set the rules! 
Inside the abstract `Animal` class, we put a `makeSound()` function but left it completely empty. We are essentially decreeing a law: **"Any specific animal that wants to exist in our code MUST be capable of making a sound!"**

So when our `Dog` is created, it is forced to provide its own version of `makeSound()`. Abstract classes help us maintain structure and rules in large projects!
