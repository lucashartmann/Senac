import 'dart:math';
import 'package:flutter/material.dart';

class TelaSecundaria extends StatefulWidget {
  final String valor;

  const TelaSecundaria({super.key, required this.valor});

  @override
  State<TelaSecundaria> createState() => _TelaSecundariaState();
}

class _TelaSecundariaState extends State<TelaSecundaria> {
  List imagens = ["assets/moeda_cara.png", "assets/moeda_coroa.png"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Tela Secundária'),
        backgroundColor: Colors.amber,
      ),
      body: Container(
        padding: const EdgeInsets.all(32),
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Image.asset(imagens[Random().nextInt(imagens.length)]),
            SizedBox(height: 50),
            InkWell(
              child: Image.asset(
                "assets/botao_voltar.png",
                height: 30,
                width: 200,
              ),
              onTap: () {
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
    );
  }
}
