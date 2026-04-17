void main() {
  Car myDreamCar = Car();
  myDreamCar.brand = "Tesla";
  myDreamCar.color = "Red";
  
  myDreamCar.startEngine();
}

class Car {
  String? brand;
  String? color;

  void startEngine() {
    print("Vroom! $brand car of color $color has started.");
  }
}
