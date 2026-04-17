import 'package:flutter/material.dart';

void main() => runApp(const TransitionApp());

class TransitionApp extends StatelessWidget {
  const TransitionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[100],
      appBar: AppBar(title: const Text('Home Screen')),
      body: Center(
        child: ElevatedButton(
          child: const Text('Navigate Forward >>'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const DetailScreen()),
            );
          },
        ),
      ),
    );
  }
}

class DetailScreen extends StatelessWidget {
  const DetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green[100],
      appBar: AppBar(title: const Text('Detail Screen')),
      body: Center(
        child: ElevatedButton(
          child: const Text('<< Navigate Back (Pop)'),
          onPressed: () {
            // POP removes this screen and goes to previous
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}
