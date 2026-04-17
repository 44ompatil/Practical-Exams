void main() {
  print("--- For Loop ---");
  for (int i = 1; i <= 3; i++) {
    print("Count: $i");
  }

  print("\n--- While Loop ---");
  int j = 1;
  while (j <= 3) {
    print("Count: $j");
    j++;
  }

  print("\n--- Do-While Loop ---");
  int k = 1;
  do {
    print("Count: $k");
    k++;
  } while (k <= 3);
}
