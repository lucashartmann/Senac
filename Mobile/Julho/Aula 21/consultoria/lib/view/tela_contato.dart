import 'package:flutter/material.dart';

class TelaContato extends StatefulWidget {
  const TelaContato({super.key, required this.title});

  final String title;

  @override
  State<TelaContato> createState() => _TelaContatoState();
}


class _TelaContatoState extends State<TelaContato> {
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