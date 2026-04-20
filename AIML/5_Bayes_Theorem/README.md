# Bayes' Theorem

## What is it?
Bayes' Theorem is a way to *update your beliefs* when you get new evidence. It is famously used to show how tricky medical tests can be.

## The Medical Test Example
Imagine there is a rare disease that only 1% of the population gets.
A doctor gives you a test that is "99% accurate". You take the test, and it comes back POSITIVE. 

You panic! You must be 99% likely to be sick, right? 

**NO! Bayes' Theorem proves you are likely fine.**
Why? Because the disease is so rare, and the 1% error rate on healthy people creates so many "false alarms" that the false alarms actually outnumber the real sick people! 

Bayes' Theorem uses simple math to calculate:
`Chance of being sick given a positive test = (Real Sick Positives) / (Real Sick Positives + False Alarms)`

Run the script to see the actual math in action. It will blow your mind!

## How to run this code?
Just run `python main.py` in your terminal!
