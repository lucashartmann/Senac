Desfio: A Inteligência do Restaurante

1 - Enunciado:
"O layout do nosso restaurante está impecável, mas ele ainda é uma 'vitrine estática'. O cliente agora exige que o site seja funcional. Seu objetivo é transformar a barra de busca e os botões de de compra em ferramentas reais, usando apenas o que o navegador nos oferece."


2 - As Missões

Missão 1: Busca em tempo real
	Desafio: Ao digitar o campo de busca (#search-box), o site deve filtrar os pratos automaticamente.

	Regra: Não pode recarregar a página.

	Dica de pesquisa: Como usar o evento oninput no JavaScript para esconder elementos HTML que não batem com o texto digitado?


Missão 2: O carrinho de memória:
	Desafio: Ao clicar no ícone de carrinho de um prato, o sistema deve "anotar" que aquele item foi escolhido.

	Regra: Crie uma lista (Array) de objetos para guardar o nome e o preço do prato.

	O grande problema: Tente resolver este mistério: Por que, quando eu atualizo (F5), meu carrinho volta a ficar vazio? Existe alguma forma do navegador 'salvar' isso sem um banco de dados externo?


Missão 3: O formulário consciente
	Desafio: O formulário de pedido (section .order) não pode ser enviado vazio.

	Regra: Se o usuário clicar em "Order Now", o JavaScript deve capturar os dados digitados e mostrar um resumo no console.log.

	Dica de pesquisa: Como usar o event.preventDefault() para impedir que o formulário limpe a tela antes de processarmos no console.log.



