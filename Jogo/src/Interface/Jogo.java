package Interface;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.geometry.Bounds;

public class Jogo extends Application {

    private ImageView jogadorView;
    private ImageView tabuleiroView;
    private ImageView[] inimigos;
    private Scene scene;
    private Pane root;
    private boolean colisao;

    @Override
    public void start(Stage primaryStage) {
        root = new Pane();
        jogadorView = new ImageView(new Image("/Imagens/jogador.png"));
        tabuleiroView = new ImageView(new Image("/Imagens/tabuleiro.png"));
        scene = new Scene(root, 600, 600);
        inimigos = new ImageView[3];

        tabuleiroView.setFitWidth(600);
        tabuleiroView.setFitHeight(600);
        tabuleiroView.setPreserveRatio(true);
        tabuleiroView.setSmooth(true);
        root.getChildren().add(tabuleiroView);

        jogadorView.setFitWidth(50);
        jogadorView.setFitHeight(50);
        jogadorView.setX(100);
        jogadorView.setY(100);
        jogadorView.setRotate(0);
        root.getChildren().add(jogadorView);

        for (int i = 0; i < inimigos.length; i++) {
            inimigos[i] = new ImageView(new Image("/Imagens/zumbi.png"));
            inimigos[i].setFitWidth(50);
            inimigos[i].setFitHeight(50);
            inimigos[i].setX(200 + (i * 60));
            inimigos[i].setY(400);
            root.getChildren().add(inimigos[i]);
        }

        scene.setOnKeyPressed(event -> {
            if (event.getCode() == KeyCode.UP) {
                jogadorView.setY(jogadorView.getY() - 10);
                jogadorView.setRotate(-270);
            } else if (event.getCode() == KeyCode.DOWN) {
                jogadorView.setY(jogadorView.getY() + 10);
                jogadorView.setRotate(270);
            } else if (event.getCode() == KeyCode.LEFT) {
                jogadorView.setX(jogadorView.getX() - 10);
                jogadorView.setScaleX(1);
            } else if (event.getCode() == KeyCode.RIGHT) {
                jogadorView.setX(jogadorView.getX() + 10);
                jogadorView.setScaleX(-1);
            }

        });

        primaryStage.setTitle("Jogo com JavaFX");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public boolean verificaColisao(ImageView jogador, ImageView inimigo) {
        Bounds boundsJogador = jogador.getBoundsInParent();
        Bounds boundsInimigo = inimigo.getBoundsInParent();
        colisao = true;
        return boundsJogador.intersects(boundsInimigo);
    }

    public boolean getColisao(){
        return colisao;
    }

    public void executar(String[] args) {
        launch(args);
    }

    public ImageView getJogadorView() {
        return jogadorView;
    }

    public ImageView getTabuleiroView() {
        return tabuleiroView;
    }

    public ImageView[] getInimigos() {
        return inimigos;
    }
}
