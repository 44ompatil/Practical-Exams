import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:stateful_app/main.dart';

void main() {
  testWidgets('Counter increments', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());
    expect(find.text('Counter Value: 0'), findsOneWidget);
    await tester.tap(find.byType(FloatingActionButton));
    await tester.pump();
    expect(find.text('Counter Value: 1'), findsOneWidget);
  });
}
