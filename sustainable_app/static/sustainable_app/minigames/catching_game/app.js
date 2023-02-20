let game_container = document.querySelector(".game-container");
let bin = document.querySelector(".bin");
let rubbish_group = document.querySelector(".rubbish_group");
let binLeft = parseInt(window.getComputedStyle(bin).getPropertyValue("left"));
let binBottom = parseInt(window.getComputedStyle(bin).getPropertyValue("bottom"));
let score = 0;

function moveBinLeft() {
    if(binLeft > 0) {
        binLeft -= 15;
        bin.style.left = binLeft + 'px';
    }
}

function moveBinRight() {
    if(binLeft < 620) {
        binLeft += 15;
        bin.style.left = binLeft + 'px';
    }
}

function control(e) {
    if(e.key == "ArrowLeft") {
        moveBinLeft();
    }

    if(e.key == "ArrowRight") {
        moveBinRight();
    }
}

function generateRubbish() {
    let rubbishBottom = 470;
    let rubbishLeft = Math.floor(Math.random() * 620);
    let rubbish = document.createElement('div');
    rubbish.setAttribute("class", "rubbish");
    rubbish_group.appendChild(rubbish);

    function fallDown() {
        if(rubbishBottom < binBottom + 50 && rubbishBottom > binBottom && rubbishLeft > binLeft - 30 && rubbishLeft < binLeft + 80) {
            rubbish_group.removeChild(rubbish);
            clearInterval(fallInterval);
            score++;
        }
        if(rubbishBottom < binBottom) {
            alert("Game Over! Score: " + score);
            clearInterval(fallInterval);
            clearTimeout(rubbishTimeout);
            location.reload();
        }
        rubbishBottom -= 10;
        rubbish.style.bottom = rubbishBottom + 'px';
    }

    let fallInterval = setInterval(fallDown, 20);
    let rubbishTimeout = setTimeout(generateRubbish, 2000);
    rubbish.style.bottom = rubbishBottom + 'px';
    rubbish.style.left = rubbishLeft + 'px';

}

generateRubbish();

document.addEventListener("keydown", control);