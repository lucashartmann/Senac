Algoritmo "Cadastro de funcionarios"

// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
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

     Escreva("Digite a quantidade de funcionários que você deseja cadastrar (máximo 10): ")
   leia(quant)

   se (quant > 10) entao
      quant <- 10
      escreval("Quantidade excede o limite! Apenas 10 funcionários serão cadastrados.")
   fimse

   para i de 1 ate quant faca
      escreva("Digite o nome do funcionário: ")
      leia(nome)
      condicao <- cadastro(nome, i)
      se (condicao = 1) entao
         escreval("Funcionário cadastrado com sucesso!")
      senao
         escreval("Não foi possível cadastrar o funcionário.")
      fimse
   fimpara

   escreval()
   
   escreval("Lista de funcionários cadastrados:")
   para i de 1 ate quant faca
      escreval("Nome: ", funcionarios[i])
   fimpara

Fimalgoritmo