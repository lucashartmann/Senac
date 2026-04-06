function pesquisa() {
    const input = document.getElementById("search-box");
    const valor = input.value;
    console.log(valor);
    const section_dishes = document.getElementById("dishes");
    divs_boxes = section_dishes.querySelectorAll(".box");
    console.log(divs_boxes);
    divs_boxes.forEach(element => {
        const h3 = element.querySelector("h3");
        if (h3.innerText.includes(valor)) {
            element.style.display = "block";
            console.log("pedro")
        }else {
            element.style.display = "none";
        }
    });
}