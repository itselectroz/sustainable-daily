$(document).ready(function() {

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
                alert("Equipped");
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
                alert("Equipped");
                window.location.reload();
            }
        });
    });
});