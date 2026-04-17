import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:layout_widgets/main.dart';

void main() {
  testWidgets('Layout widgets exist', (WidgetTester tester) async {
    await tester.pumpWidget(const LayoutApp());
    expect(find.text('I am in a Container'), findsOneWidget);
    expect(find.text('Row Item 1'), findsOneWidget);
    expect(find.text('Row Item 2'), findsOneWidget);
  });
}
