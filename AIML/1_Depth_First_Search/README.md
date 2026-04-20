# Depth First Search Algorithm (Uninformed Search)

## What is it?
Imagine you are exploring a giant maze. You decide on a strategy: you will pick a path and walk down it as far as you possibly can until you hit a dead end. When you finally hit that dead end, you backtrack (turn around) just enough to find a new path you haven't taken yet, and then dive all the way down *that* one. 

You repeat this going-deep-and-backtracking process until you find the exit or explore the entire maze. 

This is exactly what **Depth First Search (DFS)** does! It's called "Depth" because it goes as "deep" into a path as possible before looking at other options. 

## Why is it called "Uninformed"?
It goes blindly. It doesn't have a map. It doesn't know if the path it chose is actually getting closer to the goal; it just relentlessly follows paths until it exhausts them.

## Real-World Example
Think of playing a game of chess. If you calculate "What if I move my pawn here? Then my opponent moves their knight there... Then I move my bishop... Then they block...", you are diving deep into one specific future scenario. This is a form of Depth First Search.

## How to run this code?
Just run `python main.py` in your terminal!
