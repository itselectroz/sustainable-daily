// HTML elements
const container = document.getElementById("container");
const rubbish = document.getElementById("spawn");
const scoreLabel = document.getElementById("score");
const bins = document.querySelectorAll(".bin");
const touchLeft = document.getElementById("left-button");
const touchRight = document.getElementById("right-button");
const menuScreen = document.getElementById("menu");
const menuText = document.getElementById("menuText");
const menuButton = document.getElementById("btnMenu");
const buttonContainer = document.querySelector(".test");

menuText.innerText = "Catching Game";

// Items
const items = [
    { "image":"can.png", "alt":"Can", "bin":"recycle", "points":1 },
    { "image":"wine_glass.png", "alt":"Wine Glass", "bin":"glass", "points":1 },
    { "image":"jar.png", "alt":"Jar", "bin":"glass", "points":2 },
    { "image":"plastic_bag.png", "alt":"Plastic Bag", "bin":"general", "points":1 },
    { "image":"milk.png", "alt":"Milk ", "bin":"recycle", "points":2 },
    { "image":"crisps.png", "alt":"Crisp Packet", "bin":"general", "points":1 },
    { "image":"paper.png", "alt":"Paper", "bin":"recycle", "points":1 },
    { "image":"glass_bottel.png", "alt":"Wine Bottle", "bin":"glass", "points":1 },
    { "image":"plastic_bottel.png", "alt":"Plastic Bottle", "bin":"recycle", "points":1 },
    { "image":"sweet.png", "alt":"Sweet Wrapper", "bin":"general", "points":1 }
];

// Variables
let score = 0;
let currentImagePos = -1;
let currentImage;
let currentImageNode = -1;
let gameOver = false;

/**
 * Converts the bin type to column number
 * @param {String} bin 
 * @returns int representing the column the bin is in
 */
function binToCol(bin) {
    switch (bin) {
        case "recycle":
            return 1;
        case "glass":
            return 2;
        case "general":
            return 0;
        default:
            break;
    };
}

/**
 *  Moves the rubbish down the screen
 */
function moveRubbish() {
    let top = parseInt(rubbish.style.top || '0');
    top += 10;
    rubbish.style.top = top + 'px';
}


/**
 * Moves the rubbish left by one column if able to
 */
function moveLeft() {
    // if (rubbish.classList.contains("left")) { do nothing }
    if (rubbish.classList.contains("center")) {
        rubbish.classList.remove("center");
        rubbish.classList.add("left");
    } else if (rubbish.classList.contains("right")) {
        rubbish.classList.remove("right");
        rubbish.classList.add("center");
    }
}

/**
 * Moves the rubbish right by one column if able to
 */
function moveRight() {
    // if (rubbish.classList.contains("right")) { do nothing }
    if (rubbish.classList.contains("center")) {
        rubbish.classList.remove("center");
        rubbish.classList.add("right");
    } else if (rubbish.classList.contains("left")) {
        rubbish.classList.remove("left");
        rubbish.classList.add("center");
    }
}

/**
 * Moves the rubbish back to starting position and creates next piece
 * @returns if the game is over
 */
function resetRubbish() {
    // Remove old rubbish piece
    if (currentImageNode != -1) {
        rubbish.removeChild(currentImageNode);
    }

    // Check for game win
    currentImagePos += 1
    if ((currentImagePos) >= items.length) {
        gameOver = true;
        return;
    }

    // Create new rubbish piece
    rubbish.style.top = '0px';
    currentImage = items[currentImagePos];

    let newImg = document.createElement('img');
    newImg.src = "../static/sustainable_app/img/" + currentImage["image"];
    newImg.alt = currentImage["alt"];
    newImg.classList.add("rubbish");
    currentImageNode = newImg;
    rubbish.appendChild(newImg);

    // Center piece
    if (rubbish.classList.contains("right")) {
        rubbish.classList.remove("right");
        rubbish.classList.add("center");
    } else if (rubbish.classList.contains("left")) {
        rubbish.classList.remove("left");
        rubbish.classList.add("center");
    }
    // else if (rubbish.classList.contains("center")) { do nothing }
}

/**
 * Check if rubbish has reached the bins
 */
function checkCollision() {
    let binNo = binToCol(currentImage["bin"]);
    let bin = bins[binNo];
    let rubbishRect = rubbish.getBoundingClientRect();
    let binRect = bin.getBoundingClientRect();

    // Check if in correct bin
    if (rubbishRect.bottom > (binRect.top-100) && ((binNo == 0 && rubbish.classList.contains("left"))||(binNo == 1 && rubbish.classList.contains("center"))||(binNo == 2 && rubbish.classList.contains("right")))) {
        score += currentImage["points"];
        resetRubbish();
    } else if (rubbishRect.bottom > (binRect.top-100)) {
        score = Math.max(score - currentImage["points"], 0);
        resetRubbish();
    }
}

// Listen for arrow keys (desktop)
document.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowLeft') {
        moveLeft();
    } else if (event.key === 'ArrowRight') {
        moveRight();
    }
})

// Listen for buttons (mobile)
touchLeft.addEventListener("click", function () {
    moveLeft();
});
touchRight.addEventListener("click", function () {
    moveRight();
});

/**
 * Gameloop
 */
function update() {
    if (!gameOver) {
        moveRubbish();
        checkCollision();
    }

    scoreLabel.textContent = "Score: " + score;

    if (gameOver) {
        clearInterval(gameLoop);
        menuButton.textContent = "Play Again";
        menuText.innerText = "Game Over\nScore: " + score + " out of 12";
        menuScreen.style.display = "flex";
        container.style.display = "none";
        buttonContainer.style.display = "none";

        add_score(score,"sorting");


        score = 0;
        currentImagePos = -1;
        currentImageNode = -1;
        gameOver = false;
    }
}

/**
 * Start the game
 */
function startGame() {
    // Start gameloop
    resetRubbish();
    gameLoop = setInterval(update, 50);
    menu.style.display = "none";
    menuScreen.style.display = "none";
    container.style.display = "flex";
    buttonContainer.style.display = "flex";
}

/**
 * Exit the game
 */
function exitGame() {
    window.location.replace("/home/");
}
