document.body.innerText = "Lucas"

input = document.createElement("input")

input.placeholder = 'Digite aqui'

document.body.appendChild(input)

document.bgColor = "yellow"

imagem = document.createElement("img")

imagem.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTItQz3sqR9Vb5Fvwew5IDnYYbNfixfy-e_xNvKGqQOY7VqdRCcX11l78746aZge92IF3Qxtj3uyr6gglX84tMpuNUpd3uHEiBm3IDoG1VM"

imagem.id = "lucas"

document.body.appendChild(imagem)

document.body.style.display = "grid"

document.body.style.alignContent = "center"


document.body.getAttribute(imagem).style.marginTop = 2
