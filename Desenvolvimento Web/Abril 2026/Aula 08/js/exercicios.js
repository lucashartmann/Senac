class Prato {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }
}


function pesquisa() {
    const input = document.getElementById("search-box");
    const valor = input.value.toLowerCase();
    // console.log(valor);
    const section_dishes = document.getElementById("dishes");
    const divs_boxes = section_dishes.querySelectorAll(".box");
    // console.log(divs_boxes);
    divs_boxes.forEach(element => {
        const h3 = element.querySelector("h3");
        const texto = h3.innerText.toLowerCase();
        if (texto.includes(valor)) {
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
    JSON.parse(dados).forEach(dado => {
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
    console.log("adicionado ao carrinho:", objetos_clicados);
}


document.addEventListener("submit", () => {
    event.preventDefault();
    const section_order = document.getElementById("order");
    const form_html = section_order.querySelector("form");
    // console.log(form_html);
    const form = new FormData(form_html);
    // console.log(form);
    console.log("Pedido:");
    form.entries().forEach(element => {
        console.log(`${element[0]}: ${element[1]}`);
    });

    form_html.reset();

});

document.addEventListener("DOMContentLoaded", inicializar());

document.querySelector(".fa-shopping-cart").addEventListener("mouseover", mostrarCarrinho);

document.querySelector(".fa-shopping-cart").addEventListener("mouseout", () => {
    if (document.querySelector("#dropdown")) {
        document.querySelector("#dropdown").style.display = "none";
    }
});

async function mostrarCarrinho(event) {
    
    let div_nav = document.querySelector(".icons");
    let div_dropdown = document.createElement("div");
    let div_dropdown_content = document.createElement("div");
    if (document.querySelector("#dropdown")) {
       
        div_dropdown = document.querySelector("#dropdown");
        div_dropdown_content = document.querySelector("#dropdown #dropdown-content");
        while (div_dropdown_content.firstChild) {
            await div_dropdown_content.removeChild(div_dropdown_content.firstChild);
        }
        objetos_clicados.forEach(objeto => {
            var div = document.createElement("div");
            div.style.display = "flex";
            div.innerHTML = `<h3>Nome: ${objeto.nome}, preço:<span>R$${objeto.preco}</span></h3>
            <button class="btn" onclick="removerDoCarrinho('${objeto.nome}')">Remover</button>`;
            div_dropdown_content.appendChild(div);
        });

        div_dropdown.style.display = "block";
       

        return
    }


    div_dropdown.id = "dropdown";
    div_dropdown.style.display = "block";

    div_dropdown_content.id = "dropdown-content";

    objetos_clicados.forEach(objeto => {
        var h3 = document.createElement("h3");
        h3.innerText = `Nome: ${objeto.nome}, preço: ${objeto.preco};`
        div_dropdown_content.appendChild(h3);
    });
   
    div_dropdown.appendChild(div_dropdown_content);
    div_nav.appendChild(div_dropdown);

}