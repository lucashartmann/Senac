# Conceitos fundamentais de Programação Orientada a Objetos

Esta lição explica os conceitos básicos da programação orientada a objetos. Não nos preocuparemos, por enquanto, em como aplicar estes conceitos em alguma linguagem de programação.

## O que é um objeto?

Podemos olhar para quaisquer objetos do mundo real e distinguir neles três características. Todos eles têm:

- propriedades
- estados
- comportamentos

Por exemplo, discos-voadores têm `estados`:

- velocidade
- carga dos lasers

`propriedades características`:

- dois motores
- número de canhões

e `comportamentos`:

- frear
- acelerar
- disparar lasers
- abduzir

Objetos de software também têm propriedades, estados e comportamentos. Um objeto de software guarda seus estados e propriedades em variáveis e implementa seus comportamentos através de métodos (aquilo que em liguagens como C ou Pascal chamaríamos de procedimentos ou funções).

![Objetos - propriedades, estados e comportamentos](/img/poo01/POO01-Objetos-propriedades-estados-e-comportamentos.png)

> Definição: Um `objeto` é um conjunto de variáveis e métodos relacionados em uma mesma estrutura de dados.

Uma outra forma de pensar nas propriedades e estados de um objeto é pensar que elas são tudo aquilo que um objeto, por assim dizer, conhece.

Continuando o exemplo do disco-voador. Ele poderá ter variáveis que indiquem seu estado atual:

- sua velocidade é de x Km/s
- motor 1 está girando a y rpm
- motor 2 está girando a z rpm
- lasers estão a plena carga

e poderá ter variáveis que guardem suas propriedades características, como:

- dimensões (supondo que ele não seja um dos modelos que mudam de dimensão)
- cor
- número identificador da frota estelar

Tudo que um objeto não conhece ou não pode fazer é excluído do objeto. Por exemplo, discos-voadores não podem ter nomes, não podem correr nem ruminar. Por isso, não existem variáveis ou métodos para estas características, estados e comportamentos.

Também excluímos do objeto tudo o que não é relevante para o sistema que estamos escrevendo. Por exemplo, a cor do disco-voador pode ser importante para um sistema de revenda on-line de discos-voadores mas não é importante para o sitema de navegação que roda nos computadores da nave.

> Esse processo de "deixar de fora" o que não é relevante ao sistema é um processo de `abstração` e abstrair é uma das coisas mais importantes que você precisa aprender a fazer para programar computadores.

## O que é um método?

O disco-voador de software também deve ter métodos:

- frear
- acelerar
- disparar lasers

Podemos pensar nos seus métodos também como tudo aquilo que o objeto sabe fazer. A execução de cada um desses métodos altera as variáveis do disco-voador de alguma forma.

![Objeto disco-voador](/img/poo01/POO01-Objeto-disco-voador.png)

> Definição: Um `método` é um trecho de código que executa uma tarefa (algorítmo, procedimento, etc.) e que possivelmente altera estados e propriedades de um objeto.

O ponto importante é que essa alteração de estados e propriedades feita por um método seja consistente com aquilo que um disco-voador pode fazer, para que a modelagem desse objeto de software seja adequada ao objeto real.

Por exemplo:

- não deve ser possível executar o método `frear` e a velocidade aumentar;
- não deve ser possível que a execução do método que troca as marchas cause uma frenagem;
- não deve haver um método para trocar a velocidade, já que a velocidade do disco-voador é, na verdade, uma conseqüência de termos executado a operação `acelerar` ou `frear`, do número de rotações dos motores e também da velocidade do disco-voador antes dessas operações serem executadas.

Em uma linguagem orientada a objetos, um programa escrito com um bom design irá tirar proveito dos métodos que são associados a um objeto para fazer com que esses métodos não coloquem o objeto em um estado instável, absurdo. Um bom conjunto de métodos irá, assim, contribuir para a boa representação que o objeto deve ser, em nosso programa, do objeto do mundo real e dos dados reais associados a ele.

## O que são mensagens?

Um objeto sempre apenas um dos componentes de um sistema composto de muitos objetos e não é muito útil isoladamente. Um disco-voador só é útil quando outro objeto (digamos, você) interage com ele.

Objetos de software interagem e comunicam-se uns com os outros mandando mensagens de um para o outro. Quando o objeto A quer que o objeto B acione um de seus métodos, o objeto A manda uma mensagem para o objeto B.

Às vezes o objeto receptor precisa de mais informações para saber exatamente o que fazer.

Por exemplo: quando você quer disparar os lasers do seu disco-voador você tem que dizer qual potência você quer. Essa informação é passada junto com a mensagem como um parâmetro.

Três componentes compreendem uma mensagem:

1. o objeto para o qual a mensagem é endereçada (o disco-voador)
1. o nome do método a ser executado
1. quaisquer parâmetros solicitados pelo método

Veja exemplos de mensagens sendo enviadas em diversas linguagens de programação:

``` smalltalk
"Smalltalk"

disco dispararLasers: 5
```

``` C++
/*
    C++, C#, Java
*/

disco.dispararLasers(5);

```

``` lua
/*
    Python, Lua
*/

disco.dispararLasers(5)

```

Esses três componentes são informação suficiente para que o objeto receptor da mensagem execute o método desejado. Não é necessário nenhuma outra informação ou contexto.

Note que, não importa a linguagem de programação, a sintaxe da mensagem completa corresponde à sintaxe:

`Sujeito Verbo Complemento`

assim como no português.

`O disco-voador dispara os lasers.`

O objeto corresponde ao sujeito (`O disco-voador`), que é quem realiza a ação. O método é o verbo (`dispara`), que determina a ação que é realizada. O complemento é o objeto do verbo, que neste caso é um objeto direto (`os lasers`).
