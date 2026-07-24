import 'package:flutter/material.dart';

class TelaEmpresa extends StatelessWidget {
  const TelaEmpresa({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text("Empresa"),
        backgroundColor: Colors.deepOrange,
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Row(
                children: <Widget>[
                  Image.asset("assets/images/detalhe_empresa.png"),
                  Padding(
                    padding: EdgeInsets.only(left: 10),
                    child: Text(
                      "Sobre a empresa",
                      style: TextStyle(
                        fontSize: 20,
                        color: Colors.deepOrange,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              Padding(
                padding: EdgeInsets.only(top: 16),
                child: Text(
                  "A ATM Consultoria é uma empresa dedicada a oferecer as melhores soluções em consultoria empresarial. "
                  "Com anos de experiência no mercado, nossa missão é ajudar seu negócio a alcançar novos patamares "
                  "de sucesso e produtividade através de estratégias inovadoras e personalizadas.",
                  textAlign: TextAlign.justify,
                ),
              ),
            ], // Fecha Children
          ),
        ),
      ),
    ); // Fecha Scaffold
  } // Fecha o build
} // Fecha a classe TelaEmpresa
