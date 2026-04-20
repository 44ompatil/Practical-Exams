# A* Search Algorithm (Informed Search)

## What is it?
A* (pronounced "A-Star") is the absolute gold standard for finding your way around. It is the algorithm used by Google Maps and video games to find the fastest way from Point A to Point B.

To understand it, remember Greedy Best-First Search? Greedy only cared about "How close does this look to the target?" (Heuristic).

A* is smarter. It says: "I care about how close it looks, BUT I also care about how much gas I spent getting here."

## The Magic Formula
A* uses a simple equation:
`F = G + H`

- **G (Gas/Cost)**: How far have we actually traveled to get here from the start?
- **H (Heuristic/Estimate)**: How far do we *guess* we have left to go until the finish line?
- **F (Total)**: The total guess of how long this whole trip will take!

By always choosing the path with the lowest **Total (F)**, A* is mathematically guaranteed to find the absolute shortest path without getting tricked by dead ends. 

## How to run this code?
Just run `python main.py` in your terminal!
