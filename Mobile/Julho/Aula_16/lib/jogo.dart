import 'package:flutter/material.dart';
import 'dart:math';

class Jogo extends StatefulWidget {
  const Jogo({Key? key}) : super(key: key);

  @override
  State<Jogo> createState() => _JogoState();
} // fecha o construtor

class _JogoState extends State<Jogo> {
  // Declarações de Variáveis
  String _caminhoImagemApp = "assets/images/padrao.png";
  String _mensagem = "Escolha uma opção abaixo";

  final Random _random = Random();

  // Metodo de escolha do usuário
  void _opcaoSelecionada(String escolhaUsuario) {
    final List<String> opcoes = ["pedra", "papel", "tesoura"];
    final int numero = _random.nextInt(3);
    final String escolhaApp = opcoes[numero];

    debugPrint("Escolha do App: $escolhaApp");
    debugPrint("Escolha do usuário: $escolhaUsuario");

    String novaImagem = "assets/images/padrao.png";
    switch (escolhaApp) {
      case "pedra":
        novaImagem = "assets/images/pedra.png";
        break;
      case "papel":
        novaImagem = "assets/images/papel.png";
        break;
      case "tesoura":
        novaImagem = "assets/images/tesoura.png";
        break;
    } // Fecha o switch

    String resultado = "";
    if (escolhaUsuario == escolhaApp) {
      resultado = "Empatamos :)";
    } else if ((escolhaUsuario == "pedra" && escolhaApp == "tesoura") ||
        (escolhaUsuario == "tesoura" && escolhaApp == "papel") ||
        (escolhaUsuario == "papel" && escolhaApp == "pedra")) {
      resultado = "Parabéns!!! Você ganhou :)";
    } else {
      resultado = "Você perdeu :(";
    } // Fecha a estrutura if/else if/else

    setState(() {
      _caminhoImagemApp = novaImagem;
      _mensagem = resultado;
    });
  } // Fecha o metodo _opcaoSelecionada

  // Interface do App
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Jokenpo"),
        centerTitle: true,
        backgroundColor: Colors.deepPurple,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const Text(
            "Escolha do App",
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: Colors.deepPurple,
            ),
          ),

          const SizedBox(height: 20),

          Image.asset(
            _caminhoImagemApp,
            height: 150,
            width: 150,
            fit: BoxFit.contain,
          ),

          const SizedBox(height: 30),

          Text(
            _mensagem,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.black87,
            ),
          ),

          const SizedBox(height: 50),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildOpcaoButton("pedra", "assets/images/pedra.png"),
              _buildOpcaoButton("papel", "assets/images/papel.png"),
              _buildOpcaoButton("tesoura", "assets/images/tesoura.png"),
            ], //Fecha a lista de filhos da Row
          ),
        ], // Fecha a lista de filhos da Column
      ),
    );
  } //fecha o metodo build

  Widget _buildOpcaoButton(String opcao, String caminhoImagem) {
    return GestureDetector(
      onTap: () => _opcaoSelecionada(opcao),
      child: Image.asset(
        caminhoImagem,
        height: 100,
        width: 100,
        fit: BoxFit.contain,
      ),
    );
  } // fecha o metodo _buildOpcaoButton
}
