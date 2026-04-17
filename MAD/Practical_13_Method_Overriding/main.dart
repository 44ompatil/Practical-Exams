void main() {
  Cat myCat = Cat();
  myCat.eat(); // Calls the overridden method
}

class Animal {
  void eat() {
    print("Animal is eating normal food.");
  }
}

class Cat extends Animal {
  // Overriding the parent's method
  @override
  void eat() {
    print("Cat is eating fish gently.");
  }
}
