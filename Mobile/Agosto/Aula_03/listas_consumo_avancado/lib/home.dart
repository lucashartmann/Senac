import 'dart:convert';

import 'package:flutter/material.dart';
import 'post.dart';
import 'package:http/http.dart' as http;

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final String _urlBase = 'https://jsonplaceholder.typicode.com/posts';

  Future<List<Post>> _getPostagens() async {
    var url = Uri.parse(_urlBase);
    http.Response resposta = await http.get(url);

    if (resposta.statusCode == 200) {
      var json = jsonDecode(resposta.body);
      List<Post> postagens = [];
      for (var post in json) {
        postagens.add(Post.fromJson(post));
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
          'Consumo de serviço avançado',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.black87,
      ),
      body: FutureBuilder(
        future: _getPostagens(),
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
                final List<Post> postagens = snapshot.data! as List<Post>;
                return ListView.builder(
                  itemCount: postagens.length,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: EdgeInsets.all(8.0),
                      child: ListTile(
                        tileColor: Colors.grey[300],
                        textColor: Colors.black87,
                        contentPadding: EdgeInsets.symmetric(
                          horizontal: 16.0,
                          vertical: 8.0,
                        ),
                        title: Text(
                          postagens[index].title,
                          style: TextStyle(
                            fontSize: 16.0,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        subtitle: Text(
                          postagens[index].body,
                          style: TextStyle(
                            fontSize: 14.0,
                            fontWeight: FontWeight.normal,
                          ),
                        ),
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
