# Practical 19: Navigator

## Moving Between Screens
In an app, you almost never stay on the same screen. We need to go from the home screen into a settings screen, or into a chat screen.

To do this, Flutter uses a `Navigator`. Think of it like stacking plates.
When we go to a new screen, we `push` a new plate on top of the old one. We are looking at the new screen!
When we want to go back, we `pop` the top plate off, revealing the original screen underneath!
