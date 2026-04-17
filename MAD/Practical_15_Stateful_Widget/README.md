# Practical 15: Stateful Widget

## What is a Stateful Widget?
In Flutter, everything you see on screen is a "Widget" (a building block like a button, text, or image).
Some widgets are **Stateless** - meaning they are completely frozen once they are drawn. They never change. Like a simple `Text("Hello")`.
Other widgets are **Stateful** - meaning they are ALIVE. They can change what they look like while the app is running!

Here, we've created a Stateful widget. It holds a variable (the state) inside it, which allows it to update its display when tapped.
