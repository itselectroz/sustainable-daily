$(document).ready(function() {

    // Request to add location
    $('.remove-location').on('click', function() {

        $location_id = this.getAttribute('value');

        $.ajax({
            type: "POST",
            url: "/game_keeper/locations_remove/",
            data: {
                location_id: $location_id,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});


const expanded_view = document.querySelector('.expanded-view');
const image_view = document.getElementById('expanded-image');

function expand(src) {
    image_view.src = src;
    expanded_view.style.visibility = 'visible';
}

function close_expanded() {
    expanded_view.style.visibility = 'hidden';
}