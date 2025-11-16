const shopBtn = document.querySelector(".toggle");
const shopPanel = document.querySelector(".shop-panel");
const bg = document.querySelector(".home-bg");
const container = document.querySelector(".container");

const popup = document.getElementById("lessonPopup");
const closePopup = document.getElementById("closePopup");

shopBtn.addEventListener("click", () => {
    shopPanel.classList.toggle("open");
    bg.classList.toggle("dim");
    container.classList.toggle("dim");
});

document.querySelectorAll(".lang").forEach(lang => {
    lang.addEventListener("click", () => {
        popup.style.display = "flex";
    });
});

closePopup.addEventListener("click", () => {
    popup.style.display = "none";
});

popup.addEventListener("click", (e) => {
    if (e.target === popup) {
        popup.style.display = "none";
    }
});
