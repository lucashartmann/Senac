Algoritmo "salario com while"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/11/2024
Var
   salarioAtual, salarioFinal, aumento : real
   categoria : caractere

Inicio
   escreval("## DADOS ##")
   escreva("Informe seu sal�rio: ")
   leia(salarioAtual)
   escreval("Digite a categoria de aumento salarial (usando A, B ou C): ")
   leia(categoria)

   se((categoria = "A")ou(categoria = "B")ou(categoria = "C")) entao

      escolha(categoria)
      caso "A"
         aumento <- salarioAtual * 0,50
      caso "B"
         aumento <- salarioAtual * 0,30
      caso "C"
         aumento <- salarioAtual * 0,10
      fimescolha

      salarioFinal <- salarioAtual + aumento
      escreval()
      escreval("## RESULTADO DA CONSULTA ##")
      escreval("Sal�rio atual: ", salarioAtual:2:2)
      escreval("Categoria de aumento: ", categoria)
      escreval("Sal�rio final: ", salarioFinal:2:2)
   senao
      escreval("CATEGORIA DE AUMENTO SALARIAL INV�LIDO!")
   fimse

Fimalgoritmo