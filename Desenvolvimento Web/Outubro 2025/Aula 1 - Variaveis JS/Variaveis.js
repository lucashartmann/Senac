// Para executar -> node Variaveis.js

// var (variável): pode mudar valor e referência

var a = 10

var b = 20

console.log("a", a)

var a = "dfdfsd"

console.log("a", a)

console.log("b", b)

// const (constante): pode mudar valor mas não a referência

const c  = 30

console.log("c", c)


const v  = [1,2,3]

console.log("v", v)

v.push(4)

console.log("v", v)

// let (seja): não pode redeclarar, se tem let x, não pode ter outro let x

let x = 10
// lex x = 20 Errado

console.log("x", x)

let x2 = 5

{
    let x2 = 10
    x2 = 20
}

console.log("x2", x2)

