class Post {
  final int id;
  final String title;
  final price;
  final String image;

  const Post({
    required this.id,
    required this.title,
    required this.price,
    required this.image,
  });

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(
      id: json['id'] as int,
      title: json['title'] as String,
      price: json['price'],
      image: json['image'] as String,
    );
  }
}
