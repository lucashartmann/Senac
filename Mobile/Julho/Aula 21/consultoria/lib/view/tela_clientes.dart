import 'package:flutter/material.dart';

class TelaClientes extends StatefulWidget {
  const TelaClientes({super.key, required this.title});

  final String title;

  @override
  State<TelaClientes> createState() => _TelaClientesState();
}


class _TelaClientesState extends State<TelaClientes> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 21, 150, 51),
        title: Text(widget.title, style: const TextStyle(color: Colors.white)),
      ),
      body: null,
    );
  }
}
