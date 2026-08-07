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
  final url = 'https://jsonplaceholder.typicode.com/todos';

  Future<List<Tarefa>> _get() async {
    List<Tarefa> tarefas = [];
    http.Response response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      for (var item in data) {
        tarefas.add(Tarefa.fromJson(item));
      }
    }

    print("Status home _get: ${response.statusCode}");
    return tarefas;
  }

  Future<void> _post() async {
    String corpoJson = json.encode(
      Tarefa(
        title: 'Titulo da nova tarefa via Flutter',
        id: null,
        userId: 120,
        completed: false,
      ).toJson(),
    );

    http.Response response = await http.post(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status home _post: ${response.statusCode}");
  }

  Future<void> _patch(int id) async {
    String corpoJson = json.encode(
      Tarefa(
        userId: null,
        id: null,
        title: 'Título atualizado via PATCH',
        completed: true,
      ).toJson(),
    );

    http.Response response = await http.patch(
      Uri.parse('$url/$id'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status home _patch: ${response.statusCode}");
  }

  Future<void> _delete(int id) async {
    http.Response response = await http.delete(Uri.parse('$url/$id'));
    print("Status home _delete: ${response.statusCode}");
  }

  void abrirDialog() {
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
              style: ElevatedButton.styleFrom(
                backgroundColor: Theme.of(context).colorScheme.primary,
                foregroundColor: Theme.of(context).colorScheme.onPrimary,
              ),
              child: const Text('Cancelar'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Theme.of(context).colorScheme.primary,
                foregroundColor: Theme.of(context).colorScheme.onPrimary,
              ),
              child: const Text('Salvar'),
              onPressed: () async {
                try {
                  await _post();
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
      appBar: AppBar(
        title: Text(
          'Home',
          style: Theme.of(context).textTheme.bodyMedium!.copyWith(
            color: Theme.of(context).colorScheme.onPrimary,
            fontSize: 20,
          ),
        ),
        backgroundColor: Theme.of(context).colorScheme.primary,
      ),
      body: Container(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Row(
                children: [
                  ElevatedButton(
                    onPressed: abrirDialog,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Theme.of(context).colorScheme.primary,
                      foregroundColor: Theme.of(context).colorScheme.onPrimary,
                    ),
                    child: Text("Nova Tarefa"),
                  ),
                ],
              ),
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
                        return const Center(
                          child: Text('Nenhuma tarefa encontrada'),
                        );
                      } else {
                        List<Tarefa> tarefas = snapshot.data!;
                        return ListView.builder(
                          itemCount: tarefas.length,
                          itemBuilder: (context, index) {
                            final tarefa = tarefas[index];
                            return Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Card(
                                child: ListTile(
                                  onTap: () {
                                    Navigator.pushNamed(
                                      context,
                                      '/detalhes',
                                      arguments: tarefa.id,
                                    );
                                  },
                                  title: Text(
                                    tarefa.title,
                                    style: tarefa.completed
                                        ? TextStyle(
                                            decoration:
                                                TextDecoration.lineThrough,
                                            color: Colors.grey,
                                          )
                                        : null,
                                  ),
                                  subtitle: Text(
                                    'Concluída: ${tarefa.completed}',
                                  ),
                                ),
                              ),
                            );
                          },
                        );
                      }
                    default:
                      return const Center(child: Text('Aguardando dados...'));
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
