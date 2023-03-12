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

    var topCell1 = topRow.insertCell();
    var topCell2 = topRow.insertCell();
    var topCell3 = topRow.insertCell();
    var topCell4 = topRow.insertCell();

    topCell1.innerHTML = "User";
    topCell2.innerHTML = "";
    topCell3.innerHTML = "Level";
    topCell4.innerHTML = "Points";

    topRow.setAttribute("id", "generated");

    //For every user in the leaderboard creating new row in table with their name, xp and level
    for (user in dictionary) {
        
        //Create new row for user
        let newRow = table.insertRow();

        //Creates new cells for user
        var cell1 = newRow.insertCell();
        var cell2 = newRow.insertCell();
        var cell3 = newRow.insertCell();
        var cell4 = newRow.insertCell();

        //Profile picture
        let accessory = dictionary[user]["accessory"];
        let character = dictionary[user]["character"];
        let background_color = dictionary[user]["background_color"];

        //Username
        let username = dictionary[user]["username"];
        let username_color = dictionary[user]["username_color"];

        //Adds relevent information to cells 
        cell1.innerHTML = `
        <div class="pfp_container">
            <div class="pfp" id="pfp" style="background-color:${background_color}">
                <img class="pfp_image" id="pfp_image" src="../static/sustainable_app/img/${character}${accessory}.png">
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
function orderTable(dictionary, changeToState) {

    dictionary = JSON.parse(dictionary);

    //If the user is clicks the button to order the leaderboard the same way it is currently ordered, reverses the leaderboard so lowest values at top
    if (changeToState == lastAction) {
        //Sets lastaction to "" so leaderboard will be ordered normally if same button clicked
        lastAction = "";

        //Blank array that will hold reverse of dictionary
        newDictionary = [];
        
        lastIndex = dictionary.length - 1;

        //Reverses dictionary
        for (user in dictionary) {
            newDictionary.push(dictionary[lastIndex - user]);

        }

        //Will create table using new revered dictionary
        dictionary = newDictionary
    } else {
        lastAction = changeToState
    }

    //Clearing leaderboard
    delete_table();

    //Creating new table
    createTable(dictionary);
}
    

  

    
    



