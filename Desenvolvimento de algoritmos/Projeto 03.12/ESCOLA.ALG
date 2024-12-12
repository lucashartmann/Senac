Algoritmo "SistemaEscolar"

Var

   quantAulas, quantPresenca, quantFaltas, quantNotas : inteiro
   idade, numero, user, cadastro, matricula, quant : inteiro
   quantAlunos, quantProfessores, presenca, index : inteiro
   numCadastrosProfessores, matriculasCadastradas: vetor[1..10] de inteiro
   nomesAlunos, nomesProfessores, materias : vetor[1..10] de caractere
   nome, turma, teclaApertada, materia : caractere
   notasGeral, notasMateria : vetor[1..10] de real
   media, soma, nota : real
   verifica: logico

funcao verificarAluno(nomeVerificar : caractere) : logico
var
   encontrado : logico
inicio
   encontrado <- falso
   para index de 1 ate quantAlunos faca
      se (nomesAlunos[index] = nomeVerificar) entao
         encontrado <- verdadeiro
         interrompa
      fimse
   fimpara
   retorne encontrado
fimfuncao

funcao verificarProfessor(materiaVerificar : caractere) : logico
var
   encontrado : logico
inicio
   encontrado <- falso
   para index de 1 ate quantProfessores faca
      se (materias[index] = materiaVerificar) entao
         encontrado <- verdadeiro
         interrompa
      fimse
   fimpara
   retorne encontrado
fimfuncao

funcao media(soma : real; quant : inteiro) : real
inicio
   se (quant > 0) entao
      retorne soma / quant
   senao
      retorne 0
   fimse
fimfuncao

funcao somaGeral() : real
var
somaNotas : real
inicio
   somaNotas <- 0
   para index de 1 ate quantNotas faca
      somaNotas <- somaNotas + notasMateria[index]
   fimpara
   retorne somaNotas
fimfuncao

funcao cadastrarFrequencia() : inteiro
inicio
   escreva("Total de aulas dadas: ")
   leia(quantAulas)
   escreva("Quantas aulas o aluno esteve presente? ")
   leia(quantPresenca)
   quantFaltas <- quantAulas - quantPresenca
   retorne quantPresenca
fimfuncao

procedimento cadastrarAluno()
var
   quant : inteiro
inicio
   escreva("Quantos alunos deseja cadastrar (1-10): ")
   leia(quant)
   quantAlunos <- quantAlunos + quant
   para index de 1 ate quant faca
      matricula <- matricula + 1
      escreva("Informe o nome do aluno: ")
      leia(nome)
      escreva("Informe a turma do aluno: ")
      leia(turma)
      nomesAlunos[index] <- nome
      aleatorio on
      aleatorio 1000, 9999
      leia(matricula)
      aleatorio off
      matriculasCadastradas[index] <- matricula
      escreval("Aluno ", nome, " cadastrado com matrícula ", matricula)
   fimpara
fimprocedimento

procedimento cadastrarProfessor()
var
   quantValidada : inteiro
inicio
   escreva("Quantos professores deseja cadastrar (1-10): ")
   leia(quantValidada)
   quantProfessores <- quantProfessores + quantValidada
   para index de 1 ate quantValidada faca
      cadastro <- cadastro + 1
      escreva("Informe o nome do professor: ")
      leia(nome)
      escreva("Informe a materia do professor: ")
      leia(materia)
      materias[index] <- materia
      nomesProfessores[index] <- nome
      aleatorio on
      aleatorio 1000, 9999
      leia(cadastro)
      aleatorio off
      numCadastrosProfessores[index] <- cadastro
      escreval("Professor ", nome, " cadastrado com cadastro ", cadastro)
   fimpara
fimprocedimento

procedimento cadastrarNotas()
var
   nomeAluno : caractere
   quantNovasNotas : inteiro
inicio
   verifica <- falso
   escreva("Nome do aluno: ")
   leia(nomeAluno)
   para index de 1 ate quantAlunos faca
      se (nomesAlunos[index] = nomeAluno) entao
         verifica <- verdadeiro
         interrompa
      fimse
   fimpara
   se (verifica = falso) entao
      escreval("Aluno não encontrado. Tente novamente.")
   fimse
   escreva("Quantas notas deseja cadastrar (1-10): ")
   leia(quantNovasNotas)
   quantNotas <- quantNotas + quantNovasNotas
   escreva("Matéria: ")
   leia(materia)
   verifica <- falso
   para index de 1 ate quantProfessores faca
      se (materias[index] = materia) entao
         para index de 1 ate quantNovasNotas faca
            escreva("Informe a nota ", index, ": ")
            leia(nota)
            notasMateria[index] <- nota
            notasGeral[index] <- nota
         fimpara
         verifica <- verdadeiro
         interrompa
      fimse
   fimpara
   se (verifica = falso) entao
      escreval("Matéria não encontrada")
   fimse
