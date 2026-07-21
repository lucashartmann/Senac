import 'package:flutter/material.dart';

class TelaEmpresa extends StatefulWidget {
  const TelaEmpresa({super.key, required this.title});

  final String title;

  @override
  State<TelaEmpresa> createState() => _TelaEmpresaState();
}


class _TelaEmpresaState extends State<TelaEmpresa> {
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