$(document).ready(function() {
    $('#name_color input').on('change', function() {

        $name_color = $('input[name="name_color_select"]:checked').val();

        $.ajax({
            type: "POST",
            url: "equip/",
            data: {
                username_color: $name_color,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                alert("Equipped");
                window.location.reload();
            }
        });
    });
});