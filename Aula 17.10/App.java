public class App {

    public static void main(String[] args) {
        divisor();
    }

    public static void divisor() {
        int number = 0;
        int divisao = number % 5;
        while (12 < number && number < 64 && divisao == 0) {
            System.out.println(number);
            number = number + 5;
        }
    }
}