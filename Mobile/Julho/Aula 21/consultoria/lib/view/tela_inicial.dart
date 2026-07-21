import 'package:flutter/material.dart';
import './tela_empresa.dart';
import './tela_clientes.dart';
import './tela_contato.dart';
import './tela_servicos.dart';


class TelaInicial extends StatefulWidget {
  const TelaInicial({super.key, required this.title});

  final String title;

  @override
  State<TelaInicial> createState() => _TelaInicialState();
}

void trocarTela(BuildContext context, String nomeRota) {
  switch (nomeRota) {
    case '/empresa':
      Navigator.pushNamed(context, '/empresa');
      break;
    case '/servico':
      Navigator.pushNamed(context, '/servico');
      break;
    case '/cliente':
      Navigator.pushNamed(context, '/cliente');
      break;
    case '/contato':
      Navigator.pushNamed(context, '/contato');
      break;
  }
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
                InkWell(onTap: () => trocarTela(context, '/empresa'), child: Image.asset('assets/images/menu_empresa.png')),
                InkWell(onTap: () => trocarTela(context, '/servico'), child: Image.asset('assets/images/menu_servico.png')),
                InkWell(onTap: () => trocarTela(context, '/cliente'), child: Image.asset('assets/images/menu_cliente.png')),
                InkWell(onTap: () => trocarTela(context, '/contato'), child: Image.asset('assets/images/menu_contato.png')),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
