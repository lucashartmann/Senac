import 'package:flutter/material.dart';

class TelaInicial extends StatelessWidget {
  const TelaInicial({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tela Inicial'), backgroundColor: Colors.teal,),
      body: Container(
        padding: const EdgeInsets.all(32),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/secundaria');
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.all(15),
              ),
              child: const Text('Ir para a segunda tela'),
            ),
          ],
        ),
      ),
    );
  }
}
