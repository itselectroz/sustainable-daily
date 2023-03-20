// Define html elements
const player = document.getElementById("player");
const rubbish_group = document.querySelector(".rubbish_group");
const playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
const playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));
const livesElement = document.getElementById("lives");

// Different screens
const menuScreen = document.getElementById("menu");
const container = document.getElementById("container");
const menuText = document.getElementById("menuText");
const menuButton = document.getElementById("btnMenu");

// Set element text
menuText.innerText = "Catching Game";

// Game over boolean
let gameOver = false;
let rubbishTimeout;
let speedTimeout;
let fallInterval;
let generateSpeed = 1000;

// Score and lives
let score = 0;
let lives = 2;

// Define X pos values
let x = 0;
let vxl = 0;
let vxr = 0;

/**
 * Update the rendered objects
 */
function updateFrame() {

    // Update X position based on velocity
    if(player.offsetLeft < (container.offsetWidth - player.offsetWidth)) {
        x += vxr;
    }

    if(player.offsetLeft > 0) {
        x += vxl;
    }

    // Move player
    player.style.left = x + 'px';
    
    // Check if game is over
    if(!gameOver) {
        requestAnimationFrame(updateFrame);
    }
}

/**
 * Generate rubbish
 */
function generateRubbish() {
    // Create piece of rubbish

    let rubbish = document.createElement('div');
    let rubbishBottom = container.offsetHeight;
    let type = getRandomClass();
    let isFalling = true;
    rubbish.setAttribute("class", "rubbish " + type.obj);
    rubbish.style.backgroundImage = 'url(/static/sustainable_app/img/' + type.obj + '.png)';
    rubbish_group.appendChild(rubbish);

    // Randomize start pos
    let rubbishLeft = Math.floor(Math.random() * (container.offsetWidth - rubbish.offsetWidth));

    /**
     * Gives the rubbish gravity
     */
    function fallDown() {

        if(!isFalling) {
            return;
        }

        if(rubbishBottom > playerBottom && rubbishBottom < (playerBottom + (player.offsetHeight / 2)) && rubbishLeft > (player.offsetLeft - (player.offsetWidth / 2)) &&
        rubbishLeft < (player.offsetLeft + (player.offsetWidth / 2))) {

            rubbish_group.removeChild(rubbish);
            isFalling = false;


            // Check which rubbish type
            if(type.type < 5) {
                score ++;
            }
            else {
                lostLife();
            }
            
            return;
        }
        if(rubbishBottom < playerBottom) {
            rubbishBottom = 1000;
            // Check which rubbish type
            if(type.type < 5) {
                lostLife();
            }

            
            rubbish_group.removeChild(rubbish);
            isFalling = false;


            return;
        }
        rubbishBottom -= 10;
        rubbish.style.bottom = rubbishBottom + 'px';
    }

    fallInterval = setInterval(fallDown, 20);
    
    rubbish.style.bottom = rubbishBottom + 'px';
    rubbish.style.left = rubbishLeft + 'px';
}

/**
 * Randomly picks rubbish
 * 
 * @returns The name and type of rubbish
 */
function getRandomClass() {
    let chosen = Math.floor(Math.random() * 10);
    let arr_rubbish = ["can", "plastic_bottle", "paper", "glass_bottle", "milk", "jelly", "crisps", "plastic_bag", "banana", "sweet"];
    
    return {"obj": arr_rubbish[chosen],
    "type": chosen};
}

/**
 * Player loses life
 */
function lostLife() {

    // Check if out of lives
    if(lives > 0) {
        lives -= 1;
        livesElement.removeChild(livesElement.lastElementChild)
    }
    else {
        gameState("end");
        livesElement.removeChild(livesElement.lastElementChild)
    }
}

/**
 * Create a new life div element
 * 
 * @returns life div element
 */
function createLives(num) {

    for(i = 0; i < num; i++) {
        let newLife = document.createElement('div');
        newLife.setAttribute("class", "life");
        livesElement.appendChild(newLife);
    }
}

/**
 * Set game to certain state
 * 
 * @param {String} state 
 */
function gameState(state) {

    if(state == "start") {
        createLives(3);
        menu.style.display = "none";
        menuScreen.style.display = "none";
        container.style.display = "flex";
        gameOver = false;
        lives = 2;
        score = 0;
        updateFrame();
        increaseSpeed();
    }
    else {
        clearInterval(rubbishTimeout);
        clearInterval(fallInterval);
        clearTimeout(speedTimeout);
        removeRubbish();
        
        gameOver = true;
        generateSpeed = 1000;
        menuButton.textContent = "Play Again";
        menuText.innerText = "Game Over\nScore: " + score;
        menuScreen.style.display = "flex";
        container.style.display = "none";
        add_score(score,"minigame_catching");
    }
}

/**
 * Increases the speed of the rubbish falling
 */
function increaseSpeed() {
    generateSpeed -= 50;
    clearInterval(rubbishTimeout);
    clearTimeout(speedTimeout);
    rubbishTimeout = setInterval(generateRubbish, generateSpeed);
    speedTimeout = setTimeout(increaseSpeed, 5000);
}

/**
 * Remove all rubbish
 */
function removeRubbish() {
    let group = document.getElementById('rubbish_group');
    group.innerHTML = '';
}

/**
 * Start the game
 */
function startGame() {
    gameState("start");
}

/**
 * Exit the game
 */
function exitGame() {
    window.location.replace("/home/");
}
