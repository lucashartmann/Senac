let meuCarrinho = [];

formularioBusca = document.querySelector("#search-form");

formularioBusca.onsubmit = (event) => {
    event.preventDefault();
    formularioBusca.classList.remove("active");
    window.location.href = "#dishes";
}

let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');

botoesCarrinho.forEach(botao => {
    if (botao.innerText.toLowerCase().includes("carrinho")) {
        botao.onclick = (evento) => {
            evento.preventDefault();
            let pai = botao.parentElement;
            let nome = pai.querySelector("h3").innerText;
            let preco = pai.querySelector("span, .price").innerText;
            let prato = {
                nome: nome,
                preco: preco
            }
            meuCarrinho.push(prato);
            localStorage.setItem("pratos", JSON.stringify(meuCarrinho));
            console.log("Carrinho atualizado:", meuCarrinho);
        };
    }
});

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}