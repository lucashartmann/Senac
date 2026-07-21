import 'package:flutter/material.dart';
import 'view/tela_inicial.dart';
import 'view/tela_empresa.dart';
import 'view/tela_clientes.dart';
import 'view/tela_contato.dart';
import 'view/tela_servicos.dart';

void main() {
  runApp(const MyApp());
}

// void trocarTela(BuildContext context, String nomeRota) {
//   switch (nomeRota) {
//     case '/empresa':
//       Navigator.pushNamed(context, '/empresa');
//       break;
//     case '/servico':
//       Navigator.pushNamed(context, '/servico');
//       break;
//     case '/cliente':
//       Navigator.pushNamed(context, '/cliente');
//       break;
//     case '/contato':
//       Navigator.pushNamed(context, '/contato');
//       break;
//   }
// }

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
