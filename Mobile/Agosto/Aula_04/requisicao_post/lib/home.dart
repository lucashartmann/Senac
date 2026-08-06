import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'post.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String _response = '';

  final url = Uri.parse('https://jsonplaceholder.typicode.com/posts');

  Future<List<Post>> _get() async {
    List<Post> postagens = [];
    http.Response response = await http.get(url);
    var dadosJson = json.decode(response.body);

    for (var post in dadosJson) {
      postagens.add(Post.fromJson(post));
    }
    return postagens;
  }

  Future<void> _post() async {
    Map<String, dynamic> dadosParaEnviar = {
      'title': 'Titulo da nova postagem via Flutter',
      'id': null,
      'userId': 120,
      'body': 'Corpo da nova postagem via Flutter',
    };

    String corpoJson = json.encode(dadosParaEnviar);

    http.Response response = await http.post(
      url,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status: ${response.statusCode}");

    setState(() {
      _response = response.body;
    });
  }

  void _put() {
    http.put(
      Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: json.encode({
        'title': 'Título atualizado via PUT',
        'body': 'Corpo atualizado via PUT',
        'userId': 1,
        'id': 1,
      }),
    );
  }

  void _patch() {
    http.patch(
      Uri.parse('https://jsonplaceholder.typicode.com/posts/1'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: json.encode({'title': 'Título atualizado via PATCH'}),
    );
  }

  void _delete() {
    http.delete(Uri.parse('https://jsonplaceholder.typicode.com/posts/4'));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('POST Request Example')),
      body: Container(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Row(
              children: [
                ElevatedButton(onPressed: _post, child: const Text('POST')),
                ElevatedButton(onPressed: _put, child: const Text('PUT')),
                ElevatedButton(onPressed: _patch, child: const Text('PATCH')),
                ElevatedButton(onPressed: _delete, child: const Text('DELETE')),
              ],
            ),
            Expanded(
              child: FutureBuilder(
                future: _get(),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const Center(child: CircularProgressIndicator());
                  } else if (snapshot.hasError) {
                    return Center(child: Text('Error: ${snapshot.error}'));
                  } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                    return const Center(child: Text('No data available'));
                  } else {
                    List<Post> postagens = snapshot.data!;
                    return ListView.builder(
                      itemCount: postagens.length,
                      itemBuilder: (context, index) {
                        final postagem = postagens[index];
                        return ListTile(
                          title: Text(postagem.title),
                          subtitle: Text(postagem.body),
                        );
                      },
                    );
                  }
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
