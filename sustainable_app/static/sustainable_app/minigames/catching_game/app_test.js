
// Define html elements
const container = document.getElementById("container");
const player = document.getElementById("player");

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

updateFrame();