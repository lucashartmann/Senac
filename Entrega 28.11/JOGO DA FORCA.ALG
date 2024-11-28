algoritmo "Jogo da forca"

var

   opcao, opcaoFrutas, erros, acertos, enter, iniciaVitoria, iniciaDerrota, index : inteiro
   nomeFruta : vetor[1..7] de caracter
   linhas : vetor [1..7] de caractere
   letraDigitada : Caracter
   verifica : inteiro

funcao derrota(x : inteiro) : inteiro
inicio
   escreval(" --------- FIM  DE JOGO! ------- ")
   ESCREVAL
   ESCREVAL(" --------- GAME OVER ------- ")
   escreval
   retorne x+1
fimfuncao

funcao vitoria(x : inteiro) : inteiro
inicio
   escreval
   escreval(" --------- PARABÉNS, VOCÊ VENCEU! ------- ")
   ESCREVAL
   retorne x+1
fimfuncao

inicio
   repita
      limpatela
      escreval("---SEJA BEM VINDO---")
      escreval
      escreval("---JOGO DA FORCA---")
      escreval()
      escreva("Tecle Enter")
      leia(enter)
      opcao := 3
      aleatorio on // ativa o modo aleatorio fonte, palavra on é opcional
      aleatorio 1,7 //aleatorio 1,7 seleciona o ranger do aleatorio
      leia (opcaoFrutas) // todo leia vai ser lançado um numero aleatorio nesse caso de 1 a 7
      aleatorio off  // desativa o modo aleatorio, assim ele escolher uma das opções das palavras.
      se opcao <> 0 ENTÃO
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
         linhas[1] <- "_"           // LINHAS USADAS PARA ESCREVER
         linhas[2] <- "_"
         linhas[3] <- "_"
         linhas[4] <- "_"
         linhas[5] <- "_"
         linhas[6] <- "_"
         linhas[7] <- "_"
         repita
            se (erros > 7) ENTÃO  // Se número de erros for maior que 6 que
               // é o tamanho das palavras logo, jogador perde,
               // ou seja, jogador possui 6 chances apenas.
               iniciaDerrota <- derrota (iniciaDerrota)
               opcao := 101
            fimse
            se (linhas[1] <> "_") e (linhas[2] <> "_") e (linhas[3] <> "_") e (linhas[4] <> "_") e (linhas[5] <> "_") e (linhas[6] <> "_") e (linhas[7] <> "_") ENTÃO // Se as linhas forem diferentes de _ significa que existe letra no local,
               escreval()
               escreva("A palavra é " )
               para index de 1 ate 7 faca
                  escreva(nomeFruta[index])
               fimpara
               escreva("!")
               escreval()
               iniciaVitoria <- vitoria (iniciaVitoria)
               opcao := 101
            fimse
            se opcao <> 101 ENTÃO
               limpatela
               Escreval("============================================================")
               escreval("============================================================")
               escreval("")
               escreval("    /-----|")
               escreval("   /      |")
               se (erros > 0 ) ENTÃO
                  escreval("  /     (x.x)")
               senao
                  escreval("  /")
               fimse
               se (erros > 1 ) ENTÃO
                  escreval(" |      __||__  ")
               senao
                  escreval(" |   ")
               fimse
               se (erros > 2 ) ENTÃO
                  escreval(" |     /|     |\")
               senao
                  escreval(" |   ")
               fimse
               se (erros > 3) ENTÃO
                  escreval(" |    / |_____| \")
               senao
                  escreval(" |   ")
               fimse
               se (erros > 4) ENTÃO
                  escreval(" |       ||  ||")
               senao
                  escreval(" |      ")
               fimse
               se (erros > 5) ENTÃO
                  escreval(" |      _|| _||")
               senao
                  escreval(" |     ")
               fimse
               se (erros > 6) ENTÃO
                  escreval(" |     |__||__|")
                  escreval("=====                ULTIMA CHANCE! ")
               senao
                  escreval(" |    ")
                  escreval("=====               ")
               fimse
               escreval("")
               escreval("Acertos: ", acertos)
               escreval("Erros: ", erros)
               escreval("")
               escreva("Palavra com 7 letras:     ",linhas[1]," ",linhas[2]," ",linhas[3]," ",linhas[4]," ",linhas[5]," ",linhas[6]," ",linhas[7])
               escreval("")
               escreval("Dica da palavra: FRUTA")
               escreval
               escreva("digite uma letra: ")
               leia(letraDigitada)
               verifica <- 0
               se (nomeFruta[1] = letraDigitada) e (linhas[1] = "_") ENTÃO
                  linhas[1] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <- 1
               fimse
               se (nomeFruta[2] = letraDigitada) e (linhas[2] = "_") ENTÃO
                  linhas[2] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <- 1
               fimse
               se (nomeFruta[3] = letraDigitada) e (linhas[3] = "_") ENTÃO
                  linhas[3] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <- 1
               fimse
               se (nomeFruta[4] = letraDigitada) e (linhas[4] = "_") ENTÃO
                  linhas[4] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <-  1
               fimse
               se (nomeFruta[5] = letraDigitada) e (linhas[5] = "_") ENTÃO
                  linhas[5] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <- 1
               fimse
               se (nomeFruta[6] = letraDigitada) e (linhas[6] = "_") ENTÃO
                  linhas[6] <- letraDigitada
                  acertos <- acertos + 1
                  verifica <- 1
               fimse
               se (nomeFruta[7] = letraDigitada) e (linhas[7] = "_") ENTÃO
                  linhas[7] <- letraDigitada
                  na <- na + 1
                  verifica <- 1
               fimse
               se (verifica = 0) ENTÃO
                  erros <- erros + 1
               fimse
               escreval("==============================================================")
               escreval("==============================================================")
            fimse
         ate opcao = 101
      fimse
      escreval("Quer Jogar Novamente ")
      escreval("0 - Não")
      escreval("1 - Sim ")
      leia(opcao)
   ate opcao = 0
   escreval("Total De Vitórias -------: ", iniciaVitoria)
   escreval("Total De Derrotas -------: ", iniciaDerrota)
fimalgoritmo