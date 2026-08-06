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
    return null;
  }

  Future<void> _patch(int id, bool completed) async {
    Tarefa dadosParaAtualizar = Tarefa(
      userId: null,
      id: null,
      title: 'Título atualizado via PATCH',
      completed: completed,
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

  @override
  Widget build(BuildContext context) {
    final argumento =
        ModalRoute.of(context)!.settings.arguments as Map<String?, String?>?;
    final id = int.tryParse(argumento?['id'] ?? '');
    final Future<Tarefa?> tarefaFuture = id != null
        ? _get(id)
        : Future.value(null);

    return Scaffold(
      appBar: AppBar(title: const Text('Detalhes da Tarefa')),
      body: FutureBuilder<Tarefa?>(
        future: tarefaFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Erro: ${snapshot.error}'));
          }
          if (!snapshot.hasData || snapshot.data == null) {
            return const Center(child: Text('Tarefa não encontrada'));
          }

          final tarefa = snapshot.data!;
          return Column(
            children: [
              Text("ID: $id"),
              Text("Título: Exemplo"),
              Row(
                children: [
                  ElevatedButton(
                    onPressed: () async {
                      bool resultado = !tarefa.completed;
                      await _patch(id!, resultado);
                      Navigator.popAndPushNamed(context, '/');
                    },
                    child: Text("Concluir/Reverter"),
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      await _delete(id!);
                      Navigator.popAndPushNamed(context, '/');
                    },
                    child: Text("Excluir"),
                  ),
                ],
              ),
            ],
          );
        },
      ),
    );
  }
}
