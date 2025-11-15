const backBtn = document.querySelector("#back");
const nextBtn = document.querySelector("#next");

const foxBtn = document.querySelector("#baby-fox");
const puppyBtn = document.querySelector("#puppy");
const catBtn = document.querySelector("#kitty");
const petChoices = document.querySelectorAll(".pet");
for(let choice of petChoices){
    choice.addEventListener("click", () => {
        let userPet = choice.getAttribute("id");
        userInfo.pet = userPet;
    })
}

const userInfo = {
    pet: "",
    language: ""
};

console.log(userInfo.pet)
 
backBtn.addEventListener("click", () => {
    window.location.href = "../Start-page/start.html";
});

nextBtn.addEventListener("click", () => {
    window.location.href = "../Choosing-lang/language.html";
});