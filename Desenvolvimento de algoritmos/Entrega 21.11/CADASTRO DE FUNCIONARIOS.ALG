Algoritmo "Cadastro de funcionarios"

// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024

Var

   funcionarios : vetor[1..10] de caractere
   quant, i, condicao, j : inteiro
   nome : caractere

funcao cadastro(nome : caractere; j : inteiro) : inteiro
inicio
   funcionarios[j] <- nome
   retorne 1
fimfuncao

Inicio

     Escreva("Digite a quantidade de funcion�rios que voc� deseja cadastrar (m�ximo 10): ")
   leia(quant)

   se (quant > 10) entao
      quant <- 10
      escreval("Quantidade excede o limite! Apenas 10 funcion�rios ser�o cadastrados.")
   fimse

   para i de 1 ate quant faca
      escreva("Digite o nome do funcion�rio: ")
      leia(nome)
      condicao <- cadastro(nome, i)
      se (condicao = 1) entao
         escreval("Funcion�rio cadastrado com sucesso!")
      senao
         escreval("N�o foi poss�vel cadastrar o funcion�rio.")
      fimse
   fimpara

   escreval()
   
   escreval("Lista de funcion�rios cadastrados:")
   para i de 1 ate quant faca
      escreval("Nome: ", funcionarios[i])
   fimpara

Fimalgoritmo