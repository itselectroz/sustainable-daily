//The current order of the leaderboard/the last way the table was ordered
let lastAction = ""

/**
 * Deletes all generated rows in a table
 */
function delete_table() {
    let elementsToDelete = document.querySelectorAll('[id="generated"');

    elementsToDelete.forEach(function(element){
        element.remove();
    })
}

/**
 * Creates a table with username, points and level field
 * Gets the order from the dictionary (actually an array of dictionary)
 */
function createTable(dictionary) {

    //Getting table element from html
    let table = document.getElementById("leaderboard-table");
    

    let topRow = table.insertRow();

    let topCell1 = topRow.insertCell();
    let topCell2 = topRow.insertCell();
    let topCell3 = topRow.insertCell();
    let topCell4 = topRow.insertCell();

    topCell1.innerHTML = "User";
    topCell2.innerHTML = "";
    topCell3.innerHTML = "Level";
    topCell4.innerHTML = "Points";

    topRow.setAttribute("id", "generated");

    //For every user in the leaderboard creating new row in table with their name, xp and level
    for (let i = 0; i < Math.min(Object.keys(dictionary).length, 5); i++) {
        let user = Object.keys(dictionary)[i];

        //Create new row for user
        let newRow = table.insertRow();

        //Creates new cells for user
        let cell1 = newRow.insertCell();
        let cell2 = newRow.insertCell();
        let cell3 = newRow.insertCell();
        let cell4 = newRow.insertCell();

        //Profile picture
        let accessory = dictionary[user]["accessory"];
        let character = dictionary[user]["character"];
        let background_color = dictionary[user]["background_color"];

        //Username
        let username = dictionary[user]["username"];
        let username_color = dictionary[user]["username_color"];

        //Position
        let position = dictionary[user]["position"];

        //Adds relevent information to cells
        cell1.innerHTML =`
        <div class="cell1_container">
        <div class="user_position">${position}&nbsp;</div>
        <div class="pfp_container">
            <div class="pfp" id="pfp" style="background-color:${background_color}">
                <img class="pfp_image" id="pfp_image" src="../static/sustainable_app/img/${character}${accessory}.png">
            </div>
        </div>
        </div>
        `;
        cell2.innerHTML = `<p style="color:${username_color}">${username}</p>`;
        cell3.innerHTML = dictionary[user]["level"];
        cell4.innerHTML = dictionary[user]["points"];

        //Gives new row an id of "generated" so if the leaderboard is re-ordered it will delete the old rows
        newRow.setAttribute("id", "generated");
    }
}


        
/**
 * Delete all rows in table apart from top and creates new table using dictionary parameter
 */
function orderTable(dictionary, changeToState, currentUser) {

    dictionary = JSON.parse(dictionary);

    for (let i = 0; i < dictionary.length; i++) {
        dictionary[i].position = i + 1;
    }

    //If the user is clicks the button to order the leaderboard the same way it is currently ordered, gets the user's stats and the stats of those ranked around them
    if (changeToState == lastAction) {
        //Sets lastaction to "" so leaderboard will be ordered normally if same button clicked
        lastAction = "";

        //Blank array that will hold reverse of dictionary
        let newDictionary = [];

        //Finds index of current user
        for (let i = 0; i < dictionary.length; i++) {
            if (dictionary[i].id.toString() === currentUser) {
                userIndex = i;
                break;
              }
        }

        //Finds users ranked 2 above and 2 below the current user
        for (let i = userIndex - 2; i < userIndex + 3; i++) {
            if (i >= 0 && i < dictionary.length) {
                newDictionary.push(dictionary[i]);
            }
        }

        //Sets dictionary to newDictionary
        dictionary = newDictionary
    } else {
        lastAction = changeToState
    }

    //Clearing leaderboard
    delete_table();

    //Creating new table
    createTable(dictionary);
}
    

  

    
    



