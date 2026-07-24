import 'package:flutter/material.dart';
import 'tela_empresa.dart';
import 'tela_cliente.dart';
import 'tela_contato.dart';
import 'tela_servico.dart';

class TelaInicial extends StatefulWidget {
  const TelaInicial({super.key, required this.title});

  final String title;

  @override
  State<TelaInicial> createState() => _TelaInicialState();
}

void _navigateTo(BuildContext context, int index) {
  // if (index == widget.currentIndex) {
  //   return;
  // }

  Widget destino;

  switch (index) {
    case 0:
      destino = const TelaEmpresa();
      break;
    case 1:
      destino = const TelaServico();
      break;
    case 2:
      destino = const TelaCliente();
      break;
    case 3:
      destino = const TelaContato();
      break;
    default:
      return;
  }

  Navigator.push(context, MaterialPageRoute(builder: (context) => destino));
}

class _TelaInicialState extends State<TelaInicial> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        title: Text(widget.title, style: const TextStyle(color: Colors.white)),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Image.asset('assets/images/logo.png', alignment: Alignment.center),

            GridView.count(
              crossAxisCount: 2,
              crossAxisSpacing: 0.6,
              mainAxisSpacing: 0.6,
              shrinkWrap: true,
              children: <Widget>[
                InkWell(
                  onTap: () => _navigateTo(context, 0),
                  child: Image.asset('assets/images/menu_empresa.png'),
                ),
                InkWell(
                  onTap: () => _navigateTo(context, 1),
                  child: Image.asset('assets/images/menu_servico.png'),
                ),
                InkWell(
                  onTap: () => _navigateTo(context, 2),
                  child: Image.asset('assets/images/menu_cliente.png'),
                ),
                InkWell(
                  onTap: () => _navigateTo(context, 3),
                  child: Image.asset('assets/images/menu_contato.png'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
