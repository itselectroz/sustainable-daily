$(document).ready(function() {

    // Request to add location
    $('.remove-question').on('click', function() {

        $question_id = this.getAttribute('value');

        $.ajax({
            type: "POST",
            url: "/game_keeper/questions_remove/",
            data: {
                question_id: $question_id,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});

// make correct answer appear green
