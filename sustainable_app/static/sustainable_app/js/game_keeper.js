
// get html elements
const sideMenu = document.querySelector("aside");
const btnDash = document.getElementById("btn-dash");
const btnLoc = document.getElementById('btn-loc');
const btnSur = document.getElementById('btn-sur');
const btnEve = document.getElementById('btn-eve');


const selected_page = {"/game_keeper/": btnDash,
 "/game_keeper_locations/": btnLoc,
"/game_keeper_surveys/": btnSur,
"/game_keeper_events/": btnEve};



function updateActive() {
    let url = window.location.pathname;
    selected_page[url].classList.add("active");
}


updateActive();