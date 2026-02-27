let currentStepNum = 1;
const completedSteps = new Set();
const totalSteps = 15;


document.addEventListener("DOMContentLoaded", () => {
    setupNav();
    updateUI();
});

function setupNav() {
    // const nav = document.getElementById("navContainer");
    const nav = document.querySelector(".nav-container");
    // nav.querySelectorAll("button").forEach(b => b.remove());
    for (let i = 1; i <= totalSteps; i++) {
        const btn = document.createElement("button");
        btn.className = `nav-btn ${i == 1 ? 'active' : ''}`;
        btn.innerText = i;
        btn.onclick = () => goToStep(i)
        btn.id = `nav-btn-${i}`;
        nav.appendChild(btn);
    }
}

function markComplete(step) {
    document.querySelectorAll(".nav-btn")[step - 1].classList.add("completed");
    completedSteps.add(step)
}

function celebrateCompletion() {
    markComplete(15);
    alert("🥳 Parabéns! Você completou todas o curso de POO com JavaScript!\n\n Agora você domina:\nObjetos e métdos\nClasses ES6\n Herança e muito mais");
}

function goToStep(step) {
    if (step < 1 || step > totalSteps) {
        return
    }
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));

    document.getElementById(`step${step}`).classList.add("active");

    document.querySelectorAll(".nav-btn").forEach((b, index) => {
        b.classList.remove("active")
        if (index + 1 === step) b.classList.add("active");
    });

    currentStepNum = step;

    document.getElementById("currentStep").textContent = step;
    document.getElementById('stepIndicator').textContent = step;


    updateUI(step);
}

function updateUI(step) {
    const percent = (step / totalSteps) * 100;
    document.getElementById("progressFill").style.width = `${percent}%`;
    document.getElementById("currentStep").innerText = `${step} de ${totalSteps}`;

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function runCode(step) {
    const consoleDiv = document.getElementById(`console${step}`);
    // consoleDiv.innerHTML = "";
    const output = document.createElement("div");
    output.style.color = "white";

    switch (step) {
        case 1:
            output.innerText = "> au au!";
            break;
        case 2:
            output.innerText = "> Olá Lucas";
            break;
        default:
            output.innerText = "> Código executado com sucesso.";
    }

    consoleDiv.appendChild(output);
}

function nextStep() {
    goToStep(currentStepNum + 1);
}

function prevStep() {
    goToStep(currentStepNum - 1);
}