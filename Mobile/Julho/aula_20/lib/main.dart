import 'package:flutter/material.dart';
import 'home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Álcool ou Gasolina',
      theme: ThemeData(primaryColor: Color(0xFF1D3E97), useMaterial3: true),
      home: const Home(title: 'Álcool ou Gasolina'),
      debugShowCheckedModeBanner: false,
    );
  }
}
