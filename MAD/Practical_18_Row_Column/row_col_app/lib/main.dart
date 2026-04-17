import 'package:flutter/material.dart';

void main() => runApp(const RowColApp());

class RowColApp extends StatelessWidget {
  const RowColApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: GridScreen(),
    );
  }
}

class GridScreen extends StatelessWidget {
  const GridScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Row & Column Design')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: const [
              Icon(Icons.star, size: 50, color: Colors.amber),
              Icon(Icons.star, size: 50, color: Colors.amber),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: const [
              Icon(Icons.favorite, size: 50, color: Colors.red),
              Icon(Icons.favorite, size: 50, color: Colors.red),
            ],
          ),
        ],
      ),
    );
  }
}
