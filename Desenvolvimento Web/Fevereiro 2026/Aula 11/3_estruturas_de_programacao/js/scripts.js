// 1 - Variáveis

let nome = "Leo";
console.log(nome);

nome = "Leonardo";
console.log(nome);

const IDADE = 30;
console.log(IDADE);

console.log(typeof nome);
console.log(typeof IDADE);

// 2 - Mais sobre variáveis

let a = 10, b = 20, c = 30;
console.log(a, b, c);

const nomecompleto = "Leo Leo";
const nomeCompleto = "Leozinho Leozinho";

console.log(nomeCompleto, nomecompleto);

let _teste = "Válido"
let $teste = "também válido"
console.log(_teste, $teste);

// 3 - Prompt - exibe janela para digitação de string

const age = prompt("Digite sua idade: ");
console.log(`Você tem ${age} anos!`);

// 4 - Alert - exibe janela de alerta no navegador

alert("Testando!");

const z = 10;
alert(`O número é ${z}`);

// 5 - Math

console.log(Math.max(5, 2, 4, 1, 10, 23));
console.log(Math.min(5, 2, 4, 1, 10, 23));
console.log(Math.floor(5.14));
console.log(Math.ceil(5.14));

// 6 - Console

console.log("teste");
console.error("Erro!");
console.warn("Aviso!");

// 7 - Estrutura de controle If

const M = 10;

if (M > 5){
    console.log ("M é maior que 5");
}

const USER = "João";
if(USER === "João"){
    console.log("Olá, João!");
}

// 8 - Else

const loggedIn = false;

if (loggedIn){
    console.log("Usuário autenticado!");
} else {
    console.log("Usuário não autenticado");
}

const q = 10;

const w = 15;

if (q>5 && w>20){
    console.log("Números mais altos!");
} else {
    console.log("Números não são altos o suficiente!");
    
}

// 9 - Else If

if (1 > 2) {
    console.log("Teste");
    
} else if (2 > 3) {
    console.log("Teste 2");
    
} else if (5 > 1) {
    console.log("Teste 3");
    
}

const userName = "Claudio";
const userAge = 23;

if (userName === "Claudio") {
    console.log("Bem vindo, Cláudio!");
    
} else if (userName === "Claudio" && userAge ==23) {
    console.log("Olá, Cláudio, você tem 23 anos");
    
} else {
    console.log("Nenhuma condução aceita");
    
}

// 10 - While

let p = 0;

while (p < 5) {
    console.log(`Repetindo ${p}`);
    p++; // auto incrementa a cada iteração
}

// 11 - Do while
let o = 10;

do {
    console.log(`Valor de o: ${o}`);
    // o = o - 1;
    o --;
} while (o > 11);

// 12 - For

for (let t = 0; t < 10; t++) { // inicia a variável; até quando vai manter; quanto vai incrementando ela
    console.log("Repetindo...");
    
}

let r = 10;

for (r; r > 0; r = r-1) {
    console.log(`O r está diminuindo: ${r}`);
}
console.log(r);

// 13 - Identação

for (let u = 0; u < 10; u++){
    if (u*2 > 10) {
        console.log(`${u*2} é maior que 10!`);
        
    } else {
        if (u/1 === 0) {
            console.log("Deu 0");
            
        } // fim do if interno
    } //fim do else
} // fim do for

// 14 - Break

for (let g = 20; g > 10; g--) {
    console.log(`O g é ${g}`);
    if (g === 12) {
        console.log("Chegamos no 12!");
        break;
    } // fim do if
} // fim do laço for

// 15 - Continue

for (s = 0; s < 10; s++) {
    if (s%2 === 0) {
        console.log("Número par!");
        continue;   
    } 
    console.log(s);
     
}

// 16 - Switch

const job = "Advogado";

switch (job) {
    case "Programador": 
        console.log("Você é um programador!");
        break;
    case "Advogado":
        console.log("Você é um advogado");
        break;
    case "Engenheiro":
        console.log("Você é um engenheiro");
        break;
    default:
        console.log("Profissão não encontrada");
        
        
} // fecha o switch

// 16.1 - Switch errado

const l = 100;

switch(l) {
    case 200:
        console.log("L é 200");
    case 100:
        console.log("L é 100");
    case 10:
        console.log("L é 10");
    default: log("L não foi encontrado");

}
