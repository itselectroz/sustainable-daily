
// Define html elements
const container = document.getElementById("container");
const player = document.getElementById("player");
const rubbish_group = document.querySelector(".rubbish_group");
const playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
const playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));

let score = 0;

// Define X value
let x = 0;
let vxl = 0;
let vxr = 0;

/**
 * Update the rendered objects
 */
function updateFrame() {

    // Update X position based on velocity
    if(getOffest(player) < (container.offsetWidth - player.offsetWidth)) {
        x += vxr;
    }

    if(getOffest(player) > 0) {
        x += vxl;
    }

    // Move player
    
    player.style.left = x + 'px';
    
    requestAnimationFrame(updateFrame);
}

function getOffest(el) {
    const rect = el.getBoundingClientRect();
    return rect.left + window.scrollX;
}

function generateRubbish() {
    let rubbish = document.createElement('div');
    let rubbishBottom = container.offsetHeight;
    let type = getRandomClass();
    rubbish.setAttribute("class", "rubbish " + type);
    let rubbishLeft = Math.floor(Math.random() * (container.offsetWidth - rubbish.offsetWidth));
    console.log("Container: " + container.offsetWidth);
    console.log("Rubbish: " + rubbish.offsetWidth);
    console.log(container.offsetWidth - rubbish.offsetWidth);
    rubbish.style.backgroundImage = 'url(img/' + type + '.png)';
    rubbish_group.appendChild(rubbish);

    function fallDown() {

        if(rubbishBottom > playerBottom && rubbishBottom < (playerBottom + (player.offsetHeight / 2)) && rubbishLeft > (player.offsetLeft - (player.offsetWidth / 2)) && 
        rubbishLeft < (player.offsetLeft + (player.offsetWidth / 2))) {
            rubbish_group.removeChild(rubbish);
            clearInterval(fallInterval);
            score ++;
        }
        if(rubbishBottom < playerBottom) {
            alert("Game Over! Score:" + score);
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

function getRandomClass() {
    let chosen = Math.floor(Math.random() * 10);
    let arr_rubbish = ["can", "banana", "crisps", "glass_bottle", "jelly", "milk", "paper", "plastic_bag", "plastic_bottle", "sweet"];
    
    return arr_rubbish[chosen];
}

generateRubbish();
updateFrame();