# Practical 20: Transiting and Back

## Giving the User a Back Button
Just like Practical 19, we are moving from one screen to the other. But this time we emphasize coming BACK!

In Flutter, when you use `Navigator.push()` with an AppBar, Flutter automatically provides a visual back button (an arrow) in the top left corner.
However, we can also manually write code to return. To do this, we use `Navigator.pop()`. 

Remember the plates analogy? Calling `pop` throws the current screen away, and the phone smoothly transitions back to the previous view. 
