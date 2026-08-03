class Produto {
  final int id;
  final String title;
  final double price;
  final String image;

  const Produto({
    required this.id,
    required this.title,
    required this.price,
    required this.image,
  });

  factory Produto.fromJson(Map<String, dynamic> json) {
    return Produto(
      id: json['id'] as int,
      title: json['title'] as String,
      price: (json['price'] as num).toDouble(),
      image: json['image'] as String,
    );
  }
}
