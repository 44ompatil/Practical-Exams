import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:screen_trans/main.dart';

void main() {
  testWidgets('Pop transition test', (WidgetTester tester) async {
    await tester.pumpWidget(const TransitionApp());
    await tester.tap(find.text('Navigate Forward >>'));
    await tester.pumpAndSettle();
    expect(find.text('<< Navigate Back (Pop)'), findsOneWidget);
    await tester.tap(find.text('<< Navigate Back (Pop)'));
    await tester.pumpAndSettle();
    expect(find.text('Navigate Forward >>'), findsOneWidget);
  });
}
