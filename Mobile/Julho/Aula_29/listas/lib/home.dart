import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:currency_formatter/currency_formatter.dart';
import 'dart:async';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final List<Map<String, dynamic>> _itens = [];
  String _precoBRL = "0";
  String _precoUSD = "0";
  Color _cor = Colors.black;
  Timer? _timer;

  Future<Map<String, dynamic>> _atualizarPreco() async {
    http.Response response = await http.get(
      Uri.parse('https://blockchain.info/ticker'),
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Falha ao recuperar preço');
    }
  }

  void formatarPreco() {
    CurrencyFormat brlSettings = CurrencyFormat(
      code: 'brl',
      symbol: 'R\$',
      symbolSide: SymbolSide.left,
      thousandSeparator: '.',
      decimalSeparator: ',',
      symbolSeparator: ' ',
    );
    _precoBRL = CurrencyFormatter.format(_precoBRL, brlSettings);
    _precoUSD = CurrencyFormatter.format(_precoUSD, CurrencyFormat.usd);
  }

  void _carregarItens() {
    _itens.clear();

    for (int i = 0; i <= 10; i++) {
      final Map<String, dynamic> item = {
        "titulo":
            "Título $i Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "descricao":
            "Descrição $i Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
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

  void _exibirMensagem(int index, BuildContext context) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: Colors.white,
          title: Text(
            "Confirmação",
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
          ),
          content: Text(
            "Titulo: ${_itens[index]['titulo']}\n\nDescrição: ${_itens[index]['descricao']}\n\nDeseja confirmar a ação?",
          ),
          actions: [
            TextButton(
              style: TextButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: const Color.fromARGB(255, 206, 54, 43),
              ),
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Não'),
            ),
            TextButton(
              style: TextButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: const Color.fromARGB(255, 43, 27, 3),
              ),
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Sim'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text(
          'Preço do Bitcoin (FutureBuilder)',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: const Color.fromARGB(255, 43, 27, 3),
      ),
      body: FutureBuilder<Map<String, dynamic>>(
        future: _atualizarPreco(),
        builder: (context, snapshot) {
          String resultado = "";
          switch (snapshot.connectionState) {
            case ConnectionState.none:
              resultado = "Sem conexão com o FutureBuilder";
              break;
            case ConnectionState.waiting:
              resultado = "Aguardando conexão com o FutureBuilder";
              break;
            case ConnectionState.active:
              resultado = "Conexão ativa com o FutureBuilder";
              break;
            case ConnectionState.done:
              if (snapshot.hasError) {
                resultado = "Erro ao conectar com o FutureBuilder";
              } else {
                resultado = "Conexão finalizada com o FutureBuilder";
                final data = snapshot.data;
                if (data != null &&
                    data.containsKey('BRL') &&
                    data.containsKey('USD')) {
                  _precoBRL = data['BRL']['buy'].toStringAsFixed(2);
                  _precoUSD = data['USD']['buy'].toStringAsFixed(2);
                  double precoBRL = double.parse(data['BRL']['buy'].toString());
                  double precoUSD = double.parse(data['USD']['buy'].toString());
                  formatarPreco();
                  resultado =
                      "Preço do Bitcoin:\n\nBRL: ${_precoBRL}\n\nUSD: ${_precoUSD}";
                } else {
                  resultado = "Dados inválidos recebidos do FutureBuilder";
                }
              }
              break;
          }
          return Center(
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Text(
                resultado,
                style: const TextStyle(fontSize: 20, color: Colors.black),
                textAlign: TextAlign.center,
              ),
            ),
          );
        },
      ),
    );
  }

  // @override
  // Widget build(BuildContext context) {
  //   return Scaffold(
  //     backgroundColor: Colors.white,
  //     appBar: AppBar(
  //       title: const Text('Preço do Bitcoin (FutureBuilder)', style: TextStyle(color: Colors.white)),
  //       backgroundColor: const Color.fromARGB(255, 43, 27, 3),
  //     ),
  //     body: Container(
  //       padding: const EdgeInsets.all(20),
  //       child: ListView.builder(
  //         physics: const ClampingScrollPhysics(),
  //         itemCount: _itens.length,
  //         itemBuilder: (context, index) {
  //           final item = _itens[index];
  //           return Padding(
  //             padding: const EdgeInsets.all(8.0),
  //             child: ListTile(
  //               tileColor: Colors.grey[200],
  //               textColor: Colors.black,
  //               title: Text(item['titulo'] as String),
  //               subtitle: Text(item['descricao'] as String),
  //               onTap: () {
  //                 _exibirMensagem(index, context);
  //               },
  //               onLongPress: () {
  //                 print('Item pressionado: ${item['titulo']}');
  //               },
  //             ),
  //           );
  //         },
  //       ),
  //     ),
  //   );
  // }
}
