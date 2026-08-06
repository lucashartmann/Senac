import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../model/tarefa.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final url = Uri.parse('https://jsonplaceholder.typicode.com/todos');

  Future<List<Tarefa>> _get() async {
    List<Tarefa> tarefas = [];
    http.Response response = await http.get(url);
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      for (var item in data) {
        tarefas.add(Tarefa.fromJson(item));
      }
    }

    // tarefas.sort((a, b) => b.id!.compareTo(a.id!));
    return tarefas;
  }

  Future<void> _post() async {
    Tarefa dadosParaEnviar = Tarefa(
      title: 'Titulo da nova tarefa via Flutter',
      id: null,
      userId: 120,
      completed: false,
    );

    String corpoJson = json.encode(dadosParaEnviar.toJson());

    http.Response response = await http.post(
      url,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status: ${response.statusCode}");
  }

  Future<void> _patch(int id) async {
    Tarefa dadosParaAtualizar = Tarefa(
      userId: null,
      id: null,
      title: 'Título atualizado via PATCH',
      completed: true,
    );

    String corpoJson = json.encode(dadosParaAtualizar.toJson());

    http.Response response = await http.patch(
      Uri.parse('https://jsonplaceholder.typicode.com/todos/$id'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status: ${response.statusCode}");
  }

  Future<void> _delete(int id) async {
    http.Response response = await http.delete(
      Uri.parse('https://jsonplaceholder.typicode.com/todos/$id'),
    );
    print("Status: ${response.statusCode}");
  }

  void abrirForm() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        String titulo = '';
        return AlertDialog(
          title: const Text('Nova Tarefa'),
          content: TextField(
            onChanged: (value) {
              titulo = value;
            },
            decoration: const InputDecoration(hintText: "Digite o título"),
          ),
          actions: <Widget>[
            ElevatedButton(
              child: const Text('Cancelar'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            ElevatedButton(
              child: const Text('Salvar'),
              onPressed: () async {
                try {
                  await _post();
                  setState(() {});
                  if (context.mounted) {
                    Navigator.of(context).pop(true);
                  }
                } catch (e) {
                  print("Erro ao salvar: $e");
                }
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Row(
            children: [
              ElevatedButton(onPressed: abrirForm, child: Text("Nova Tarefa")),
            ],
          ),
          Expanded(
            child: FutureBuilder(
              future: _get(),
              builder: (context, snapshot) {
                switch (snapshot.connectionState) {
                  case ConnectionState.waiting:
                    return const Center(child: CircularProgressIndicator());
                  case ConnectionState.done:
                    if (snapshot.hasError) {
                      return Center(child: Text('Error: ${snapshot.error}'));
                    } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                      return const Center(child: Text('No data available'));
                    } else {
                      List<Tarefa> tarefas = snapshot.data!;
                      return ListView.builder(
                        itemCount: tarefas.length,
                        itemBuilder: (context, index) {
                          final tarefa = tarefas[index];
                          return Card(
                            child: ListTile(
                              onTap: () {
                                Navigator.pushNamed(
                                  context,
                                  '/detalhes',
                                  arguments: {
                                    'id': tarefa.id.toString(),
                                    'title': tarefa.title.toString(),
                                  },
                                );
                              },
                              title: Text(
                                tarefa.title,
                                style: tarefa.completed
                                    ? TextStyle(
                                        decoration: TextDecoration.lineThrough,
                                        color: Colors.grey,
                                      )
                                    : null,
                              ),
                              subtitle: Text('Completed: ${tarefa.completed}'),
                            ),
                          );
                        },
                      );
                    }
                  default:
                    return const SizedBox.shrink();
                }
              },
            ),
          ),
        ],
      ),
    );
  }
}
