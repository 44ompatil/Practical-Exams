void main() {
  Dog myDog = Dog();
  myDog.makeSound();
}

abstract class Animal {
  // This function has no body. It is an abstract idea.
  void makeSound(); 
}

class Dog extends Animal {
  @override
  void makeSound() {
    print("Woof! Woof!");
  }
}
