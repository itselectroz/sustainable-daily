
// Movemnet with WASD

addEventListener("keydown", function(e) {
    if(e.code == "KeyD") {
       moveRight()
    }
    if(e.code == "KeyA") {
        moveLeft()
    }
})

addEventListener("keyup", function(e) {
    if(e.code == "KeyD") {
        stopRight()
    }
    if(e.code == "KeyA") {
       stopLeft();
    }
})

function moveRight() {
    vxr = container.offsetWidth / 128;
}

function moveLeft() {
    vxl = -(container.offsetWidth / 128);
}

function stopRight() {
    vxr = 0;
}

function stopLeft() {
    vxl = 0;
}