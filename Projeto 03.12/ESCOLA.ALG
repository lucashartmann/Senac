Algoritmo "Escola"

Var

   nome, cpf, rg, turma, professor, materia, teclaApertada : caractere
   idade, numero, user, cadastro, matricula, quant : inteiro
   quantAlunos, quantProfessores, presenca : inteiro
   notasGeral, notasMateria : vetor[1..10] de real
   nomesAlunos, matriculasCadastradas: vetor[1..10] de caractere
   nomesProfessores, numCadastrosProfessores : vetor[1..10] de caractere
   media, soma, nota : real

procedimento menuUsuario()
inicio
   enquanto((number < 1) ou (number > 7)) faca
      escreval("1 -- Ver frequência")
      escreval("2 -- Ver média")
      escreval("3 -- Ver todas as notas")
      escreval("4 -- Ver notas de certa matéria")
      escreval("5 -- Ver todas as materias")
      escreval("6 -- Pedir atestado de matrícula")
      escreval("7 -- Sair do menu")
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escolha(numero)
      caso 1
         escreval("Você escolheu ver frequencia")
         escreval("Aulas dadas: ", quantAulas)
         escreval("Presença: ", presenca)
         escreval("Faltas: ", faltas)
      caso 2
         escreval("Você escolheu ver media")
         escreval("Média: ", media(soma, quant))
      caso 3
         escreval("Você escolheu ver todas as notas")
         escreva("Notas: ")
         para i de 1 ate quant faca
            escreva(notasGeral[i])
         fimpara
         escreval()
      caso 4
         escreval("Você escolheu ver notas de certa materia")
         escreva("Notas: ")
         para i de 1 ate quant faca
            escreva(notasMateria[i])
         fimpara
         escreval()
      caso 5
         escreval("Você escolheu ver todas as materias")
      caso 6
         escreval("Você escolheu pedir atestado de matricula")
      caso 7
         escreval("Você escolheu sairr")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento menuProfessor()
inicio
   enquanto((number < 1) ou (number > 3)) faca
      escreval("1 -- Cadastrar notas")
      escreval("2 -- Cadastrar frequencia")
      escreval("3 -- Sair do menu")
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar notas")
         cadastarNotas
      caso 2
         escreval("Você escolheu cadastrar frequencia")
         cadastrarFrequencia
      caso 3
         escreval("Você escolheu sair")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento menuAdmin()
inicio
   enquanto((number < 1) ou (number > 5)) faca
      escreval("1 -- Cadastrar aluno")
      escreval("2 -- Cadastrar professor")
      escreval("3 -- Editar dados")
      escreval("4 -- Remover cadastro")
      escreval("5 -- Sair do menu")
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar aluno")
         cadastarAluno
      caso 2
         escreval("Você escolheu cadastrar professor")
         cadastarProfessor
      caso 3
         escreval("Você escolheu editar")
      caso 4
         escreval("Você escolheu remover")
      caso 5
         escreval("Você escolheu sair")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento cadastarAluno()
inicio
   quant <- 0
   escreva("Quantos alunos deseja cadastrar: ")
   leia(quant)
   quantAlunos <- quantAlunos + quant
   para i de 1 ate quant faca
      escreva("Informe o nome do aluno: ")
      leia(nome)
      nomesAlunos[i] = nome
      aleatorio on
      aleatorio 1, cadastro
      leia (cadastro)
      aleatorio off
      matriculasCadastradas[i] = cad
   fimpara
fimprocedimento

procedimento cadastarProfessor()
inicio
   quant <- 0
   escreva("Quantos professores deseja cadastrar: ")
   leia(quant)
   quantProfessores <- quantProfessores +  quant
   para i de 1 ate quant faca
      escreva("Informe o nome do professor: ")
      leia(nome)
      nomesProfessores[i] = nome
      aleatorio on
      aleatorio 1, cadastro
      leia (cadastro)
      aleatorio off
      numCadastrosProfessores[i] = cad
   fimpara
fimprocedimento

procedimento cadastarNotas()
inicio
   quant <- 0
   escreva("Quantos notas deseja cadastrar: ")
   leia(quant)
   para i de 1 ate quant faca
      escreva("Informe a nota : ")
      leia(nome)
      notasMateria[i] = nota
      notasGeral[i] = nota
   fimpara
fimprocedimento

funcao cadastrarFrequencia() : inteiro
inicio
   escreva("Quantas aulas foram dadas? ")
   leia(quantAulas)
   escreva("Quantas aulas o aluno esteve presente? ")
   leia(presenca)
   faltas <- quantAulas - presenca
   retorne presenca
fimfuncao

funcao media(soma : real; quant : inteiro) : real
inicio
   media <- soma / quant
   retorne media
fimfuncao

funcao somaGeral(quant : inteiro) : real
inicio
   para i de 1 ate quant
      soma <- soma + notasGeral[i]
   fimpara
   retorne soma
fimfuncao

Inicio
   escreval("Escola Santo Joaquim")
   escreval()
   escreval("Aperte uma tecla")
   leia(teclaApertada)
   limpatela
   enquanto((number < 1) ou (number > 3)) faca
      escreval("####### LOGIN #######")
      escreval("1 -- Aluno")
      escreval("2 -- Professor")
      escreval("3 -- Admin")
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escolha(numero)
         escreval("####### MENU #######")
      caso 1
         escreval("Você escolheu aluno")
         escreva("Informe sua matrícula: ")
         leia(matricula)
         para i de 1 ate 10
            se(matriculaCadastradas[i] = matricula)
               user <- 1
            fimse
         fimpara
         se(user = 1) entao
            menuUsuario
         senao
            escreval("Você não está cadastrado. Contate um admin")
         fimse
      caso 2
         escreval("Você escolheu professor")
         escreva("Informe seu nmro de cadastro: ")
         leia(cad)
         para i de 1 ate 10
            se(cadProf[i] = cad)
               user <- 2
            fimse
         fimpara
         se(user = 2) entao
            menuProfessor
         senao
            escreval("Você não está cadastrado. Contate um admin")
         fimse
      caso 3
         escreval("Você escolheu admin")
         user <- 3
         menuAdmin
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
   limpatela

Fimalgoritmo