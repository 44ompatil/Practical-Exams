# Breadth First Search Algorithm (Uninformed Search)

## What is it?
Imagine you lost your keys in your house. How do you search? 
Instead of walking straight to the back bedroom and searching deeply under the bed (which is Depth First Search), you decide to search your house systematically:
1. First, search the exact spot you are standing on.
2. Next, search everything exactly 1 arm's length away.
3. Next, search everything 2 arm's length away.
4. And so on, moving outwards in expanding circles.

You search everywhere close by before you bother walking to the far corners of the house.

This is **Breadth First Search (BFS)**. It explores all the neighbors around you before moving deeper into the next layer of neighbors. Because it expands outward evenly, it is mathematically guaranteed to find the *shortest path* to your destination!

## Why is it called "Uninformed"?
Like DFS, it has no clue where the keys actually are. It isn't being pulled to a specific area by a "hunch" or a clue. It just objectively checks every possibility layer by layer.

## How to run this code?
Just run `python main.py` in your terminal!
