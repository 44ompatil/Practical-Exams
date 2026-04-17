void main() {
  int marks = 85;

  print("--- If-Else Statement ---");
  if (marks >= 90) {
    print("Grade: A");
  } else if (marks >= 80) {
    print("Grade: B");
  } else {
    print("Grade: C");
  }

  print("\n--- Switch Statement ---");
  int day = 3;
  switch (day) {
    case 1:
      print("Monday");
      break;
    case 2:
      print("Tuesday");
      break;
    case 3:
      print("Wednesday");
      break;
    default:
      print("Weekend or invalid day");
  }
}
