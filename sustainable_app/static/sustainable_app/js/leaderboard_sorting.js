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
 * Gets the order from the dictionary
 */
function createTable(dictionary) {

    
    //Getting table element from html
    let table = document.getElementById("leaderboard-table");
    

    dictionary = JSON.parse(dictionary);

    

    //For every user in the leaderboard creating new row in table with their name, xp and level
    for (user in dictionary) {
        
        //Create new row for user
        let newRow = table.insertRow();

        //Creates new cells for user
        var cell1 = newRow.insertCell();
        var cell2 = newRow.insertCell();
        var cell3 = newRow.insertCell();

        //Adds relevent information to cells 
        cell1.innerHTML = dictionary[user]["username"];
        cell2.innerHTML = dictionary[user]["level"];
        cell3.innerHTML = dictionary[user]["points"];

        //Gives new row an id of "generated" so if the leaderboard is re-ordered it will delete the old rows
        newRow.setAttribute("id", "generated");
    }
}
        
/**
 * Delete all rows in table apart from top and creates new table using dictionary parameter
 */
function orderTable(dictionary) {
    delete_table();

    createTable(dictionary);
}
    

  

    
    



