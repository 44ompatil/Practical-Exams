void main() {
  print(sayHello("Alice"));
  print("Double of 5 is: ${doubleValue(5)}");
}

String sayHello(String name) => "Hello, $name!";

int doubleValue(int number) => number * 2;
