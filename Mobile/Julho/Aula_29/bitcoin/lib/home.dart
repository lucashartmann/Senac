// import 'dart:nativewrappers/_internal/vm/lib/async_patch.dart';
import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'dart:async';
import 'package:currency_formatter/currency_formatter.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String _precoBRL = "0";
  String _precoUSD = "0";
  Color _cor = Colors.black;
  Timer? _timer;

  Future<void> _atualizarPreco() async {
    var url = Uri.parse("https://blockchain.info/ticker");
    http.Response response = await http.get(url);
    Map<String, dynamic> data = jsonDecode(response.body);
    setState(() {
      if (_precoBRL != "0") {
        if (double.parse(data['BRL']['buy'].toString()) <
            double.parse(_precoBRL.split("R\$")[1].replaceAll(".", ",").replaceAll(",", ""))) {
          _cor = const Color.fromARGB(255, 165, 2, 2);
        } else {
          _cor = const Color.fromARGB(255, 22, 112, 4);
        }
      }

      _precoBRL = data['BRL']['buy'].toString();
      _precoUSD = data['USD']['buy'].toString();
    });
    formatarPreco();
  }

  @override
  void initState() {
    super.initState();
    _atualizarPreco();
    _timer = Timer.periodic(const Duration(seconds: 5), (timer) {
      _atualizarPreco();
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void formatarPreco() {
    // _precoBRL = double.parse(_precoBRL).toStringAsFixed(2);
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 247, 147, 26),
      appBar: AppBar(
        title: const Text(
          "Preço do Bitcoin",
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.black,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Image.asset("assets/bitcoin.png"),
            Padding(
              padding: const EdgeInsets.only(top: 60, bottom: 0),
              child: RichText(
                text: TextSpan(
                  text: "R\$",
                  style: TextStyle(fontSize: 35, color: Colors.black),
                  children: [
                    TextSpan(
                      text: _precoBRL != "0" ? _precoBRL.split("R\$")[1] : "0",
                      style: TextStyle(fontSize: 35, color: _cor),
                    ),
                  ],
                ),
              ),
            ),

            Padding(
              padding: const EdgeInsets.only(top: 10, bottom: 30),
              child: RichText(
                text: TextSpan(
                  text: "US\$",
                  style: TextStyle(fontSize: 35, color: Colors.black),
                  children: [
                    TextSpan(
                      text: _precoUSD != "0" ? _precoUSD.split("\$")[1] : "0",
                      style: TextStyle(fontSize: 35, color: _cor),
                    ),
                  ],
                ),
              ),
            ),

            ElevatedButton(
              onPressed: _atualizarPreco,
              child: const Text(
                "Atualizar",
                style: TextStyle(
                  fontSize: 20,
                  backgroundColor: Color.fromARGB(15, 224, 132, 19),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
