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
const download_image = document.getElementById('download-image');

function expand(src, location_id, type) {
    image_view.src = src;
    expanded_view.style.visibility = 'visible';

    if(type == 'qr') {
        download_image.setAttribute("href", ("/game_keeper/open/" + location_id + "/"));
        download_image.style.visibility = 'visible';
    }
    else {
        download_image.style.visibility = 'hidden';
    }
}

function close_expanded() {
    expanded_view.style.visibility = 'hidden';
}