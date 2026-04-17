void main() {
  Smartphone myPhone = Smartphone();
  myPhone.takePhotos(); // Inherited from Camera
  myPhone.makeCalls();  // Specific to Smartphone
}

class Camera {
  void takePhotos() {
    print("Click! Taking a picture.");
  }
}

// Smartphone inherits from Camera
class Smartphone extends Camera {
  void makeCalls() {
    print("Ring ring! Calling a friend.");
  }
}