fimprocedimento


procedimento dados()
inicio
   escreval("### DADOS DO SISTEMA ###")
   escreval()
   temDados <- falso
   escreval("--- NOTAS ---")
   se (quantNotas > 0) entao
      para index de 1 ate quantNotas faca
         escreval("Nota Matéria: ", notasMateria[index]:4:2, " | Nota Geral: ", notasGeral[index]:4:2)
      fimpara
   senao
      escreval("Nenhuma nota cadastrada.")
   fimse
   escreval()
   escreval("--- ALUNOS CADASTRADOS ---")
   se (quantAlunos > 0) entao
      para index de 1 ate quantAlunos faca
         escreval("Nome: ", nomesAlunos[index])
         escreval("Matrícula: ", matriculasCadastradas[index])
         escreval("---")
         temDados <- verdadeiro
      fimpara
   senao
      escreval("Nenhum aluno cadastrado.")
   fimse
   escreval()
   escreval("--- PROFESSORES CADASTRADOS ---")
   se (quantProfessores > 0) entao
      para index de 1 ate quantProfessores faca
         escreval("Nome: ", nomesProfessores[index])
         escreval("Cadastro: ", numCadastrosProfessores[index])
         escreval("Matéria: ", materias[index])
         escreval("---")
      fimpara
   senao
      escreval("Nenhum professor cadastrado.")
   fimse
fimprocedimento

procedimento dadosMaterias()
inicio
   escreval("### MATÉRIAS CADASTRADAS ###")
   para index de 1 ate quantProfessores faca
      escreval("Matéria: ", materias[index])
      escreval("Professor: ", nomesProfessores[index])
      escreval("---")
   fimpara
fimprocedimento

procedimento editar()
var
   tipoEdicao : inteiro
   nomeOriginal, novoNome : caractere
inicio
   escreval("### EDIÇÃO DE DADOS ###")
   escreval("1 -- Editar Aluno")
   escreval("2 -- Editar Professor")
   escreva("Digite o número correspondente: ")
   leia(tipoEdicao)
   se (tipoEdicao < 1) ou (tipoEdicao > 2) entao
      escreval("Opção inválida")
   fimse
   escreva("Digite o nome da pessoa a ser editada: ")
   leia(nomeOriginal)
   verifica <- falso
   indexEncontrado <- 0
   se (tipoEdicao = 1) entao
      para index de 1 ate quantAlunos faca
         se (nomesAlunos[index] = nomeOriginal) entao
            nomesAlunos[index] <- novoNome
            escreval("Nome do aluno atualizado com sucesso!")
            interrompa
         fimse
      fimpara
   senao
      para index de 1 ate quantProfessores faca
         se (nomesProfessores[index] = nomeOriginal) entao
            nomesProfessores[index] <- novoNome
            escreval("Nome do professor atualizado com sucesso!")
            interrompa
         fimse
      fimpara
   fimse
fimprocedimento

procedimento atestado()
inicio
   escreval("### ATESTADO DE MATRÍCULA ###")
   escreval("Escola Santo Joaquim")
   escreval("Ensino Médio 2024")
   para index de 1 ate quantAlunos faca
      se (matriculasCadastradas[index] = matricula) entao
         escreval("Nome do aluno: ", nomesAlunos[index])
         escreval("Matrícula: ", matricula)
         interrompa
      fimse
   fimpara
   escreval()
   escreval("Matérias matriculadas:")
   para index de 1 ate quantProfessores faca
      escreval("- ", materias[index])
   fimpara
fimprocedimento

