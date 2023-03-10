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

// Set variables
let score = 0
let questionNum = -1

let questions = {"question":"test", "a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4"}

/**
 * Display new question
 */
function createNewQuestion() {
    questionNum += 1
    let newQuestion = questions[questionNum]
    question.textContent = newQuestion["question"]
    label1.textContent = newQuestion["a1"]
    label2.textContent = newQuestion["a2"]
    label3.textContent = newQuestion["a3"]
    label4.textContent = newQuestion["a4"]
}

/**
 * Start quiz
 */
function startGame() {
    menuScreen.style.display = "none"
    container.style.display = "flex"
    createNewQuestion()
}

/**
 * Exit the game
 */
function exitGame() {
    window.location.replace("/home");
}
