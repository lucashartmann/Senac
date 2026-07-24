import 'package:flutter/material.dart';
import 'view/tela_inicial.dart';

void main() {
  runApp(const MyApp());
}


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Color.fromARGB(255, 26, 185, 63)),
      ),
      home: const TelaInicial(title: 'ATM Consultoria'),
    );
  }
}
