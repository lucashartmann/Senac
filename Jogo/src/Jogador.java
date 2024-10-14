public class Jogador {
    private int vidas;
    private int dano;
    private Tipo tipoJogador;

    public Jogador(int vidas, Tipo tipoJogador) {
        this.vidas = vidas;
        this.tipoJogador = tipoJogador;
    }

    public int getVidas() {
        return vidas;
    }

    public void setVidas(int vidas) {
        this.vidas = vidas;
    }

    public int getDano() {
        return dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }

}
