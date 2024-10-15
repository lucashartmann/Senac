package Dados;

import java.util.ArrayList;

import javafx.scene.image.ImageView;

public class Tabuleiro {
   private ArrayList<Jogador> inimigos;
   private int quantidade;
   private ImageView tabuleiroView;

   public Tabuleiro(ImageView tabuleiroView) {
      inimigos = new ArrayList<>();
      this.tabuleiroView = tabuleiroView;
   }

   public void add(Jogador jogador) {
      inimigos.add(jogador);
   }

   public void remove(Jogador jogador) {
      inimigos.remove(jogador);
   }

   public Jogador getInimigoByImage(ImageView imageInimigo) {
      for (Jogador jogador : inimigos) {
         if (jogador.getJogadorView() == imageInimigo) {
            return jogador;
         }
      }
      return null;
   }

   public boolean containsPlayer(Jogador jogador){
      if (inimigos.contains(jogador)) {
         return true;
      }
      return false;
   }

   public int getQuantidade() {
      return quantidade;
   }
}
