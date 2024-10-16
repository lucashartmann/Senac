package Interface;

import Dados.Jogador;
import Dados.Tabuleiro;
import Dados.Tipo;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.geometry.Bounds;
import java.util.ArrayList;
import java.util.List;

public class Jogo extends Application {

    private ImageView jogadorView;
    private ImageView tabuleiroView;
    private List<ImageView> inimigos;
    private Scene scene;
    private Pane root;
    private Jogador cacador;
    private Tabuleiro tabuleiro;

    @Override
    public void start(Stage primaryStage) {
        root = new Pane();
        jogadorView = new ImageView(new Image("/Imagens/jogador.png"));
        tabuleiroView = new ImageView(new Image("/Imagens/tabuleiro.png"));
        scene = new Scene(root, 600, 600);
        inimigos = new ArrayList<>();

        tabuleiroView.setFitWidth(600);
        tabuleiroView.setFitHeight(600);
        tabuleiroView.setPreserveRatio(true);
        tabuleiroView.setSmooth(true);
        root.getChildren().add(tabuleiroView);

        jogadorView.setFitWidth(50);
        jogadorView.setFitHeight(50);
        jogadorView.setX(100);
        jogadorView.setY(100);
        jogadorView.setScaleX(1); 
        root.getChildren().add(jogadorView);

        tabuleiro = new Tabuleiro(tabuleiroView);
        cacador = new Jogador(18, Tipo.CAÇADOR, jogadorView);
        tabuleiro.add(cacador);

        for (int i = 0; i < 5; i++) {
            ImageView inimigo = new ImageView(new Image("/Imagens/zumbi.png"));
            inimigo.setFitWidth(50);
            inimigo.setFitHeight(50);
            inimigo.setX(200 + (i * 60));
            inimigo.setY(400);
            root.getChildren().add(inimigo);
            inimigos.add(inimigo);
            Jogador zumbi = new Jogador(6, Tipo.ZUMBI, inimigo);
            tabuleiro.add(zumbi);
        }

        scene.setOnKeyPressed(event -> {
            if (event.getCode() == KeyCode.UP) {
                jogadorView.setY(jogadorView.getY() - 10);
                jogadorView.setRotate(0);
                jogadorView.setRotate(-270);
            } else if (event.getCode() == KeyCode.DOWN) {
                jogadorView.setY(jogadorView.getY() + 10);
                jogadorView.setRotate(0);
                jogadorView.setRotate(270);
            } else if (event.getCode() == KeyCode.LEFT) {
                jogadorView.setX(jogadorView.getX() - 10);
                jogadorView.setRotate(0);
                jogadorView.setScaleX(1);
                jogadorView.setScaleY(1);
            } else if (event.getCode() == KeyCode.RIGHT) {
                jogadorView.setX(jogadorView.getX() + 10);
                jogadorView.setRotate(0);
                jogadorView.setScaleX(-1);
            }
            for (ImageView inimigo : inimigos) {
                if (verificaColisao(jogadorView, inimigo)) {
                    System.out.println("Colisão com zumbi!");
                    iniciarCombate();
                }
            }

        });

        primaryStage.setTitle("Jogo com JavaFX");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public void iniciarCombate() {
        for (ImageView inimigo : inimigos) {
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
                if (tabuleiro != null && (!tabuleiro.isEmpty()) && tabuleiro.contains(cacador)) {
                    tabuleiro.remove(cacador);
                }
                root.getChildren().remove(jogadorView);
            } else if (zumbiNew.getVidas() <= 0) {
                if (tabuleiro != null && (!tabuleiro.isEmpty()) && tabuleiro.contains(zumbiNew)) {
                    tabuleiro.remove(zumbiNew);
                }
                root.getChildren().remove(inimigo);
                if (inimigos != null && (!inimigos.isEmpty()) && inimigos.contains(inimigo)) {
                    inimigos.remove(inimigo);
                }
            }
            break;
        }
    }

    public boolean verificaColisao(ImageView jogador, ImageView inimigo) {
        Bounds boundsJogador = jogador.getBoundsInParent();
        Bounds boundsInimigo = inimigo.getBoundsInParent();
        return boundsJogador.intersects(boundsInimigo);
    }

    public void pausar(long milliseconds) {
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public void executar(String[] args) {
        launch(args);
    }
}
