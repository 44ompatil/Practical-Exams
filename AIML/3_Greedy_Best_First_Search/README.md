# Greedy Best-First Search (Informed Search)

## What is it?
Imagine you are driving to a coffee shop using a map. At every intersection, you look at your map and pick the road that seems to point *most directly* towards the coffee shop. You don't care about traffic or speed limits; you just want to go in a straight line toward your goal.

This is exactly what **Greedy Best-First Search** does! It is "greedy" because it always takes the immediate step that *looks* closest to the finish line. 

## How does it know what is closest? "Heuristics" 
Unlike blind searches (DFS/BFS), this algorithm has a "Heuristic." A heuristic is just a fancy word for a "guess" or "estimate." It is like a compass telling you "The coffee shop is roughly 2 miles North from here." 

The algorithm trusts this compass blindly.

## The Catch
Sometimes, the road that points directly at the coffee shop is a dead end, or leads to a broken bridge. Greedy BFS can get stuck or take a really bad route because it is short-sighted—it only looks at what seems best right *now*.

## How to run this code?
Just run `python main.py` in your terminal!
