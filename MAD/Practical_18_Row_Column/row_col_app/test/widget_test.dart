import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:row_col_app/main.dart';

void main() {
  testWidgets('Icons test', (WidgetTester tester) async {
    await tester.pumpWidget(const RowColApp());
    expect(find.byIcon(Icons.star), findsWidgets);
    expect(find.byIcon(Icons.favorite), findsWidgets);
  });
}
