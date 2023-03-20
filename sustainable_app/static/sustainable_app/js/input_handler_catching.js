
// Movemnet with WASD

/**
 * Listen for relevant keydown events
 */
addEventListener("keydown", function(e) {
    if(e.code == "KeyD") {
       moveRight();
    }
    if(e.code == "KeyA") {
        moveLeft();
    }
})

/**
 * Listen for relevant keyup events
 */
addEventListener("keyup", function(e) {
    if(e.code == "KeyD") {
        stopRight();
    }
    if(e.code == "KeyA") {
       stopLeft();
    }
})

/**
 * Set the players right velocity
 */
function moveRight() {
    vxr = container.offsetWidth / 128;
}

/**
 * Set the players left velocity
 */
function moveLeft() {
    vxl = -(container.offsetWidth / 128);
}

/**
 * Remove the players right velocity
 */
function stopRight() {
    vxr = 0;
}

/**
 * Remove the players left velocity
 */
function stopLeft() {
    vxl = 0;
}