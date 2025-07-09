### Remodelagem do PI

- o que fazer? Sobre o que trata o sistema?
- quais são os dados?
- como eles estão (ou poderiam estar) organizados?
    - quais são relevantes?
    - quais informações queremos obter dos dados?

### Análise Orientada a Objetos

- Agrupamos os dados em objetos.
- Dados são suas propriedades/estados
- Sempre usamos de alguma metáfora para ajudar a substantivar os dados

`Exemplo`: gerenciador de pacote 'Brew' - metáfora de uma cervejaria

- garrafa -> pacote de software
- fórmula -> script que gera o pacote
- sótão -> repositório de pacotes de software
- etc...

`Exemplo`: Windows

- janela -> uma view
- esquadria -> moldura (frame) de uma view que é um container de outras views...
- etc..

Método que utilizamos:

- Listamos os dados procurando identificar substantivos
- Identificamos quais dados são propriedades desses substantivos
- Preliminarmente, consideramos que nosso objetos são esses substantivos.

Exemplo:

```
ALUGAR UM FILME

o filme
	estar alugado: 
	estar no acervo
	está danificado
	valor 
	classificação etária
	gênero
	categoria

categoria
	nome
	multa por dano
	
o cliente
	quem está alugando

o aluguel
	data de retirada
	data de devolução
	valor do aluguel
	juros cobrado por atraso

se o filme for danificado, paga multa

```