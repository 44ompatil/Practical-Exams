void main() {
  Person p = Person("David", 30);
  p.showDetails();
}

class Person {
  String name;
  int age;

  // This is the constructor
  Person(this.name, this.age);

  void showDetails() {
    print("Name: $name, Age: $age");
  }
}
