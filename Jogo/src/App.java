import Dados.Jogador;
import Dados.Tipo;
import Interface.Jogo;
import javafx.scene.image.ImageView;
import Dados.Tabuleiro;

public class App {

    private Jogo jogo;
    private Jogador cacador;
    private Jogador zumbi;
    private Tabuleiro tabuleiro;

    public void executar() {
        jogo = new Jogo();
        tabuleiro = new Tabuleiro(jogo.getTabuleiroView());
        cacador = new Jogador(18, Tipo.CAÇADOR, jogo.getJogadorView());
        tabuleiro.add(cacador);
        jogo.executar(null);
        for (ImageView inimigo : jogo.getInimigos()) {
            zumbi = new Jogador(6, Tipo.ZUMBI, inimigo); // Adicione a imagem do zumbi se necessário
            tabuleiro.add(zumbi);
        }
        while (tabuleiro.containsPlayer(cacador) == true) {
            if (jogo.getColisao() == true) {
                iniciarCombate();
            }
        }
    }

    private void iniciarCombate() {
        for (ImageView inimigo : jogo.getInimigos()) {
            Jogador zumbiNew = tabuleiro.getInimigoByImage(inimigo);
            while (cacador.getVidas() > 0 && zumbiNew.getVidas() > 0) {
                cacador.atacar(zumbiNew);
                zumbiNew.atacar(cacador);
                System.out.println("Vida do Caçador: " + cacador.getVidas() +
                        "\nVida do zumbi: " + zumbiNew.getVidas());
                pausar(500);
            }
            if (cacador.getVidas() <= 0) {
                System.out.println("O Caçador foi derrotado!");
            } else if (zumbiNew.getVidas() <= 0) {
                System.out.println("O zumbi foi derrotado!");
                tabuleiro.remove(zumbiNew);
            }
            break;
        }
    }

    private void pausar(long milliseconds) {
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
