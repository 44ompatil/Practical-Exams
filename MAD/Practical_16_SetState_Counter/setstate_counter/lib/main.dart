import 'package:flutter/material.dart';

void main() => runApp(const CounterApp());

class CounterApp extends StatelessWidget {
  const CounterApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: CounterScreen(),
    );
  }
}

class CounterScreen extends StatefulWidget {
  const CounterScreen({super.key});

  @override
  State<CounterScreen> createState() => _CounterScreenState();
}

class _CounterScreenState extends State<CounterScreen> {
  int _value = 0;

  void _increment() {
    // setState forces the screen to rebuild and show the new _value
    setState(() {
      _value++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('setState() Demo')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('You pushed the button this many times:'),
            Text('$_value', style: const TextStyle(fontSize: 48, fontWeight: FontWeight.bold)),
            ElevatedButton(
              onPressed: _increment,
              child: const Text('Increment'),
            )
          ],
        ),
      ),
    );
  }
}
