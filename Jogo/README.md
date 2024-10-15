## Composição do sistema

* Tabuleiro
* Protagonista:
    - Jogador
* Inimigo:
    - Zumbi
* Obstáculo
    - Cerca
    - Barril
* Objetivo Final:
    - Portal
* Objetivo Inicial:
    - Chave
* Ataque:
    - Dado
* Vida:
    - Dado
* Quantidade de Ações/Movimento:
    - Dado
* Ações:
    - Cartas de movimento


## Definição do Jogo
O jogo é um singleplayer em tabuleiro com rolagem de dados. O jogo contém: cercas, barris, portas, chave, cartas, portais, dados, campos de vida, jogador e zumbis.

O objetivo do jogador é matar dois zumbis para a porta que guarda a chave abrir, e ele poder pegar a chave. Para o jogador se mover ele deve rolar o dado de movimento. A quantidade de números definida no dado é a quantidade de movimentos que o jogador pode realizar no tabuleiro. O jogador escolhe de que forma se mover selecionando cartas de movimento disponiveis. O tabuleiro conta com quatro zumbis: Dois zumbis são ativados por aproximação. O jogador ao se aproximar do zumbis irá iniciar uma batalha mesmo que essa não seja sua intenção. Os zumbis restantes só entram em batalha caso o jogador decida enfrentá-los. O jogador tem 12 vidas, o zumbi tem 6 vidas. O dano dado tanto pelo jogador como pelo zumbi é definido pela rolagem do dado de ataque e a batalha é realizada em turnos. Quando o jogador estiver com a vida fraca, poderá ir para um dos dois campos de vida no mapa, onde será acrescentado em sua vida a quantidade pré-definida pelo campo. Se o jogador morrer, o jogo acaba. Se ele sobreviver á batalha, ele deve seguir sua jornada com o objetivo de matar dois zumbis para liberar a porta e por sua vez pegar a chave. Ao pegar a chave o jogador deve se movimentar até a porta que guarda o portal, usar a chave para abrir a porta e assim ganhar o jogo. 

Se a quantidade de roladas do dado de movimento chegar a dez, um novo zumbi aparece no mapa do jogo, porém, diferentemente dos outros, este zumbi pode se mover livremente pelo mapa. Seu objetivo é perseguir o jogador para matá-lo. O jogador deve fugir do zumbi ou decidir enfrentá-lo. Caso derrote o zumbi, o jogador deve seguir com seus objetivos iniciais.

## Zumbis
Os zumbis são personagem imóveis. Quatro zumbis ocupam o mapa e a quantidade de dano que eles realizam é definida de forma aleatória pelo sistema.
Se a quantidade de roladas do dado de movimento chegar a dez, um novo zumi aparece no mapa do jogo. Seu objetivo é perseguir o jogador para matá-lo. O jogador deve fugir do "boss" ou decidir enfrentá-lo. Caso derrote o boss, o jogador deve seguir com seus objetivos iniciais.



 