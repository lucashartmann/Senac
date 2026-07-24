import 'package:flutter/material.dart';

class TelaServico extends StatelessWidget {
  const TelaServico({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: const Text("Serviços"),
        backgroundColor: Colors.cyan,
      ),

      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Row(
                children: <Widget>[
                  Image.asset("assets/images/detalhe_servico.png"),
                  Padding(
                    padding: EdgeInsets.only(left: 10),
                    child: Text(
                      "Nossos Serviços",
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),

              // --- Inìcio da lista de serviços ---
              Padding(
                padding: EdgeInsets.only(top: 16),
                child: Text(" Consultoria empresarial"),
              ),

              Padding(
                padding: EdgeInsets.only(top: 8),
                child: Text(" Cálculo de preços"),
              ),

              Padding(
                padding: EdgeInsets.only(top: 8),
                child: Text(" Acompanhamento de projetos"),
              ),

              Padding(
                padding: EdgeInsets.only(top: 8),
                child: Text(" Treinamento de equipes"),
              ),

              // --- Fim da lista de Serviços ---
            ],
          ),
        ),
      ),
    ); // Fecha o Scaffold
  } // Fecha a build
} // Fecha a classe TelaServico
