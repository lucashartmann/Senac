import java.util.Scanner;

public class App {

    Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        App app = new App();
        //app.algoritmoUm();
        //app.algoritmoDois();
        //app.algoritmoTres();
        //app.algoritmoQuatro();
        //app.algoritmoCinco();
        app.algoritmoCinco();
    }

    public void algoritmoUm() {
        String nome = "Roberto";
        int count = 0;
        while (count < 10) {
            System.out.println("Nome: " + nome);
            count = count + 1;
        }
    }

    public void algoritmoDois() {
        int numero = 1;
        while (numero <= 1000) {
            System.out.println(numero);
            numero = numero + 1;
        }
    }

    public void algoritmoTres() {
        int count = 1;
        while (count <= 10) {
            System.out.println(count + " * 9 = " + (count * 9));
            count++;
        }
    }

    public void algoritmoQuatro() {
        int numero;
        int count = 1;
        System.out.println("Digite um valor");
        numero = sc.nextInt();
        while (count <= 10) {
            System.out.println(count + " * " + numero + " = " + (count * numero));
            count++;
        }
    }

    public void algoritmoCinco() {
        int n;
        int count = 0;
        int soma = 0;
        System.out.println("Digite um valor");
        n = sc.nextInt();
        while (count <= n) {
            System.out.println(soma + " + " + count + " = " + (soma + count));
            soma = soma + count;
            count = count + 1;
        }
        System.out.println(soma);
    }

}
