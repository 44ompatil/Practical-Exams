# Practical 13: Method Overriding

## Changing the Rules
When a child class inherits an ability from a parent class (like we saw in the last practical), it doesn't mean the child is forced to do it the EXACT same way the parent did.

Let's say all `Animal`s have an `eat()` behavior, and by default, it just says "Eating normal food."

When we create a `Cat` that inherits from `Animal`, the Cat thinks, "Wait, I don't eat normal food, I specifically eat fish."

**Method Overriding** is the ability of the child to replace the parent's behavior with its own custom version! 
We use the keyword `@override` to politely tell the code, "I know I inherited the eat method, but I am overwriting it with my own Cat-specific instructions."

This lets us use widespread abilities while allowing specific objects to act uniquely!
