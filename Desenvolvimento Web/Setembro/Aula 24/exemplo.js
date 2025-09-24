texto = document.querySelector("p")
texto.innerText = "Lucas"

texto.addEventListener("mouseover", mudaCor)

function mudaCor() {
    texto.style = "color:blue"
}