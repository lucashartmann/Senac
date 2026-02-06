console.error("Erro! Seu PC foi hackeado!");
console.warn("Cuidado!");

const M = 10;

if (M > 5) {
    console.log("M maior que 5");
}

const USER = "João";

if (USER === "João") {
    console.log("User é João!");
}

const loggedIn = false;

if (loggedIn) {
    console.log("Usuário logado!");
} else {
    console.log("Usuário não autenticado");
}

const q = 10;
const w = 15;

if (q > 5 && w > 20) {
    console.log("Números mais altos");
} else {
    console.log("Números não são altos o suficiente");
}


if (1 > 2) {
    console.log("Teste");
} else if (2 > 3) {
    console.log("Teste2");
} else if (5 > 1) {
    console.log("Agora sim");
}

const userName = "Claudio";
const userAge = 23;

if (userName === "Claudio") {
    console.log("Bem vindo Claudio!");
} else if (userName === "Claudio" && userAge === 23) {
    console.log("Olá Claudio de 23 anos");
} else {
    console.log("Nenhuma condição aceita!");
}

let p = 0;

while (p < 5) {
    console.log(`Repetindo ${p}`);
    p++;
}

let o = 10;

do {
    console.log(`Valor de o: ${o}`);
    o--; // o = o - 1;
} while (o > 0);

for (let i = 0; i < 10; i++) {
    console.log("i " + i);
}

let r = 10;

for (r; r > 0; r--) {
    console.log("r: " + r);
}

console.log("r: " + r);

for (let u = 0; u < 10; u++) {
    if (u * 2 > 10) {
        console.log("Maior que 10! " + u + " " + u * 2);
    } else {
        if (u / 2 === 0) {
            console.log("Deu 0");
        }
    }
}

for (let g = 20; g > 10; g--) {
    console.log("O g é " + g);
    if (g === 12) {
        console.log("Chegamos no 12!");
        break;
    }
}

for (s = 0; s < 10; s++) {
    if (s % 2 === 0) {
        console.log("Número par! " + s);
        continue;
    }
    console.log("Impar " + s)
}

const job = "Advogado";

switch (job) {
    case "Programador":
        console.log("Voce é programador");
        break;
    case "Advogado":
        console.log("Voce é advogado");
        break;
    case "Engenheiro":
        console.log("Voce e engenheiro");
        break;
    default:
        console.log("Voce nao existe")
}

const l = 100;

switch(l) {
    case 200:
        console.log("L é 200");
    case 100:
        console.log("L é 100");
    case 10:
        console.log("L é 10!");
    default:
        console.log("L não foi encontrado!")
}