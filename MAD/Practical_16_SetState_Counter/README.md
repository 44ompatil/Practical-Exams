# Practical 16: Uses setState()

## What is setState()?
In the previous practical, we learned that a Stateful Widget can change. But *how* does it tell the screen to redraw itself?

If we just write `counter = counter + 1`, the secret number in the background updates, but the physical screen doesn't know about it! The numbers on your screen remain frozen.

**`setState()`** is basically an alarm bell. When we put our update code inside `setState(() { ... })`, we are telling Flutter: 
"Hey! I changed some data, please redraw the screen immediately so the user can see the new result!"
