import 'package:flutter/material.dart';
import 'view/home.dart';
import 'view/detalhes_tarefa.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      initialRoute: '/',
      routes: {
        '/': (context) => const Home(),
        '/detalhes': (context) =>  const DetalhesTarefa(), 
      },
    );
  }
}

