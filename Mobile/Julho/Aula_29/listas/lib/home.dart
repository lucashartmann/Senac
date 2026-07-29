import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final List<Map<String, dynamic>> _itens = [];

  void _carregarItens() {
    _itens.clear();

    for (int i = 0; i <= 10; i++) {

      final Map<String, dynamic> item = {
        "titulo" : "Título $i Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "descricao" : "Descrição $i Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      };

      _itens.add(item);
    }
  }

  @override
  void initState() {
    super.initState();
    _carregarItens();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Listas')),
      body: ListView.builder(
        itemCount: _itens.length,
        itemBuilder: (context, index) {
          final item = _itens[index];
          return ListTile(
            title: Text(item['titulo'] as String),
            subtitle: Text(item['descricao'] as String),
          );
        },
      ),
    );
  }
}
