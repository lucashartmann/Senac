// 1 - Arrays

const lista = [1, 2, 3, 4, 5]

console.log(lista);
console.log(typeof lista);

const itens = ["Roberto", true, 2, 4.12];

console.log(itens);

// 1.1 - Adicionando itens na lista

lista.push(6); // PUSH - Adiciona ao final da lista 
console.log(lista);

lista.unshift(0); // UNSHIFT - Adiciona ao início da lista
console.log(lista);

// 1.2 - Removendo itens da lista
const itens2 = ["Roberto", true, 2, 4.12];

console.log(itens2);

itens2.pop(); // POP - Remove o último elemento da lista
console.log(itens2);

itens2.shift(); //  SHIFT - Remove o primeiro elemento da lista
console.log(itens2);

// 2 - MAis sobre arrays

const arr = ["a", "b", "c", "d"]

console.log(arr[0]);
console.log(arr[2]);
console.log(arr[10]);

// 3 - Propriedades 

const numbers = [5, 12, 3, 22]
console.log(numbers.length); // LENGTH - diz o tamanho da lista
console.log(numbers["length"]);

// 4 - Métodos

const otherNumbers = [1, 2, 3];

const allNumbers = numbers.concat(otherNumbers)

console.log(allNumbers);

const text = "algum texto";
console.log(text.toUpperCase()); // Transforma tudo em caixa alta
console.log(typeof text.toUpperCase());

console.log(text.indexOf("g")); // Retorna a primeira entrada do argumento

// 5 - Objetos - Object Literals

const person = {
    name: "Leo",
    age: 30,
    job: "Programador"
}

console.log(person.name);
console.log(person.name.length);
console.log(typeof person);


// 6 - Criando e deletando propriedades

const car = {
    engine: 2.0,
    brand: "VW",
    model: "Tiguan",
    km: 20000
}

console.log(car);

car.doors = 4; // Adicionando uma nova propriedade ao mapa
console.log(car);

delete car.km; // Deletando a propriedade do  mapa
console.log(car);

// 7 - Mais sobre objetos

const obj = {
    a: "teste",
    b: true
}

console.log(obj instanceof Object); // Verifica se está retornando um objeto

const obj2 = {
    c:  [],
};

Object.assign(obj2, obj) // Vai copiar para dentro do obj2
console.log(obj2);

// 8 - Mais sobre objetos (de novo)

console.log(Object.keys(obj)); // Retorna as chaves do mapa
console.log(Object.values(obj)); // Retorna os valores do mapa

console.log(Object.keys(person));
console.log(Object.values(person));

console.log(Object.entries(obj2)); // Retorna arrays com chave e valor

// 9 - Mutação 

const a = {
    name: "Leonardo",
};

const b = a;

console.log(a);
console.log(b);

console.log(a === b);

a.age = 30;
console.log(b);

delete b.age;
console.log(b);
console.log(a);

// 10 - Loop de arrays

const users = ["Arthur", "Leonardo", "Lucas", "Matheus", "Yuri", "William"]

for(let i=0; i<users.length; i++){
    console.log(`Listando usuário: ${users[i]}`);
};

// 11 - IndexOf e LastIndexOf

const myElements = ["Morango", "Maçã", "Abacate", "Pêra", "Abacate"]

console.log(myElements.indexOf("Maçã"));
console.log(myElements.indexOf("Abacate"));

console.log(myElements[2]);
console.log(myElements[myElements.indexOf("Abacate")]);

console.log(myElements.lastIndexOf("Abacate"));


console.log(myElements.includes("Abacate"));
console.log(myElements.includes("Sapo"));





