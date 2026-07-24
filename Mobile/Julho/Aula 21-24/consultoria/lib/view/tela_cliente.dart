import 'package:flutter/material.dart';

class TelaCliente extends StatelessWidget {
  const TelaCliente({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: const Text("Clientes"),
        backgroundColor: Colors.green[300],
      ),

      body: SingleChildScrollView(
        child: Container(
          padding: EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Row(
                children: <Widget>[
                  Image.asset("assets/images/detalhe_cliente.png"),
                  Padding(
                    padding: EdgeInsets.only(left: 10),
                    child: Text(
                      "Clientes",
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),

              Padding(
                padding: EdgeInsets.only(top: 16),
                child: Text(
                  "Empresa de Software XPTO",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
              Text("Desenvolvimento de soluções tecnológicas sob medida."),

              Padding(
                padding: EdgeInsets.only(top: 16),
                child: Text(
                  "Auditoria Contábil Silva",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
              Text("Consultoria financeira e revisão de processos."),
            ],
          ),
        ),
      ),
    );
  }
}
