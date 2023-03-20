
/**
 * Set all non-owned items to locked
 */
function setupUnlockables() {
    // Setting unlockables to be locked if necessary
    for(let level in character_array) {
        if(parseInt(level) > user_level) {
            // console.log("Level: " + level + " User: " + user_level)
            character_array[level].style.backgroundImage = "url(/static/sustainable_app/img/xp_symbol.png)";
            character_array[level].firstElementChild.innerText = (level).toString();
            character_array[level].setAttribute("level", level);
        }
    }
}

// pop up for buying with points
popup_menu = document.querySelector(".purchase-pop-up");
popup_text_start = document.querySelector(".question").childNodes[0];
popup_text_end = document.querySelector(".question").childNodes[2];
item_cost = document.querySelector(".item_cost");
item_img = document.querySelector(".item_to_buy");
item_container = document.querySelector(".item_to_buy_container");

/**
 * Set click events for all non-owned items
 */
function setupPurchasables() {
    let temp;
    for(let item in item_array) {
        document.getElementById(item).addEventListener("click", (e) => {
            // pass in points and image
            popup(item_array[item], "/static/sustainable_app/img/" + item.toString() + ".png", e.target.parentNode.id);
        })

        document.querySelector('[for=' + item + ']').style.backgroundImage = "url(/static/sustainable_app/img/locked.png)";
    }
}

/**
 * Set click events for all owned items
 */
function setEquipables() {
    for(let item in owned_array) {
        document.getElementById(item).addEventListener("click", () => {
            equipItem(owned_array[item]);
        })
    }
}

/**
 * Pops up a confirmation menu to buy an item
 * @param {Number} points 
 * @param {URL} img_url 
 */
function popup(points, img_url, type) {
    popup_menu.style.visibility = "visible";
    popup_text_start.textContent = "Purchase this item for ";
    popup_text_end.textContent = " points?";
    item_cost.innerText = (" " + points.toString() + " ");


    if(type=="accessory") {
        item_container.style.visibility = "visible";
        item_container.style.height = 'fit-content';
        item_img.src = img_url;
    }
    else {
        item_container.style.visibility = "hidden";
        item_container.style.height = '0px';
    }


    if(user_points >= points) {
        document.querySelector(".buy").addEventListener("click", () => {
            // purchase the item
            purchaseItem(type);
            popdown();
        })
    }
    else {
        document.querySelector(".buy").addEventListener("click", () => {
            // not enough points
            popup_text_start.textContent = "You need ";
            popup_text_end.textContent = " more points!";
            item_cost.innerText = (" " + (points - user_points) + " ");
        })
    }
}

/**
 * Collapses the confirmation menu
 */
function popdown() {
    popup_menu.style.visibility = "hidden";
    item_container.style.visibility = "hidden";
}

/**
 * Sends ajax request to equip an item
 */
function equipItem(type) {

    $item = $('input[name="' + type + '_select"]:checked').val();

    $.ajax({
        type: "POST",
        url: "equip/",
        data: {
            type: type,
            name: $item,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function() {
            window.location.reload();
        }
    });
}

/**
 * Sends ajax request to purchase an item
 */
function purchaseItem(type) {

    $item = $('input[name="' + type + '_select"]:checked').val();

    $.ajax({
        type: "POST",
        url: "purchase/",
        data: {
            type: type,
            name: $item,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function() {
            window.location.reload();
        }
    });
}


// Ajax requests to change characters
$(document).ready(function() {

    // Request for character
    $('#character input').on('change', function() {

        $character_clicked = $('input[name="character_select"]:checked').attr("id");
        $level_needed = $('label[for=' + $character_clicked.toString() + ']').attr('level');

        if(user_level < $level_needed) {
            alert("Not high enough level");
        }
        else {
            $character = $('input[name="character_select"]:checked').val();
            $.ajax({
                type: "POST",
                url: "equip/",
                data: {
                    type: "character",
                    name: $character,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                },
                success: function() {
                    window.location.reload();
                }
            });
        }

        
    });
});

// Complete the setup
setupPurchasables();
setupUnlockables();
setEquipables();