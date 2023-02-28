const goal_items = document.querySelectorAll(".item");
const click_effects = document.querySelectorAll(".click-effect");
const goal1 = document.getElementById("u-one");
const goal2 = document.getElementById("u-two");

goal1.style.backgroundImage = "url(/static/sustainable_app/img/test_home_tile.jpg)";

let u_goals_urls = ["/minigame_catching", "#", "#", "#", "#"];
let u_goals_complete = ["green", "grey", "grey", "grey", "grey"];

//TODO: implement images
let u_goals_type = ["game", "qr", "quiz", "survey"];

// redirects
for(let i = 0; i < goal_items.length; i++) {
    goal_items[i].addEventListener("click", () => {
        window.location.replace(u_goals_urls[i]);
    });
};

// button click effect
for(let i = 0; i < goal_items.length; i++) {

    goal_items[i].addEventListener("touchstart", () => {
        goal_items[i].style.transform = "scale(80%, 80%)";
    });

    goal_items[i].addEventListener("touchend", () => {
        goal_items[i].style.transform = "scale(100%, 100%)";
    });
};


// setting completed color
goal_items.forEach(item => {
    item.style.setProperty('--background-completed', item.getAttribute('value'));
});