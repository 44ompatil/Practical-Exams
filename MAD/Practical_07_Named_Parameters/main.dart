void main() {
  printUser(name: "John");
  printUser(name: "Jane", age: 25);
}

// Named parameters exist inside {}
// The ? means the age might not be provided (it can be null)
void printUser({required String name, int? age}) {
  if (age != null) {
    print("User: $name, Age: $age");
  } else {
    print("User: $name, Age: Not provided");
  }
}
