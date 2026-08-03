import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'produto.dart';
import 'dart:convert';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final _urlBase = 'https://fakestoreapi.com/products';

  Future<List<Produto>> _getProdutos() async {
    var url = Uri.parse(_urlBase);
    http.Response resposta = await http.get(url);

    if (resposta.statusCode == 200) {
      var json = jsonDecode(resposta.body);
      List<Produto> postagens = [];
      for (var produto in json) {
        if (produto['id'] == null ||
            produto['title'] == null ||
            produto['price'] == null ||
            produto['image'] == null) {
          continue;
        }
        postagens.add(Produto.fromJson(produto));
      }
      return postagens;
    } else {
      throw Exception('Falha ao carregar postagens');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Catálogo de Produtos',
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: const Color.fromARGB(255, 93, 48, 170),
      ),
      body: FutureBuilder(
        future: _getProdutos(),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.none:
              return Center(child: Text('Não foi possível conectar'));
            case ConnectionState.waiting:
              return Center(child: CircularProgressIndicator());
            case ConnectionState.active:
              return Center(child: CircularProgressIndicator());
            case ConnectionState.done:
              if (snapshot.hasData) {
                final List<Produto> produtos = snapshot.data!;
                return ListView.builder(
                  itemCount: produtos.length,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: EdgeInsets.all(8.0),
                      child: ListTile(
                        shape: RoundedRectangleBorder(
                          side: const BorderSide(
                            color: Colors.grey,
                            width: 0.2,
                          ),
                          borderRadius: BorderRadius.circular(8.0),
                        ),
                        tileColor: Colors.grey[100],
                        textColor: Colors.black87,
                        contentPadding: EdgeInsets.symmetric(
                          horizontal: 16.0,
                          vertical: 8.0,
                        ),

                        leading: Image.network(
                          produtos[index].image,
                          width: 45,
                          height: 190,
                          fit: BoxFit.fill,
                        ),

                        title: Text(
                          produtos[index].title,
                          style: TextStyle(
                            fontSize: 17.0,
                            fontWeight: FontWeight.bold,
                          ),
                        ),

                        subtitle: Text(
                          "R\$ " + produtos[index].price.toStringAsFixed(2),
                          style: TextStyle(
                            fontSize: 16.0,
                            fontWeight: FontWeight.normal,
                            color: Colors.green,
                          ),
                        ),

                        trailing: Icon(Icons.shopping_cart_outlined),
                      ),
                    );
                  },
                );
              } else if (snapshot.hasError) {
                return Center(child: Text('Erro: ${snapshot.error}'));
              } else {
                return Center(child: CircularProgressIndicator());
              }
          }
        },
      ),
    );
  }
}
