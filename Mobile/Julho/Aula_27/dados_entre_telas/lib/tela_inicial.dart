import 'package:flutter/material.dart';
import 'tela_moeda.dart';

class TelaInicial extends StatelessWidget {
  const TelaInicial({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Tela Inicial de Sorteio'),
        backgroundColor: Color(0xFF5CB88C),
      ),
      body: Container(
        padding: const EdgeInsets.all(32),
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              "Clique na imagem para jogar a moeda!",
              style: TextStyle(fontSize: 18),
            ),
            SizedBox(height: 20),
            InkWell(
              child: Image.asset("assets/logo.png"),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const TelaSecundaria(valor: 'Lucas'),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
