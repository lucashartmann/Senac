class Prato {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }
}


function pesquisa() {
    const input = document.getElementById("search-box");
    const valor = input.value;
    // console.log(valor);
    const section_dishes = document.getElementById("dishes");
    const divs_boxes = section_dishes.querySelectorAll(".box");
    // console.log(divs_boxes);
    divs_boxes.forEach(element => {
        const h3 = element.querySelector("h3");
        if (h3.innerText.includes(valor)) {
            element.style.display = "block";
            // console.log("pedro")
        } else {
            element.style.display = "none";
        }
    });
}

// localStorage.clear();

const dados = localStorage.getItem("pratos");

var objetos_clicados = [];

if (dados) {
    JSON.parse(dados).forEach(dado =>{
        var prato = new Prato(dado.nome, dado.preco);
        objetos_clicados.push(prato);
    })
    // objetos_clicados = [];
}




function inicializar() {
    adicionar_evento();
    console.log("carrinho:", objetos_clicados);
}

function adicionar_evento() {
    botoes = document.querySelectorAll(".btn");
    botoes.forEach(botao => {
        // console.log(botao.innerText)
        if (botao.innerText.includes("carrinho") || botao.innerText.includes("Carrinho")) {
            botao.addEventListener("click", () => carrinho(botao));
        }
    });
}

function carrinho(event) {
    const botao = event;
    // console.log(botao)
    const div = botao.parentElement;
    const nome = div.querySelector("h3").innerText;
    const preco = div.querySelector("span").innerText.split("R$")[1];
    var prato = new Prato(nome, preco);
    objetos_clicados.push(prato);
    localStorage.setItem("pratos", JSON.stringify(objetos_clicados));
    console.log("carrinho:", objetos_clicados);
}

document.addEventListener("submit", () => {
    event.preventDefault();
    const section_order = document.getElementById("order");
    const form_html = section_order.querySelector("form");
    // console.log(form_html);
    const form = new FormData(form_html); 
    // console.log(form);
    form.entries().forEach(element => {
        console.log(`${element[0]}: ${element[1]}`);
    });

});

document.addEventListener("DOMContentLoaded", inicializar());