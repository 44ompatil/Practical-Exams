import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:navigator_demo/main.dart';

void main() {
  testWidgets('Navigator push test', (WidgetTester tester) async {
    await tester.pumpWidget(const NavApp());
    expect(find.text('Go to Second Screen'), findsOneWidget);
    await tester.tap(find.text('Go to Second Screen'));
    await tester.pumpAndSettle(); // settle animation
    expect(find.text('Welcome to Screen 2!'), findsOneWidget);
  });
}
