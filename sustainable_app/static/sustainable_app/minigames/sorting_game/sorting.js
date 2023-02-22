// HTML elements
const container = document.getElementById("container")
const rubbish = document.getElementById("spawn")
const scoreLabel = document.getElementById("score")
const bins = document.querySelectorAll(".bin")

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
]

// Variables
let score = 0
let currentImagePos = -1
let currentImage
let currentImageNode = -1
let gameOver = false

function binToCol(bin) {
    switch (bin) {
        case "recycle":
            return 1
        case "glass":
            return 2
        case "general":
            return 0
        default:
            break;
    }
}

function moveRubbish() {
    let top = parseInt(rubbish.style.top || '0')
    top += 5;
    rubbish.style.top = top + 'px'
}

function moveLeft() {
    if (rubbish.classList.contains("left")) {
        return
    } else if (rubbish.classList.contains("center")) {
        rubbish.classList.remove("center")
        rubbish.classList.add("left")
        return
    } else if (rubbish.classList.contains("right")) {
        rubbish.classList.remove("right")
        rubbish.classList.add("center")
        return
    } else {
        return
    }
}

function moveRight() {
    if (rubbish.classList.contains("right")) {
        return
    } else if (rubbish.classList.contains("center")) {
        rubbish.classList.remove("center")
        rubbish.classList.add("right")
        return
    } else if (rubbish.classList.contains("left")) {
        rubbish.classList.remove("left")
        rubbish.classList.add("center")
        return
    } else {
        return
    }
}

function resetRubbish() {
    if (currentImageNode != -1) {
        rubbish.removeChild(currentImageNode)
    }
    currentImagePos += 1
    if ((currentImagePos) >= items.length) {
        gameOver = true
        return
    }
    rubbish.style.top = 0 + 'px'
    currentImage = items[currentImagePos]
    let newImg = document.createElement('img')
    newImg.src = "img/" + currentImage["image"]
    newImg.alt = currentImage["alt"]
    currentImageNode = newImg
    rubbish.appendChild(newImg)
}

function checkCollision() {
    let binNo = binToCol(currentImage["bin"])
    let bin = bins[binNo]
    let rubbishRect = rubbish.getBoundingClientRect()
    let binRect = bin.getBoundingClientRect()

    if (rubbishRect.bottom > binRect.top && ((binNo == 0 && rubbish.classList.contains("left"))||(binNo == 1 && rubbish.classList.contains("center"))||(binNo == 2 && rubbish.classList.contains("right")))) {
        score += currentImage["points"]
        resetRubbish()
        return
    } else if (rubbishRect.bottom > binRect.top) {
        score = Math.max(score - currentImage["points"], 0)
        resetRubbish()
        return
    }
}

document.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowLeft') {
        moveLeft()
    } else if (event.key === 'ArrowRight') {
        moveRight()
    }
})

function update() {
    if (!gameOver) {
        moveRubbish()
        checkCollision()
    }

    scoreLabel.textContent = "Score: " + score

    if (gameOver) {
        clearInterval(gameLoop)
        alert("Game Over!\nYou scored " + score + " out of 12!\nHappy Sorting!")
    }
}

resetRubbish()
const gameLoop = setInterval(update, 50)