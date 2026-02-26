let currentStep = 1;
const totalSteps = 6;


document.addEventListener("DOMContentLoaded", () => {
    setupNav();
    updateUI();
});

function setupNav() {
    // const nav = document.getElementById("navContainer");
    const nav = document.querySelector("#navContainer");
    nav.querySelectorAll("button").forEach(b => b.remove());

    for (let i = 1; i <= totalSteps; i++) {
        const btn = document.createElement("button");
        btn.className = `nav-btn ${i == 1 ? 'active' : ''}`;
        btn.innerText = i;
        btn.onclick = () => goToStep(i)
        btn.id = `nav-btn-${i}`;
        nav.appendChild(btn);
    }
}

function goToStep(step) {
    if (step < 1 || step > totalSteps) {
        return
    }
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
    document.getElementById(`step${step}`).classList.add("active");

    document.querySelectorAll(".nav-btn").forEach(b => b.classList.remove("active"));
    document.getElementById(`nav-btn${step}`).classList.add("active");

    currentStep = step;
    updateUI();
}

function updateUI() {

}

function runExample(i) {

}

function nextStep() {

}