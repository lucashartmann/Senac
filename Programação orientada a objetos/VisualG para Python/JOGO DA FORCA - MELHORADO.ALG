algoritmo "Jogo da Forca - Melhorado"

var
   opcao, opcaoFrutas, countErros, countAcertos, enter, iniciaVitoria, iniciaDerrota: inteiro
   index, countVitorias, countDerrotas: inteiro
   nomeFruta, linhas: vetor[1..7] de caractere
   letraDigitada: caractere
   verifica: logico

// Função para exibir mensagem de derrota
funcao derrota(contador: inteiro): inteiro
inicio
   escreval(" --------- FIM  DE JOGO! ------- ")
   escreval(" --------- GAME OVER ------- ")
   retorne contador + 1
fimfuncao

// Função para exibir mensagem de vitória
funcao vitoria(contador: inteiro): inteiro
inicio
   escreval(" --------- PARABÉNS, VOCÊ VENCEU! ------- ")
   retorne contador + 1
fimfuncao

inicio
   repita
      limpatela
      escreval("--- SEJA BEM-VINDO AO JOGO DA FORCA ---")
      escreval("Tecle Enter para iniciar")
      leia(enter)

      // Selecionar aleatoriamente uma fruta
      aleatorio on
      aleatorio 1, 7
      leia(opcaoFrutas)
      aleatorio off

      // Definir a palavra correspondente
      escolha opcaoFrutas
         caso 1 nomeFruta <- ["d", "a", "m", "a", "s", "c", "o"]
         caso 2 nomeFruta <- ["a", "b", "a", "c", "a", "x", "i"]
         caso 3 nomeFruta <- ["a", "b", "a", "c", "a", "t", "e"]
         caso 4 nomeFruta <- ["a", "c", "e", "r", "o", "l", "a"]
         caso 5 nomeFruta <- ["l", "a", "r", "a", "n", "j", "a"]
         caso 6 nomeFruta <- ["p", "e", "s", "s", "e", "g", "o"]
         caso 7 nomeFruta <- ["g", "u", "a", "r", "a", "n", "a"]
      fimescolha

      // Inicializar linhas e contadores
      para index de 1 ate 7 faca
         linhas[index] <- "_"
      fimpara
      countErros <- 0
      countAcertos <- 0

      // Loop principal do jogo
      repita
         limpatela
         escreval("============================================================")
         escreval("PALAVRA: ", linhas[1], " ", linhas[2], " ", linhas[3], " ", linhas[4], " ", linhas[5], " ", linhas[6], " ", linhas[7])
         escreval("Acertos: ", countAcertos, "  |  Erros: ", countErros, " (Máximo: 7)")
         escreval("Dica: FRUTA")

         // Desenho do boneco
         escreval("    /-----|")
         escreval("   /      |")
         escreval(se (countErros > 0) entao "  /     (x.x)" senao "  /")
         escreval(se (countErros > 1) entao " |      __||__" senao " |")
         escreval(se (countErros > 2) entao " |     /|     |\\" senao " |")
         escreval(se (countErros > 3) entao " |    / |_____| \\" senao " |")
         escreval(se (countErros > 4) entao " |       ||  ||" senao " |")
         escreval(se (countErros > 5) entao " |      _|| _||" senao " |")
         escreval(se (countErros > 6) entao " |     |__||__|" senao " |")
         escreval("============================================================")

         // Verificar vitória ou derrota
         se countErros > 6 entao
            iniciaDerrota <- derrota(iniciaDerrota)
            saia
         fimse

         se countAcertos = 7 entao
            iniciaVitoria <- vitoria(iniciaVitoria)
            saia
         fimse

         // Entrada do jogador
         escreva("Digite uma letra: ")
         leia(letraDigitada)
         verifica <- falso

         // Verificar letra digitada
         para index de 1 ate 7 faca
            se (nomeFruta[index] = letraDigitada) e (linhas[index] = "_") entao
               linhas[index] <- letraDigitada
               countAcertos <- countAcertos + 1
               verifica <- verdadeiro
            fimse
         fimpara

         // Atualizar erros caso a letra não seja encontrada
         se nao verifica entao
            countErros <- countErros + 1
         fimse

      ate (countErros > 6) ou (countAcertos = 7)

      // Perguntar se o jogador quer jogar novamente
      escreval("Quer jogar novamente?")
      escreval("1 - Sim")
      escreval("0 - Não")
      leia(opcao)

   ate opcao = 0

   // Exibir estatísticas finais
   escreval("Total de Vitórias: ", iniciaVitoria)
   escreval("Total de Derrotas: ", iniciaDerrota)
fimalgoritmo
