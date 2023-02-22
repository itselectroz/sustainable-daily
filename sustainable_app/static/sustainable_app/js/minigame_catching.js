
// Define html elements
const player = document.getElementById("player");
const rubbish_group = document.querySelector(".rubbish_group");
const playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
const playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));

// Different screens
const menuScreen = document.getElementById("menu");
const container = document.getElementById("container");
const gameOverScreen = document.getElementById("gameOver");
const gameOverText = document.getElementById("gameOverText");

// Game over boolean
let gameOver = false;
let rubbishTimeout;

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
    rubbish.setAttribute("class", "rubbish " + type.obj);
    rubbish.style.backgroundImage = 'url(/static/sustainable_app/img/' + type.obj + '.png)';
    rubbish_group.appendChild(rubbish);

    // Randomize start pos
    let rubbishLeft = Math.floor(Math.random() * (container.offsetWidth - rubbish.offsetWidth));

    /**
     * Gives the rubbish gravity
     */
    function fallDown() {

        if(rubbishBottom > playerBottom && rubbishBottom < (playerBottom + (player.offsetHeight / 2)) && rubbishLeft > (player.offsetLeft - (player.offsetWidth / 2)) &&
        rubbishLeft < (player.offsetLeft + (player.offsetWidth / 2))) {
            rubbish_group.removeChild(rubbish);
            clearInterval(fallInterval);

            // Check which rubbish type
            if(type.type < 5) {
                score ++;
            }
            else {
                lostLife();
            }
        }
        if(rubbishBottom < playerBottom) {

            // Check which rubbish type
            if(type.type < 5) {
                lostLife();
            }
            rubbish_group.removeChild(rubbish);
            clearInterval(fallInterval);

            
        }
        rubbishBottom -= 10;
        rubbish.style.bottom = rubbishBottom + 'px';
    }

    let fallInterval = setInterval(fallDown, 20);
    
    rubbish.style.bottom = rubbishBottom + 'px';
    rubbish.style.left = rubbishLeft + 'px';
}

/**
 * Randomly picks rubbish
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
    }
    else {
        gameState("end");
    }
}

/**
 * Set game to certain state
 * @param {String} state 
 */
function gameState(state) {

    

    if(state == "start") {
        console.log("STARTED");
        rubbishTimeout = setInterval(generateRubbish, 1000);
        menu.style.display = "none";
        gameOverScreen.style.display = "none";
        container.style.display = "flex";
        gameOver = false;
        updateFrame();
        
    }
    else {
        console.log("ENDED");
        clearInterval(rubbishTimeout);
        gameOver = true;
        gameOverText.innerText = gameOverText.innerText + "\nScore: " + score;
        gameOverScreen.style.display = "flex";
        container.style.display = "none";
    }
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
    window.location.replace("/home");
}
