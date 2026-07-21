import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key, required this.title});

  final String title;

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  late String _textoResultado = "";

  @override
  void dispose() {
    _controllerAlcool.dispose();
    _controllerGasolina.dispose();
    super.dispose();
  }

  void _calcular() {
    double? precoAlcool = double.tryParse(
      _controllerAlcool.text.replaceAll("R\$", "").replaceAll(",", ".").trim(),
    );
    double? precoGasolina = double.tryParse(
      _controllerGasolina.text
          .replaceAll("R\$", "")
          .replaceAll(",", ".")
          .trim(),
    );

    print("Preço Álcool: $precoAlcool");
    print("Preço Gasolina: $precoGasolina");

    if (precoAlcool == null ||
        precoGasolina == null ||
        precoAlcool <= 0 ||
        precoGasolina <= 0) {
      setState(() {
        _textoResultado =
            "Por favor, insira valores válidos para ambos os preços.";
      });
      return;
    }

    double resultado = precoAlcool / precoGasolina;

    setState(() {
      _textoResultado = (resultado >= 0.7)
          ? "Melhor abastecer com Gasolina"
          : "Melhor abastecer com Álcool";
    });
  }

  void _limparCampos() {
    _controllerAlcool.clear();
    _controllerGasolina.clear();
    setState(() {
      _textoResultado = "";
    });
  }

  final TextEditingController _controllerAlcool = TextEditingController();
  final TextEditingController _controllerGasolina = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
        backgroundColor: Color(0xFF1D3E97),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(32),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.only(bottom: 32),
              child: Center(child: Image.asset("assets/images/logo.png")),
            ),
            const Padding(
              padding: EdgeInsets.only(bottom: 20),
              child: Text(
                "Saiba qual a melhor opção para o abastecimento do seu veículo",
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
              ),
            ),
            TextField(
              keyboardType: const TextInputType.numberWithOptions(
                decimal: true,
              ),
              decoration: const InputDecoration(
                labelText: "Preço Álcool, ex: 4.06",
                border: OutlineInputBorder(),
                prefixText: "R\$",
              ),
              style: const TextStyle(fontSize: 22),
              controller: _controllerAlcool,
            ),
            const SizedBox(height: 16),
            TextField(
              keyboardType: const TextInputType.numberWithOptions(
                decimal: true,
              ),
              decoration: const InputDecoration(
                labelText: "Preço Gasolina, ex: 6.10",
                border: OutlineInputBorder(),
                prefixText: "R\$",
              ),
              style: const TextStyle(fontSize: 22),
              controller: _controllerGasolina,
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Color(0xFF1D3E97),
                foregroundColor: Colors.white,
                padding: const EdgeInsets.all(16),
                textStyle: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              onPressed: _calcular,
              child: const Text("Calcular"),
            ),
            const SizedBox(height: 12),
            OutlinedButton(
              style: OutlinedButton.styleFrom(
                backgroundColor: Colors.grey,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.all(16),
                textStyle: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              onPressed: _limparCampos,
              child: const Text("Limpar"),
            ),
            const SizedBox(height: 24),
            Text(
              _textoResultado,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.green,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
