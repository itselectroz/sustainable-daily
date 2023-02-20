
// Define html elements
const container = document.getElementById("container");
const player = document.getElementById("player");
const rubbish_group = document.querySelector(".rubbish_group");
const playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue("left"));
const playerBottom = parseInt(window.getComputedStyle(player).getPropertyValue("bottom"));

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
    let rubbishBottom = container.offsetHeight;
    let rubbishLeft = Math.floor(Math.random() * container.offsetWidth);
    let rubbish = document.createElement('div');
    rubbish.setAttribute("class", "rubbish");
    rubbish_group.appendChild(rubbish);

    function fallDown() {

        if(rubbishBottom == playerBottom && rubbishLeft > playerLeft && rubbishLeft < playerLeft + player.offsetWidth) {
            rubbish_group.removeChild(rubbish);
            clearInterval(fallInterval);
        }
        if(rubbishBottom < playerBottom) {
            alert("Game Over! Score:");
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
updateFrame();