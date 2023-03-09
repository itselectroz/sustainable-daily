// HTML elements
const container = document.getElementById("container")
const question = document.getElementById("question")
const ans1 = document.getElementById("answer1")
const ans2 = document.getElementById("answer2")
const ans3 = document.getElementById("answer3")
const ans4 = document.getElementById("answer4")
const label1 = document.querySelector('label[for="answer1"]')
const label2 = document.querySelector('label[for="answer2"]')
const label3 = document.querySelector('label[for="answer3"]')
const label4 = document.querySelector('label[for="answer4"]')
const menuScreen = document.getElementById("menu")
const menuText = document.getElementById("menuText")
const menuButton = document.getElementById("btnMenu")

menuText.innerText = "The Ultimate Sustainability Quiz"

/**
 * Start quiz
 */
function startGame() {
    menuScreen.style.display = "none"
    container.style.display = "flex"
}

/**
 * Exit the game
 */
function exitGame() {
    window.location.replace("/home");
}
