import java.util.Scanner;

public class App {

    Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        App app = new App();
        //app.algoritmoUm();
        //app.algoritmoDois();
        //app.algoritmoTres();
        //app.algoritmoQuatro();
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
        int numeroInicial = 1;
        int numeroFinal = 1000;

        while (numeroInicial <= numeroFinal) {
            System.out.println(numeroInicial);
            numeroInicial = numeroInicial + 1;
        }
    }

    public void algoritmoTres() {
        int total = 0;
        int count = 1;

        while (count <= 10) {
            total = count * 9;
            System.out.println(total);
            count++;
        }
    }

    public void algoritmoQuatro() {
        int numero;
        int total = 0;
        int count = 1;

        System.out.println("Digite um valor");
        numero = sc.nextInt();

        while (count <= 10) {
            total = count * numero;
            System.out.println(total);
            count++;
        }
    }

    public void algoritmoCinco() {
        int n;
        int count = 0;
        int soma = 0;

        System.out.println("Digite um valor");
        n = sc.nextInt();

        while (count < n) {
            soma = count + n;
            System.out.println("Soma dos números: " + soma);
            count++;
        }
    }
}
