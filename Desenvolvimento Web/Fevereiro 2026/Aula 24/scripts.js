const array = ["a", "b", "c", "d", "e", "f"];

const corte = array.slice(0, -2);
const corte1 = array.slice(0, -1);
const corte2 = array.slice(1, 2);
const corte3 = array.slice(2);

console.log(array.slice(2));

const nums = [1,2,3,4,5];

nums.forEach(n => {
    console.log("O número atual é", n);
});

const posts = [
    {title: "Primeiro post", category: "PHP"},
    {title: "Segundo post", category: "JavaScript"},
    {title: "Terceiro post", category: "Python"}
];

posts.forEach((post) => {
    console.log("Exibindo post:", post.title, "\nda categoria:", post.category);
});

const brands = ["BMW", "VW", "Fiat"];

console.log(brands.includes("Fiat"));
console.log(brands.includes("Kia"));

if (brands.includes("BMW")) {
    console.log("Há carros da marca BMW!");
};

const reverse = [1,2,3,4,5];

console.log(reverse);

reverse.reverse();

console.log(reverse);

const trim = "      testando \n     ";
console.log(trim)
console.log(trim.trim())
console.log(trim.trim().length)

const pad = "1";
const number = pad.padStart(4, "0");

console.log(pad);
console.log(number);

const padEnd = number.padEnd(10, "0");

console.log(padEnd);

const frase = "O rato roeu a roupa do rei de Roma";

var arrayFrase = frase.split();
console.log(arrayFrase);

var arrayFrase = frase.split(" ");
console.log(arrayFrase);

var arrayFrase = frase.split("");
console.log(arrayFrase);

var arrayFrase = frase.split("r");
console.log(arrayFrase);

var arrayFrase = frase.split("r")[3];
console.log(arrayFrase);

const itens = ["Mouse", "Teclado", "Monitor"];

var joinExemplo = itens.join(",");
console.log(joinExemplo);

var joinExemplo = itens.join("-");
console.log(joinExemplo);

console.log("Precisamos comprar:", itens.join(" e "));

const palavra = "Testando";

console.log(palavra.repeat(10));

const somaInfinita = (...args) => {
    let total = 0;

    for(let i = 0; i < args.length; i++) {
        total += args[i];
    }

    return total;
};

console.log(somaInfinita(1, 5, 10));
console.log(somaInfinita(3, 3, 3));
console.log(somaInfinita(1, 2, 3, 4, 5, 6, 7, 7, 8, 9));

const somaInfinita2 = (...args) => {
    let total = 0;

    for(num of args) {
        total += num;
    }

    return total;
};

console.log(somaInfinita2(1, 5, 10));
console.log(somaInfinita2(3, 3, 3));
console.log(somaInfinita2(1, 2, 3, 4, 5, 6, 7, 7, 8, 9));


const user = {
    nome : "Lucas",
    sobrenome : "Souza",
    cargo: "Programador"
};


const {
    nome, sobrenome, cargo
} = user;

console.log(`${nome} ${sobrenome}, ${cargo}`);

const lista = ["Avião", "Submarino", "Carro"];

const [veiculoAreo, veiculoAquatico, veiculoTerreste] = lista;

console.log(veiculoAreo, veiculoAquatico, veiculoTerreste);

const json = '{"name": "Lucas", "age": 60, "skills":["PHP", "JavaScript", "Python"]}';

console.log(JSON.stringify(json));

const o = JSON.parse(json)

console.log(o)

const badJason = '{"name": Lucas, "age": 60.40, "skills":[PHP, JavaScript, "Python"]}';

// const a = JSON.parse(badJason)

// console.log(a)

// o.isOpenToWork = true;

const novoJson = JSON.stringify(o);

console.log(typeof(JSON.stringify(o)));