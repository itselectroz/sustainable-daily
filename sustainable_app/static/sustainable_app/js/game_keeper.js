
// get html elements
const sideMenu = document.querySelector("aside");
const btnDash = document.getElementById("btn-dash");
const btnLoc = document.getElementById('btn-loc');

const selected_page = {"/game_keeper/": btnDash,
 "/game_keeper_locations/": btnLoc};



function updateActive() {
    let url = window.location.pathname;
    selected_page[url].classList.add("active");
}

updateActive();