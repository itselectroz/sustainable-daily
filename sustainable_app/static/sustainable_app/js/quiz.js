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
const button = document.querySelector(".confirm-button")
const results = document.querySelector(".results")
const resultText = document.querySelector(".result-text")
const questionContainer = document.querySelector(".question-container")
const nextButton = document.querySelector(".next-button")

// Set defaults
menuText.innerText = "The Ultimate Sustainability Quiz"

// Set variables
let score = 0
let questionNum = -1
let correctAns = null

/**
 * Check if answer was correct
 */
function checkAns() {
    if (ans1.checked) {
        if (correctAns == 1) {
            correctAnswer(label1.textContent)
        } else {
            wrongAnswer(getCorrectAnswer())
        }
    } else if (ans2.checked) {
        if (correctAns == 2) {
            correctAnswer(label2.textContent)
        } else {
            wrongAnswer(getCorrectAnswer())
        }
    } else if (ans3.checked) {
        if (correctAns == 3) {
            correctAnswer(label3.textContent)
        } else {
            wrongAnswer(getCorrectAnswer())
        }
    } else if (ans4.checked) {
        if (correctAns == 4) {
            correctAnswer(label4.textContent)
        } else {
            wrongAnswer(getCorrectAnswer())
        }
    }
}

/**
 * Gets the string representation of the correct answer
 * @returns the correct answer
 */
function getCorrectAnswer() {
    switch (correctAns) {
        case 1:
            return label1.textContent
        case 2:
            return label2.textContent
        case 3:
            return label3.textContent
        case 4:
            return label4.textContent
        default:
            return null
    }
}

/**
 * Handle when the player gets a question right
 * @param {String} answer 
 */
function correctAnswer(answer) {
    resultText.style.color = "green"
    resultText.textContent = "Correct! The answer is in fact " + answer + "!"
    score += 1
    questionContainer.style.display = "none"
    results.style.display = "flex"
}

function wrongAnswer(correctAnswer) {
    resultText.style.color = "red"
    resultText.textContent = "Incorrect - the corret answer is actually " + correctAnswer + "!"
    questionContainer.style.display = "none"
    results.style.display = "flex"
}

/**
 * Display new question
 */
function createNewQuestion() {
    questionNum += 1
    console.log(questionNum)
    let newQuestion = questions[questionNum].fields
    question.textContent = newQuestion.question
    label1.textContent = newQuestion.a1
    label2.textContent = newQuestion.a2
    label3.textContent = newQuestion.a3
    label4.textContent = newQuestion.a4
    correctAns = newQuestion.correct_answer

    // Change button text
    if (questionNum >= questions.length-1) {
        nextButton.textContent = "End Quiz"
    }
}

/**
 * Start quiz
 */
function startGame() {
    menuScreen.style.display = "none"
    container.style.display = "flex"
    questionContainer.style.display = "flex"
    results.style.display = "none"
    createNewQuestion()
}

/**
 * End quiz
 */
function endGame() {
    menuScreen.style.display = "flex"
    container.style.display = "none"
    menuButton.textContent = "Play Again"
    menuText.innerText = "Quiz Finished!\nScore: " + score + " out of " + questions.length
    score = 0
    questionNum = -1
}

/**
 * Exit the game
 */
function exitGame() {
    window.location.replace("/home");
}

/**
 * Sets up for next question
 */
function nextQuestion() {
    // Check if on final question
    if (questionNum >= questions.length-1) {
        endGame()
        return
    }

    createNewQuestion()
    questionContainer.style.display = "flex"
    results.style.display = "none"

    // Clear radio buttons
    ans1.checked = "false"
    ans2.checked = "false"
    ans3.checked = "false"
    ans4.checked = "false"
}
