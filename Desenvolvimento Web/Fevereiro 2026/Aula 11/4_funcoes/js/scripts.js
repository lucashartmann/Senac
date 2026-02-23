// 1 - Criando uma função

function minhaFuncao(){
    console.log("Testando");
    
}

minhaFuncao();

const minhaFuncaoEmVariavel = function(){
    console.log("Função em variável!");
    
}

minhaFuncaoEmVariavel();

function funcaoComParametro(txt) {
    console.log(`Imprimindo ${txt}`);
}

funcaoComParametro("Opa!");

// 2 - Return

const a = 10;
const b = 20;
const c = 30;
const d = 40;

function soma(n1, n2) {
    return n1 + n2;
}

const resultado = soma(a, b);

console.log(resultado);

console.log(soma(c,d));

// 3 - Escopo de função

function testandoEscopo() {
    let y = 20; // este y está declarado somente dentro da função
    console.log(`Y dentro da função: ${y}`);
}

testandoEscopo();

let y = 10; // este y está declarado fora da função

console.log(`Y fora da função: ${y}`);

// 4 - Escopo aninhado

let m = 20;

function escopoAninhado () {
    if (true) {
        let m = 30; // Recebe o 30 apenas dentro do IF. 
        console.log(m);
        
    } 
    console.log(m); // Ao sair do IF, ele volta para o valor global.

}

escopoAninhado();

// 5 - Arrow function

const testeArrow = () => {
    console.log("Esta é uma Arrow Function");
    
}

testeArrow();

const parOuImpar = (n) => {
    if (n %2 === 0) {
        console.log("Par");
        return;
    }
    console.log("Ímpar");
}

parOuImpar(5);
parOuImpar(2);

// 6 - Mais sobre Arrow Function

const raizQuadrada = (x) => {
    return x*x;    
}

const raizQuadrada2 = (n) => n*n;

console.log(raizQuadrada(4));
console.log(raizQuadrada2(2));

const helloWorld = () => console.log("Hello, World!");

helloWorld();

// 7 - Parâmetro opcional

const multiplication = function (n, m) {
    if (m === undefined) {
        return n * 2;
    } else {
        return n * m;
    }
};

console.log(multiplication(4, 4)); // resultado será 16
console.log(multiplication(4)); // resultado será 8, pois o m será indefinido

const greeting = (name) => {
    if(!name) {
        console.log("Olá!");
        return;        
    }
    console.log(`Olá, ${name}!`);
}

greeting();
greeting("Leo");

// 8 - Valor default

const customGreeting = (name, greet = "Olá") => {
    return `${greet}, ${name}!`;
}

console.log(customGreeting("Leleo"));
console.log(customGreeting("Leleo", "Bem-vindo"));

const repeatText = (text, repeat = 2) => {
    for (let i =0; i < repeat; i++) {
        console.log(text);
    }
};

repeatText("Testando");
repeatText("Agora repete 5x", 5);

// 9 - Closure

function someFunction () {
    let txt = "Alguma coisa";

    function display (){
        console.log(txt);
        
    };

    display();

}

someFunction();

// 10 - Mais sobre closure

const multiplicationClosure = (n) => {
    return (m) => {
        return n*m;
    }
}

const c1 = multiplicationClosure(5);
const c2 = multiplicationClosure(10);

console.log(c1);
console.log(c2);


console.log(c1(5));
console.log(c2(10));


// 11 - Recursão 

const untilTen = (n, m) => {
    if (n < 10) {
        console.log("A função parou de executar!");
       
    } else {
        const x = n - m;
        console.log(x);
        
        untilTen(x, m);
    }
} 

untilTen(100, 1);