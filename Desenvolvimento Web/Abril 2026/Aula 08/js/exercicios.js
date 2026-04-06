function pesquisa() {
    const input = document.getElementById("search-box");
    const valor = input.value;
    console.log(valor);
    const section_dishes = document.getElementById("dishes");
    divs_boxes = section_dishes.querySelectorAll(".box");
    console.log(divs_boxes);
    divs_boxes.forEach(element => {
        const h3 = element.querySelector("h3");
        console.log(h3.innerText)
        if (valor.contains(h3.innerText)) {
            element.style.display = "block";
        }else {
            element.style.display = "none";
        }
    });
}