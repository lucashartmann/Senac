import 'package:flutter/material.dart';
import '../model/tarefa.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class DetalhesTarefa extends StatelessWidget {
  const DetalhesTarefa({super.key});

  Future<Tarefa?> _get(int id) async {
    http.Response response = await http.get(
      Uri.parse('https://jsonplaceholder.typicode.com/todos/$id'),
    );
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return Tarefa.fromJson(data);
    }
    print("Status detalhes_tarefa _get: ${response.statusCode}");
    return null;
  }

  Future<void> _patch(int id, bool completed) async {
    String corpoJson = json.encode(
      Tarefa(
        userId: null,
        id: null,
        title: 'Título atualizado via PATCH',
        completed: completed,
      ).toJson(),
    );

    http.Response response = await http.patch(
      Uri.parse('https://jsonplaceholder.typicode.com/todos/$id'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: corpoJson,
    );

    print("Status detalhes_tarefa _patch: ${response.statusCode}");
  }

  Future<void> _delete(int id) async {
    http.Response response = await http.delete(
      Uri.parse('https://jsonplaceholder.typicode.com/todos/$id'),
    );
    print("Status detalhes_tarefa _delete: ${response.statusCode}");
  }

  @override
  Widget build(BuildContext context) {
    final id = ModalRoute.of(context)!.settings.arguments as int;

    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Detalhes da Tarefa',
          style: Theme.of(context).textTheme.bodyMedium!.copyWith(
            color: Theme.of(context).colorScheme.onPrimary,
            fontSize: 20,
          ),
        ),
        backgroundColor: Theme.of(context).colorScheme.primary,
      ),
      body: FutureBuilder<Tarefa?>(
        future: _get(id),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.waiting:
              {
                return const Center(child: CircularProgressIndicator());
              }
            case ConnectionState.active:
              {
                return const Center(child: CircularProgressIndicator());
              }
            case ConnectionState.done:
              {
                if (snapshot.hasError) {
                  return Center(child: Text('Erro: ${snapshot.error}'));
                }
                if (!snapshot.hasData || snapshot.data == null) {
                  return const Center(child: Text('Tarefa não encontrada'));
                }

                final tarefa = snapshot.data!;
                return Center(
                  child: Container(
                    width: 300,
                    height: 300,
                    decoration: BoxDecoration(border: Border.all(width: 2)),

                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Text(
                          "ID: $id",
                          style: Theme.of(context).textTheme.bodyMedium!
                              .copyWith(color: Colors.black, fontSize: 17),
                        ),
                        SizedBox(height: 10),
                        Text(
                          "Título: ${tarefa.title}",
                          style: Theme.of(context).textTheme.bodyMedium!
                              .copyWith(color: Colors.black, fontSize: 17),
                        ),
                        SizedBox(height: 10),
                        Text(
                          "Concluída: ${tarefa.completed ? 'Sim' : 'Não'}",
                          style: Theme.of(context).textTheme.bodyMedium!
                              .copyWith(color: Colors.black, fontSize: 17),
                        ),
                        SizedBox(height: 50),
                        Column(
                          children: [
                            ElevatedButton(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Theme.of(
                                  context,
                                ).colorScheme.primary,
                                foregroundColor: Theme.of(
                                  context,
                                ).colorScheme.onPrimary,
                                minimumSize: Size(150, 43),
                              ),

                              onPressed: () async {
                                bool resultado = !tarefa.completed;
                                await _patch(id, resultado);
                                if (context.mounted) {
                                  Navigator.popAndPushNamed(context, '/');
                                }
                              },
                              child: Text("Concluir/Reverter"),
                            ),
                            SizedBox(height: 10),
                            ElevatedButton(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Colors.red,
                                foregroundColor: Colors.white,
                                minimumSize: Size(150, 43),
                              ),
                              onPressed: () async {
                                await _delete(id);
                                if (context.mounted) {
                                  Navigator.popAndPushNamed(context, '/');
                                }
                              },
                              child: Text("Excluir"),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                );
              }
            default:
              {
                return const Center(child: Text('Aguardando dados...'));
              }
          }
        },
      ),
    );
  }
}
