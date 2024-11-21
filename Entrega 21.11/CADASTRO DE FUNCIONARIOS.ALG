Algoritmo "Cadastro de funcionarios"

// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024

Var

   funcionarios : vetor[1..10] de caractere
   quant, i, condicao : inteiro
   nome : caractere

funcao cadastro(nome : caractere) : inteiro
var
   total : inteiro
inicio
   para i de 1 ate 1 faca
      funcionarios[i] <- nome
      total <- 1
   fimpara
   retorne total

fimfuncao

Inicio

   Escreva("Digite a quantidade de funcionarios quer você deseja cadastrar: ")
   leia(quant)
   para i de 1 ate quant faca
      escreva("Digite o nome do funcionário: ")
      leia(nome)
      condicao <- cadastro(nome)
      se (condicao = 1) entao
         escreval("Funcionário cadastrado")
      senao
         escreval("Não foi possivel cadastrar funcionário")
      fimse
   fimpara
   escreval()
   escreval("Lista de funcionários cadastrados: ")
   para i de 1 ate quant faca
      escreval("Nome: ",funcionarios[i])
   fimpara

Fimalgoritmo