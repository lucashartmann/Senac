Algoritmo "folha salarial"

// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   :
// Autor(a)    : Lucas Hartmann
// Data atual  : 27/11/2024

Var
   nome: caractere
   horasTrabalhadas, quantidadeFuncionarios, i: inteiro
   salarioPorHora, valeAlimentacao, valeTransporte, salarioLiquido, salarioBruto : real
   percentualINSS, descontoINSS, descontoTransporte, descontoAlimentacao, l: real

funcao coletarDadosFuncionario() : real
inicio
   escreval()
   escreval("---- Entrada de dados ----")
   escreva("Digite o nome do funcionario: ")
   leia(nome)
   escreva("Digite a quantidade de horas trabalhadas no m�s: ")
   leia(horasTrabalhadas)
   escreva("Digite o sal�rio por hora: ")
   leia(salarioPorHora)
   escreva("Digite o valor do vale alimenta��o: ")
   leia(valeAlimentacao)
   escreva("Digite o valor do vale transporte: ")
   leia(valeTransporte)
   l <- calcularSalariosDescontos()
   retorne l
fimfuncao

funcao calcularPercentualINSS(salario: real) : real
inicio
   se (salario <= 1412.00) entao
      retorne 7.5
   senao
      se (salario <= 2666.68) entao
         retorne 9
      senao
         se (salario <= 4000.03) entao
            retorne 12
         senao
            retorne 14
         fimse
      fimse
   fimse
fimfuncao

funcao calcularSalariosDescontos() : real
inicio
   salarioBruto <- salarioPorHora * horasTrabalhadas
   percentualINSS <- calcularPercentualINSS(salarioBruto)
   descontoINSS <- salarioBruto * (percentualINSS / 100)
   descontoTransporte <- salarioBruto * (6 / 100)
   se descontoTransporte > valeTransporte entao
      descontoTransporte <- valeTransporte
   fimse
   descontoAlimentacao <- salarioBruto * (6 / 100)
   se descontoAlimentacao > (valeAlimentacao * (20 / 100)) entao
      descontoAlimentacao <- valeAlimentacao * (20 / 100)
   fimse
   salarioLiquido <- salarioBruto - descontoTransporte - descontoINSS - descontoAlimentacao
   retorne salarioLiquido
fimfuncao

funcao exibirRelatorioFuncionario() : caractere
inicio
   limpatela
   escreval("------ Dados do Funcion�rio ------")
   escreval("Nome: ", nome)
   escreval("Horas trabalhadas: ", horasTrabalhadas)
   escreval("Sal�rio por hora: R$", salarioPorHora:2:2)
   escreval("Vale transporte: R$", valeTransporte:2:2)
   escreval("Vale alimenta��o: R$", valeAlimentacao:2:2)
   escreval("Sal�rio bruto: R$", salarioBruto:2:2)
   escreval("Sal�rio l�quido: R$", salarioLiquido:2:2)
   escreval("Percentual INSS: ", percentualINSS, "%")
   escreval("Desconto INSS: R$", descontoINSS:2:2)
   escreval("Desconto transporte: R$", descontoTransporte:2:2)
   escreval("Desconto alimenta��o: R$", descontoAlimentacao:2:2)
fimfuncao

Inicio
   escreval("### FOLHA DE PAGAMENTO ###")
   escreva("Digite a quantidade de funcion�rios: ")
   leia(quantidadeFuncionarios)
   para i de 1 ate quantidadeFuncionarios faca
      escreval(coletarDadosFuncionario)
      escreval(exibirRelatorioFuncionario)
   fimpara
Fimalgoritmo
