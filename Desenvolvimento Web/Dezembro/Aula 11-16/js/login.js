let inputNome = document.getElementById('usuario')
let inputSenha = document.getElementById('senha')



function changeScreen() {

    if (document.getElementById('cadastro').style.display == "block") {
        document.getElementById('login').style.display = "block"
        document.getElementById('cadastro').style.display = "none"
    } else {
        document.getElementById('login').style.display = "none"
        document.getElementById('cadastro').style.display = "block"
    }

}

valor_nome = inputNome.value
valor_senha = inputSenha.value