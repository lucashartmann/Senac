import 'package:flutter/material.dart';
import 'package:aula_28/tela_inicial.dart';
import 'package:aula_28/tela_secundaria.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const TelaInicial(),
        '/secundaria': (context) => const TelaSecundaria(),
      },
      title: 'Flutter Demo',
    );
  }
}
