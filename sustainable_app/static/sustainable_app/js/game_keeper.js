
const addUser = document.getElementById('add');

addUser.addEventListener("click", () => {
    window.location.replace('/register');
});

$(document).ready(function() {

    // Request for character
    $('.remove-keeper').on('click', function() {

        $username = this.getAttribute('value');

        $.ajax({
            type: "POST",
            url: "remove_keeper/",
            data: {
                username: $username,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});