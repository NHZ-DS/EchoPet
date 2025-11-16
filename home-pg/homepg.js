const shopBtn = document.querySelector(".toggle");
const shopPanel = document.querySelector(".shop-panel");
const bg = document.querySelector(".home-bg");
const container = document.querySelector(".container");

shopBtn.addEventListener("click", () => {
    shopPanel.classList.toggle("open");
    bg.classList.toggle("dim");
    container.classList.toggle("dim");
});