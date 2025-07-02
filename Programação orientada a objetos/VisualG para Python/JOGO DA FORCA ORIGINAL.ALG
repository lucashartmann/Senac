algoritmo "Jogo da forca original"
var
   op,frutas,ne,na,l,a,b,vit,der : inteiro //op: opção, ne: numero erro, na:numero de acertos
   l1,l2,l3,l4,l5,l6,l7,ld1,ld2  : caracter
   ld3,ld4,ld5,ld6,ld7,dig       : caracter //linhas(l1,l2,l3...) serão usadas para o aleatorio, já as ld (ld1, ld2, ld3) serão usadas para verificar o acerto
   V,D,verifica                  : Caracter
funcao derrota(x : inteiro) : inteiro
var
   a,b : inteiro
inicio
   Escreval("============================================================")
   escreval("============================================================")
   escreval
   escreval(" --------- FIM  DE JOGO! ------- ")
   ESCREVAL
   ESCREVAL(" --------- GAME OVER =( ------- ")
   ESCREVAL
   Escreval("============================================================")
   escreval("============================================================")
   escreval("          Tercle Enter")
   leia(l)
   retorne x+1   // aqui ele retorna um valor
fimfuncao
funcao vitoria(x : inteiro) : inteiro
var
   a,b : inteiro
inicio
   Escreval("============================================================")
   escreval("============================================================")
   escreval
   escreval(" --------- PARABÉNS VOCÊ VENCEU! ------- ")
   ESCREVAL
   Escreval("============================================================")
   escreval("============================================================")
   escreval("              Tecle Enter")
   leia(l)
   retorne x+1   // aqui ele retorna um valor
fimfuncao
//----------------INICIO---------------------------------------------------
inicio
   repita
      limpatela
      escreval("---SEJA BEM VINDO---")
      escreval
      escreval("---JOGO DA FORCA---")
      para l de 1 ate 10 faca
         escreval
      fimpara
      escreva("   Tecle Enter  ")
      leia(l)
      op := 3
      aleatorio on  // ativa o modo aleatorio fonte, palavra on é opcional
      aleatorio 1,7 // seleciona o ranger do aleatorio, é preciso definir para o comando ter as opção para escolha
      leia (frutas) // todo leia vai ser lançado um numero aleatorio nesse caso de 1 a 3
      aleatorio off  // desativa o modo aleatorio, assim ele escolher uma das opções das palavras.
      se op <> 0 ENTÃO
         escolha frutas // palava que vai ser escolhida automaticamente pelo aleatorio no inicio do código em aleatorio on
         caso 1
            l1 <- "d"
            l2 <- "a"
            l3 <- "m"
            l4 <- "a"
            l5 <- "s"
            l6 <- "c"
            l7 <- "o"
         caso 2
            l1 <- "a"
            l2 <- "b"
            l3 <- "a"
            l4 <- "c"
            l5 <- "a"
            l6 <- "x"
            l7 <- "i"
         caso 3
            l1 <- "a"
            l2 <- "b"
            l3 <- "a"
            l4 <- "c"
            l5 <- "a"
            l6 <- "t"
            l7 <- "e"
         caso 4
            l1 <- "a"
            l2 <- "c"
            l3 <- "e"
            l4 <- "r"
            l5 <- "o"
            l6 <- "l"
            l7 <- "a"
         caso 5
            l1 <- "l"
            l2 <- "a"
            l3 <- "r"
            l4 <- "a"
            l5 <- "n"
            l6 <- "j"
            l7 <- "a"
         caso 6
            l1 <- "p"
            l2 <- "e"
            l3 <- "s"
            l4 <- "s"
            l5 <- "e"
            l6 <- "g"
            l7 <- "o"
         caso 7
            l1 <- "g"
            l2 <- "u"
            l3 <- "a"
            l4 <- "r"
            l5 <- "a"
            l6 <- "n"
            l7 <- "a"
         fimescolha
         ld1 <- "_"           // LINHAS USADAS PARA ESCREVER
         ld2 <- "_"
         ld3 <- "_"
         ld4 <- "_"
         ld5 <- "_"
         ld6 <- "_"
         ld7 <- "_"
         // inicio do jogo
         repita //repita2
            se (ne > 7) ENTÃO  // Se número de erros for maior que 6 que
               // é o tamanho das palavras logo, jogador perde,
               // ou seja, jogador possui 6 chances apenas.
               der <- derrota (der)
               op := 101
            fimse
            se (ld1 <> "_") e (ld2 <> "_") e (ld3 <> "_") e (ld4 <> "_") e (ld5 <> "_") e (ld6 <> "_") e (ld7 <> "_") ENTÃO // Se as linhas forem diferentes de _ significa que existe letra no local,
               vit <- vitoria (vit)
               op := 101
            fimse
            se op <> 101 ENTÃO
               limpatela
               Escreval("============================================================")
               escreval("============================================================")
               escreval("")
               escreval("    /-----|")
               escreval("   /      |")
               se (ne > 0 ) ENTÃO
                  escreval("  /     (x.x)")
               senao
                  escreval("  /")
               fimse
               se (ne > 1 ) ENTÃO
                  escreval(" |      __||__  ")
               senao
                  escreval(" |   ")
               fimse
               se (ne > 2 ) ENTÃO
                  escreval(" |     /|     |\")
               senao
                  escreval(" |   ")
               fimse
               se (ne > 3) ENTÃO
                  escreval(" |    / |_____| \")
               senao
                  escreval(" |   ")
               fimse
               se (ne > 4) ENTÃO
                  escreval(" |       ||  ||")
               senao
                  escreval(" |      ")
               fimse
               se (ne > 5) ENTÃO
                  escreval(" |      _|| _||")
               senao
                  escreval(" |     ")
               fimse
               se (ne > 6) ENTÃO
                  escreval(" |     |__||__|")
                  escreval("=====                ULTIMA CHANCE! ")
               senao
                  escreval(" |    ")
                  escreval("=====               ")
               fimse
               escreval("")
               escreval("Acertos ------------: ",na)
               escreval("Erros --------------: ",ne)
               escreval("")
               escreva("Palavra com 7 letras:     ",ld1," ",ld2," ",ld3," ",ld4," ",ld5," ",ld6," ",ld7)
               escreval("")
               escreval("Dica da palavra ----: FRUTA ")
               escreval
               escreva("digite uma letra ---: ")
               leia(dig)
               verifica <- "0"
               se (l1 = dig) e (ld1 = "_") ENTÃO
                  ld1 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (l2 = dig) e (ld2 = "_") ENTÃO
                  ld2 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (l3 = dig) e (ld3 = "_") ENTÃO
                  ld3 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (l4 = dig) e (ld4 = "_") ENTÃO
                  ld4 <- dig
                  na <- na + 1
                  verifica <-  "1"
               fimse
               se (l5 = dig) e (ld5 = "_") ENTÃO
                  ld5 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (l6 = dig) e (ld6 = "_") ENTÃO
                  ld6 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (l7 = dig) e (ld7 = "_") ENTÃO
                  ld7 <- dig
                  na <- na + 1
                  verifica <- "1"
               fimse
               se (verifica = "0") ENTÃO
                  ne <- ne + 1
               fimse
               escreval("==============================================================")
               escreval("==============================================================")
            fimse
         ate op = 101
      fimse
      escreval("Quer Jogar Novamente ")
      escreval("0 - Não")
      escreval("1 - Sim ")
      leia(op)
   ate op = 0
   escreval("Total De Vitórias -------: ",vit)
   escreval("Total De Derrotas -------: ",der)
   escreval
   escreval("      Tecle Enter")
   leia(l)
fimalgoritmo