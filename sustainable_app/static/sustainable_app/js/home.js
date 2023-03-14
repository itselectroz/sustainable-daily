
// Base strings
const GOALS_TEXT_PREFIX = "Completed: ";
const GOALS_TEXT_SUFFIX = "/5";

// Define main html elements
const goal_items = document.querySelectorAll(".item");
const personal_goals = document.querySelectorAll(".personal");
const u_goals_text = document.getElementById("universal-text");
const p_goals_text = document.getElementById("personal-text");


// Urls and types for universal goals
let goals_urls = ["/minigame_catching/", "/sorting/", "#", "#", "#"];
let u_goals_type = ["catching-game", "sorting-game", "qr", "quiz", "survey", "wordle"]; // TODO: Implement auto selected images

// Images array
let personal_images = ["workout.png", "plastic_bottle.png", "cat_recycle.png", "paper.png", "watermelon.png"]


function setImages() {
    for(let i = 0; i < personal_goals.length; i++) {
        personal_goals[i].style.backgroundImage = "url(/static/sustainable_app/img/" + personal_images[i] + ")";
    }
}

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
setClickEffects();
loadColors();
setGoalText();
setRedirects();
setImages();

// request to complete a goal
$(document).ready(function() {

    // Request for character
    $('.personal').on('click', function() {

        $goal_id = this.getAttribute("id")

        $.ajax({
            type: "POST",
            url: "complete_personal/",
            data: {
                goal_id: $goal_id,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});