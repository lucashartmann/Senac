algoritmo "Jogo da forca"

var

   opcao, opcaoFrutas, countErros, countAcertos, enter: inteiro
   index, countVitorias, countDerrotas: inteiro
   nomeFruta, linhas: vetor[1..7] de caractere
   letraDigitada: caractere
   verifica: logico

funcao derrota(countDerrotas: inteiro): inteiro
inicio
   escreval(" --------- FIM  DE JOGO! ------- ")
   escreval(" --------- GAME OVER ------- ")
   retorne countDerrotas + 1
fimfuncao

funcao vitoria(countVitorias: inteiro): inteiro
inicio
   escreval(" --------- PARABÉNS, VOCÊ VENCEU! ------- ")
   retorne countVitorias + 1
fimfuncao

inicio
   repita
      limpatela
      escreval("--- SEJA BEM-VINDO AO JOGO DA FORCA ---")
      escreval("Tecle Enter para iniciar")
      leia(enter)
      aleatorio on // Selecionar aleatoriamente uma fruta
      aleatorio 1, 7
      leia(opcaoFrutas)
      aleatorio off // desativa o modo aleatorio, assim ele escolher uma das opções das palavras.
      escolha opcaoFrutas // palava que vai ser escolhida automaticamente pelo aleatorio no inicio do código em aleatorio on
      caso 1
         nomeFruta[1] <- "d"
         nomeFruta[2] <- "a"
         nomeFruta[3] <- "m"
         nomeFruta[4] <- "a"
         nomeFruta[5] <- "s"
         nomeFruta[6] <- "c"
         nomeFruta[7] <- "o"
      caso 2
         nomeFruta[1] <- "a"
         nomeFruta[2] <- "b"
         nomeFruta[3] <- "a"
         nomeFruta[4] <- "c"
         nomeFruta[5] <- "a"
         nomeFruta[6] <- "x"
         nomeFruta[7] <- "i"
      caso 3
         nomeFruta[1] <- "a"
         nomeFruta[2] <- "b"
         nomeFruta[3] <- "a"
         nomeFruta[4] <- "c"
         nomeFruta[5] <- "a"
         nomeFruta[6] <- "t"
         nomeFruta[7] <- "e"
      caso 4
         nomeFruta[1] <- "a"
         nomeFruta[2] <- "c"
         nomeFruta[3] <- "e"
         nomeFruta[4] <- "r"
         nomeFruta[5] <- "o"
         nomeFruta[6] <- "l"
         nomeFruta[7] <- "a"
      caso 5
         nomeFruta[1] <- "l"
         nomeFruta[2] <- "a"
         nomeFruta[3] <- "r"
         nomeFruta[4] <- "a"
         nomeFruta[5] <- "n"
         nomeFruta[6] <- "j"
         nomeFruta[7] <- "a"
      caso 6
         nomeFruta[1] <- "p"
         nomeFruta[2] <- "e"
         nomeFruta[3] <- "s"
         nomeFruta[4] <- "s"
         nomeFruta[5] <- "e"
         nomeFruta[6] <- "g"
         nomeFruta[7] <- "o"
      caso 7
         nomeFruta[1] <- "g"
         nomeFruta[2] <- "u"
         nomeFruta[3] <- "a"
         nomeFruta[4] <- "r"
         nomeFruta[5] <- "a"
         nomeFruta[6] <- "n"
         nomeFruta[7] <- "a"
      fimescolha
      para index de 1 ate 7 faca
         linhas[index] <- "_"
      fimpara
      countErros <- 0
      countAcertos <- 0
      repita
         limpatela
         escreval("============================================================")
         escreval("PALAVRA: ", linhas[1], " ", linhas[2], " ", linhas[3], " ", linhas[4], " ", linhas[5], " ", linhas[6], " ", linhas[7])
         escreval("Acertos: ", countAcertos, "  |  Erros: ", countErros, " (Máximo: 7)")
         escreval("Dica: FRUTA")
         Escreval("============================================================")
         escreval("============================================================")
         escreval("")
         escreval("    /-----|")
         escreval("   /      |")
         se (countErros > 0 ) ENTÃO
            escreval("  /     (x.x)")
         senao
            escreval("  /")
         fimse
         se (countErros > 1 ) ENTÃO
            escreval(" |      __||__  ")
         senao
            escreval(" |   ")
         fimse
         se (countErros > 2 ) ENTÃO
            escreval(" |     /|     |\")
         senao
            escreval(" |   ")
         fimse
         se (countErros > 3) ENTÃO
            escreval(" |    / |_____| \")
         senao
            escreval(" |   ")
         fimse
         se (countErros > 4) ENTÃO
            escreval(" |       ||  ||")
         senao
            escreval(" |      ")
         fimse
         se (countErros > 5) ENTÃO
            escreval(" |      _|| _||")
         senao
            escreval(" |     ")
         fimse
         se (countErros > 6) ENTÃO
            escreval(" |     |__||__|")
            escreval("=====                ULTIMA CHANCE! ")
         senao
            escreval(" |    ")
            escreval("=====               ")
         fimse
         escreval("")
         escreva("Digite uma letra: ")
         leia(letraDigitada)
         verifica <- falso
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
      se countErros > 6 entao
         countDerrotas <- derrota(countDerrotas) // Atualizar a variável corretamente
         escreval("A palavra era: ", nomeFruta[1], nomeFruta[2], nomeFruta[3], nomeFruta[4], nomeFruta[5], nomeFruta[6], nomeFruta[7]) // Exibir a palavra completa
      fimse
      se countAcertos = 7 entao
         countVitorias <- vitoria(countVitorias) // Atualizar a variável corretamente
         escreval("Você acertou a palavra: ", nomeFruta[1], nomeFruta[2], nomeFruta[3], nomeFruta[4], nomeFruta[5], nomeFruta[6], nomeFruta[7]) // Exibir a palavra completa
      fimse
      escreval()
      // Perguntar se o jogador quer jogar novamente
      escreval("Quer jogar novamente?")
      escreval("1 - Sim")
      escreval("0 - Não")
      leia(opcao)
   ate opcao = 0
   // Exibir estatísticas finais
   escreval()
   escreval("Total de Vitórias: ", countVitorias)
   escreval("Total de Derrotas: ", countDerrotas)
fimalgoritmo