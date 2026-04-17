import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:setstate_counter/main.dart';

void main() {
  testWidgets('setState works', (WidgetTester tester) async {
    await tester.pumpWidget(const CounterApp());
    expect(find.text('0'), findsOneWidget);
    await tester.tap(find.byType(ElevatedButton));
    await tester.pump();
    expect(find.text('1'), findsOneWidget);
  });
}
