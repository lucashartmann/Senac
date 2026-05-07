Exercício Prático: Expansão do Sistema de Cadastro
Contexto
Atualmente, o sistema valida Nome, Sobrenome e Idade. A coordenação do curso solicitou que o sistema agora também aceite o E-mail do usuário.

Missão
Você deve realizar as seguintes alterações nos arquivos do projeto:
```
1. Camada de Modelo (modelo/pessoa.class.php)
Adicione o atributo público $email à classe Pessoa.

Atualize o método __toString() para que ele também exiba o e-mail cadastrado.
```
```

2. Camada de Utilidade (util/validacao.php)
Crie um novo método estático chamado testarEmail($v).


Regra de validação: O e-mail deve conter um @ e pelo menos um ponto . (Dica: use a função nativa do PHP filter_var($v, FILTER_VALIDATE_EMAIL)).
```

```
3. Camada de Controle (O arquivo de processamento)
Altere o if(isset(...)) para verificar se o campo txtemail também foi enviado.

Adicione uma nova validação: se o e-mail for inválido, adicione a mensagem "E-mail inválido" ao array $erros.

Se os dados estiverem corretos, salve o e-mail no objeto $p (lembre-se de usar o converterMin para padronizar o e-mail em letras minúsculas).

Atualize o header(location:...) para enviar também o parâmetro email na URL.
```

```
Questão Teórica para Discussão
No arquivo de Controle, utilizamos a função serialize($erros).

Por que não podemos passar o array $erros diretamente pela URL?

Qual função PHP deve ser usada na página guierro.php para transformar essa string de volta em um array e exibir a lista para o usuário?
```

- Resposta:

1. Porque URL é String. Array é não é String, e sim uma 'lista' de dados. Não é possivel botar. O navegador trata a ulr como texto, entao nao da para ter uma lista no meio de texto. E array nao é automaticamente convertido para uma string, é preciso usar a função serialize() para transformar o array em uma string que pode ser passada pela URL.

2. unserialize()