procedimento menuUsuario()
inicio
   numero <- 0
   limpatela
   verifica <- falso
   enquanto (numero < 1) ou (numero > 8) faca
      escreval()
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Ver frequência")
      escreval("2 -- Ver média")
      escreval("3 -- Ver soma")
      escreval("4 -- Ver todas as notas")
      escreval("5 -- Ver notas de certa matéria")
      escreval("6 -- Ver todas as materias")
      escreval("7 -- Pedir atestado de matrícula")
      escreval("8 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      limpatela
      escolha(numero)
      caso 1
         escreval("Digite a matéria desejada")
         leia(materia)
         para index de 1 ate quantProfessores faca
            se (materias[index] = materia) entao
               escreval("Você escolheu ver frequência")
               escreval("Aulas dadas: ", quantAulas)
               escreval("Presença: ", quantPresenca)
               escreval("Faltas: ", quantFaltas)
               interrompa
            fimse
         fimpara
      caso 2
         escreval("Você escolheu ver media")
         se (soma <= 0) entao
            soma <- somaGeral
         fimse
         media <-  media(soma, quantNotas)
         escreval("Média: ", media)
      caso 3
         escreval("Você escolheu ver soma")
         soma <- somaGeral
         escreval("Soma: ", soma))
      caso 4
         escreval("Você escolheu ver todas as notas")
         escreva("Notas: ")
         para index de 1 ate quantNotas faca
            escreva(notasGeral[index], "")
         fimpara
         escreval()
      caso 5
         escreval("Você escolheu ver notas de certa materia")
         verifica <- falso
         escreval("Digite a matéria desejada")
         leia(materia)
         para index de 1 ate quantProfessores faca
            se (materias[index] = materia) entao
               escreva("Notas: ")
               para index de 1 ate quant faca
                  escreva(notasMateria[index], "")
               fimpara
               verifica <- verdadeiro
            fimse
         fimpara
         se(verifica = falso) entao
            escreval("Matéria não encontrada")
         fimse
         verifica <- falso
      fimenquanto
   caso 6
      escreval("Você escolheu ver todas as materias")
      dadosMaterias
   caso 7
      escreval("Você escolheu pedir atestado de matricula")
      atestado
   caso 8
      escreval("Você escolheu sair")
      verifica <- verdadeiro
   outrocaso
      escreval("Número inválido. Tente novamente")
   fimescolha
   se (verifica = falso) entao
      numero <- 0
   fimse
fimenquanto
fimprocedimento

procedimento menuProfessor()
inicio
   numero <- 0
   limpatela
   verifica <- falso
   enquanto (numero < 1) ou (numero > 3) faca
      escreval()
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Cadastrar notas")
      escreval("2 -- Cadastrar frequencia")
      escreval("3 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      limpatela
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar notas")
         cadastrarNotas
         verifica <- falso
      caso 2
         escreval("Você escolheu cadastrar frequencia")
         quantPresenca <- cadastrarFrequencia
         verifica <- falso
      caso 3
         escreval("Você escolheu sair")
         verifica <- verdadeiro
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
      se (verifica = falso) entao
         numero <- 0
      fimse
   fimenquanto
   exibirMenuPrincipal
fimprocedimento

procedimento menuAdmin()
inicio
   numero <- 0
   limpatela
   verifica <- falso
   enquanto (numero < 1) ou (numero > 5) faca
      escreval()
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Cadastrar aluno")
      escreval("2 -- Cadastrar professor")
      escreval("3 -- Editar dados")
      escreval("4 -- Ver dados")
      escreval("5 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      limpatela
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar aluno")
         cadastrarAluno
      caso 2
         escreval("Você escolheu cadastrar professor")
         cadastrarProfessor
      caso 3
         escreval("Você escolheu editar")
         editar
      caso 4
         escreval("Você escolheu ver dados")
         dados
      caso 5
         escreval("Você escolheu sair")
         verifica <- verdadeiro
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
      se (verifica = falso) entao
         numero <- 0
      fimse
   fimenquanto
fimprocedimento

procedimento exibirMenuPrincipal()
inicio
   limpatela
   escreval("####### LOGIN #######")
   escreval()
   escreval("1 -- Aluno")
   escreval("2 -- Professor")
   escreval("3 -- Admin")
   escreval("4 -- Sair")
   escreval()
   escreva("Digite o número correspondente a opção desejada: ")
   leia(numero)
   escolha(numero)
   caso 1
      escreva("Informe sua matrícula: ")
      leia(matricula)
      user <- 0
      para index de 1 ate quantAlunos faca
         se (matriculasCadastradas[index] = matricula) entao
            user <- 1
            interrompa
         fimse
      fimpara
      se(user = 1) entao
         menuUsuario()
      senao
         escreval("Você não está cadastrado. Contate um admin")
      fimse
   caso 2
      escreva("Informe seu número de cadastro: ")
      leia(cadastro)
      user <- 0
      para index de 1 ate quantProfessores faca
         se (numCadastrosProfessores[index] = cadastro) entao
            user <- 2
            interrompa
         fimse
      fimpara
      se(user = 2) entao
         menuProfessor()
      senao
         escreval("Você não está cadastrado. Contate um admin")
      fimse
   caso 3
      menuAdmin()
   caso 4
      escreval("Saindo do sistema...")
   outrocaso
      escreval("Número inválido. Tente novamente")
   fimescolha
fimprocedimento

Inicio
   escreval("Escola Santo Joaquim")
   escreval()
   escreval("Pressione Enter para continuar")
   leia(teclaApertada)
   numero <- 0
   user <- 0
   enquanto (numero < 1) ou (numero > 4) faca
      exibirMenuPrincipal
   fimenquanto
Fimalgoritmo