
// Base strings
const GOALS_TEXT_PREFIX = "Completed: ";
const GOALS_TEXT_SUFFIX = "/5";

// Define main html elements
const goal_items = document.querySelectorAll(".item");
const u_goals_text = document.getElementById("universal-text");
const p_goals_text = document.getElementById("personal-text");

// Individual universal goals
const u_goal1 = document.getElementById("u-one");
const u_goal2 = document.getElementById("u-two");
const u_goal3 = document.getElementById("u-three");
const u_goal4 = document.getElementById("u-four");
const u_goal5 = document.getElementById("u-five");

// Individual personal goals
const p_goal1 = document.getElementById("p-one");
const p_goal2 = document.getElementById("p-two");
const p_goal3 = document.getElementById("p-three");
const p_goal4 = document.getElementById("p-four");
const p_goal5 = document.getElementById("p-five");

// Urls and types for universal goals
let goals_urls = ["/minigame_catching", "#", "#", "#", "#"];
let u_goals_type = ["catching-game", "sorting-game", "qr", "quiz", "survey", "wordle"]; // TODO: Implement auto selected images


// Set backgrounds for universal goals (hardcoded temporarily)
u_goal1.style.backgroundImage = "url(/static/sustainable_app/img/catching_game.jpg)";
u_goal2.style.backgroundImage = "url(/static/sustainable_app/img/sorting_game.png)";
u_goal3.style.backgroundImage = "url(/static/sustainable_app/img/qr.png)";
u_goal4.style.backgroundImage = "url(/static/sustainable_app/img/qr.png)";
u_goal5.style.backgroundImage = "url(/static/sustainable_app/img/qr.png)";

// Set background for personal goals (hardcoded temporarily)
p_goal1.style.backgroundImage = "url(/static/sustainable_app/img/workout.png)";
p_goal2.style.backgroundImage = "url(/static/sustainable_app/img/plastic_bottle.png)";
p_goal3.style.backgroundImage = "url(/static/sustainable_app/img/cat_recycle.png)";
p_goal4.style.backgroundImage = "url(/static/sustainable_app/img/paper.png)";
p_goal5.style.backgroundImage = "url(/static/sustainable_app/img/watermelon.png)";


function setGoalText() {
    let u_num = 0;
    let p_num = 0;

    // Increment each number
    goal_items.forEach(item => {

        if(item.getAttribute("value") == "var(--completion-green)") {

            switch (item.getAttribute("name")) {
                case "universal":
                    u_num++;
                    break;

                case "personal":
                    p_num++;
                    break;
            }
        }
    });

    // Display numbers
    u_goals_text.innerText = GOALS_TEXT_PREFIX + u_num + GOALS_TEXT_SUFFIX
    p_goals_text.innerText = GOALS_TEXT_PREFIX + p_num + GOALS_TEXT_SUFFIX
}


function setRedirects() {
    // redirects
    for(let i = 0; i < goal_items.length; i++) {
        goal_items[i].addEventListener("click", () => {

            if(goal_items[i].getAttribute("name") == "personal") {
                goal_items[i].setAttribute("value", "var(--completion-green)");
                loadColors();
                setGoalText();
            }
            else {
                window.location.replace(goals_urls[i]);
            }
        });
    };
}


function setClickEffects() {
    // button click effect
    for(let i = 0; i < goal_items.length; i++) {

        goal_items[i].addEventListener("touchstart", () => {
            goal_items[i].style.transform = "scale(80%, 80%)";
        });

        goal_items[i].addEventListener("touchend", () => {
            goal_items[i].style.transform = "scale(100%, 100%)";
        });
    };
}


function loadColors() {
    // setting completed color
    goal_items.forEach(item => {
        item.style.setProperty("--background-completed", item.getAttribute("value"));
    });
}

// Initialize screen
setRedirects();
setClickEffects();
loadColors();
setGoalText();
