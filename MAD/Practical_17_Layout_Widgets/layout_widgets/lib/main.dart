import 'package:flutter/material.dart';

void main() => runApp(const LayoutApp());

class LayoutApp extends StatelessWidget {
  const LayoutApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: LayoutScreen(),
    );
  }
}

class LayoutScreen extends StatelessWidget {
  const LayoutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Layout Widgets Demo')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(20),
            color: Colors.blueAccent,
            child: const Text('I am in a Container', style: TextStyle(color: Colors.white)),
          ),
          const SizedBox(height: 20),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(color: Colors.red, padding: const EdgeInsets.all(10), child: const Text('Row Item 1')),
              Container(color: Colors.green, padding: const EdgeInsets.all(10), child: const Text('Row Item 2')),
            ],
          )
        ],
      ),
    );
  }
}
