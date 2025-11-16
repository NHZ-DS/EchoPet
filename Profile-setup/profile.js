
const backBtn2 = document.querySelector("#back2");
const nextBtn2 = document.querySelector("#next2");
const logo = document.querySelector(".pet-logo img");

backBtn2.addEventListener("click", () => {
    window.location.href = "../Choosing-Pet/choosePet.html";
});

nextBtn2.addEventListener("click", () => {
    window.location.href = "../home-pg/homepg.html";
});