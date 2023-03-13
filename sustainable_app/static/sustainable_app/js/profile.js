


// Setting unlockables to be locked if necessary
for(let level in character_array) {
    if(parseInt(level) > user_level) {
        // console.log("Level: " + level + " User: " + user_level)
        character_array[level].style.backgroundImage = "url(/static/sustainable_app/img/xp_symbol.png)";
        character_array[level].firstElementChild.innerText = (level).toString();
        character_array[level].setAttribute("level", level);
    }
}


// Ajax requests to change items

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
        

    // Request for accessory
    $('#accessory input').on('change', function() {

        $accessory = $('input[name="accessory_select"]:checked').val();

        $.ajax({
            type: "POST",
            url: "equip/",
            data: {
                type: "accessory",
                name: $accessory,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });

    // Request for name color
    $('#name_color input').on('change', function() {

        $name_color = $('input[name="name_color_select"]:checked').val();

        $.ajax({
            type: "POST",
            url: "equip/",
            data: {
                type: "username_color",
                name: $name_color,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });

    // Request for background color
    $('#background_color input').on('change', function() {

        $background_color = $('input[name="background_select"]:checked').val();

        $.ajax({
            type: "POST",
            url: "equip/",
            data: {
                type: "background_color",
                name: $background_color,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});