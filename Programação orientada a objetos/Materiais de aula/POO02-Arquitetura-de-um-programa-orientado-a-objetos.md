# Arquitetura de um programa orientado a objetos

Programas são coisas muito complexas, e trabalhar com objetos em uma linguagem de programação é uma forma de lidar com essa complexidade.

Programas orientados a objeto são concebidos como uma imensa rede de troca de mensagens entre objetos que estão todos colaborando entre si para a realização de uma tarefa complexa, que é a tarefa do sistema ao qual eles pertencem. 

A inspiração para o uso desse tipo de estrutura veio da biologia, do modo como células, cada uma especializada em uma tarefa, interagem para realizar tarefas complexas em conjunto.

![Células especializadas realizando tarefa em conjunto](/img/poo02/POO02-Celulas-especializadas-relizando-tarefa-em-conjunto.png)

Cada objeto é especializdo em uma tarefa. Ele pode precisar realizar diversas funções para conseguir realizar essa sua tarefa e por isso ele pode ter vários métodos, mas conceitualmente a tarefa de cada objeto é uma só.


## Encapsulamento e troca de mensagens

Digamos que nosso sistema vai modelar o processo de abdução de uma vaca por um disco-voador. Em algum momento a vaca vai estar dentro do disco-voador. Isso não significa, porém, que agora o disco-voador é um pouco vaca também. Não. O que acontece é uma interação entre eles, uma colaboração na qual nenhum deixa de ser o que é e cada um cumpre seu papel para a realização de uma ação em comum.

Vamos imaginar três objetos participando dessa operação de abdução: o disco-voador; a vaca; e você, no comando do disco-voador. Um programa orientado a objetos modelaria a abdução assim:

O `Comandante` (você) envia a mensagem `disco-voador abduzir vaca` para o objeto `disco-voador` solicitando a execução do método `abduzir` e passando como parâmetro a `vaca`.

Em Java, C#, C++, a linha de código com essa mensagem seria:

``` C++

disco.abduzir(vaca);

```

> O objeto que envia a mensagem não aparece escrito no código. Devemos sempre fazer o trabalho de nos colocarmos no lugar desse objeto ao escrever o código. É algo que faz parte daquele exercício de abstrair ao qual me referi antes, e você vai ter que ficar bom nisso para programar.

Note no exemplo acima como cada objeto teve um papel bem definido na execução da operação de abdução:

- Você, por exemplo, não executou a tarefa `abduzir`. Você foi quem solicitou.
- Quem executou a tarefa foi o `disco-voador`, mas ele não teria feito se você não tivesse enviado a mensagem pedindo.
- A vaca também não sabia, tampouco você, como realizar a tarefa `abduzir`. Só o `disco-voador` sabia.
- A `vaca` não entrou no `disco-voador` por que quis. Ela foi o objeto da abdução, o parâmetro enviado na mensagem que chamou o método `abduzir`
- Quem passou a `vaca` como parâmetro foi você, que enviou a mensagem. Isso significa que coube a você a tarefa de, primeiro, identificar qual era a vaca (isso não aparece no código do exemplo, mas é lógico supor que precisou ter acontecido)

Nenhum objeto interferiu diretamente nem nas ações nem nas propriedades ou estados dos outros para realizar essa tarefa. Cada um cuidou das suas coisas. 

![Encapsulamento e troca de mensagens - objetos](/img/poo02/POO02-Encapsulamento-e-troca-de-mensagens-objetos.png)

Além disso, não foi solicitado ao objeto que ele fizesse algo que não saberia ou que não poderia fazer. O método `abduzir`, que recebe uma `Vaca` como parâmetro, estava definido para o `disco-voador` - alguém escreveu o código para esse método. 
