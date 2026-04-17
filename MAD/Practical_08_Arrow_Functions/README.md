# Practical 8: Arrow Functions

## The Shortcut
When writing code, sometimes our functions are incredibly simple. It might literally be just one line of code doing one tiny thing.

Normally, the rules of Dart say everything requires opening brackets, closed brackets, and the word `return`.
```dart
int doubleValue(int number) {
  return number * 2;
}
```

An **Arrow Function** uses the `=>` symbol (a little arrow!) to skip all the traditional fluff. It is the exact same logic, but shrunk down into a quick, punchy one-liner:
```dart
int doubleValue(int number) => number * 2;
```
The arrow basically translates to: "Go straight ahead and return this value." It saves screen space and makes simple math or operations very fast to read!
