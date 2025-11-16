const backBtn = document.querySelector("#back");
const nextBtn = document.querySelector("#next");
const saveBtn = document.querySelector("#save");

// const foxBtn = document.querySelector("#baby-fox");
// const puppyBtn = document.querySelector("#puppy");
// const catBtn = document.querySelector("#kitty");
const petChoices = document.querySelectorAll(".pet");

let nameInput = document.querySelector("input");

class petInfo{
    constructor(petName, type, mood){
        this.petName = petName;
        this.type = type;
        this.mood = mood;
    }
}
class userInfo extends petInfo{
    constructor(petName, type, mood, userName, bio, xp, coins, language){
        super(petName, type, mood);
        this.userName = userName;
        this.bio = bio;
        this.xp = xp;
        this.coins = coins;
        this.language = language;
    }
}

let petName = "";
let petType = "";
let petMood = "neutral";

let pet1 = new petInfo(petName, petType, petMood);

for(let choice of petChoices){
    choice.addEventListener("click", () => {
        petChoices.forEach((ch) => {
            ch.classList.remove("selected");
        });
        choice.classList.add("selected");
        let userPet = choice.getAttribute("id");
        petType = userPet;
    })
}

nameInput.addEventListener("input", () => {
    petName = nameInput.value;
});

function updatePetInfo(name, type, mood) {
    pet1.petName = name;
    pet1.type = type;
    pet1.mood = mood;
}
 
backBtn.addEventListener("click", () => {
    window.location.href = "../Start-page/start.html";
});

nextBtn.addEventListener("click", () => {
    window.location.href = "../Profile-setup/profile.html";
});

saveBtn.addEventListener("click", ()=> {
    updatePetInfo(petName, petType, petMood);
    console.log(pet1.petName);
    console.log(pet1.type);
    console.log(pet1.mood);
});