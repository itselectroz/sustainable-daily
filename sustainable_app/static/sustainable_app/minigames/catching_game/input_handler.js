
// Movemnet with WASD

addEventListener("keydown", function(e) {
    if(e.code == "KeyD") {
        console.log(getOffest(player))
        vxr = container.offsetWidth / 64;
    }
    if(e.code == "KeyA") {
        vxl = -(container.offsetWidth / 64);
    }
})

addEventListener("keyup", function(e) {
    if(e.code == "KeyD") {
        vxr = 0;
    }
    if(e.code == "KeyA") {
        vxl = 0;
    }
})

