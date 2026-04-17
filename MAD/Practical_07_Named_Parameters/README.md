# Practical 7: Named and Optional Parameters

## Making Requirements Flexible
In the previous practical, our math function strictly needed two numbers in an exact order. But sometimes, life isn't that strict!

Imagine ordering a coffee. Your "required" instruction is: "I want coffee." 
But you have an "optional" instruction: "Add sugar." If you forget to say it, the barista doesn't crash and burn; they just give you normal coffee without sugar.

### Named Parameters
By wrapping arguments in curly braces `{}`, we explicitly name the ingredients we are giving the function. You don't have to guess the order anymore! You directly write `name: "Jane"` and `age: 25`. It is super clear to read.

### Optional Parameters
Notice that we wrote `required String name`, meaning the name MUST be provided.
But `age` has a question mark `int? age` next to it. That question mark tells the computer, "Hey, they might provide an age, or they might not. If they don't, it is perfectly fine."

This makes our functions incredibly flexible and prevents crashes if tiny details aren't provided.
