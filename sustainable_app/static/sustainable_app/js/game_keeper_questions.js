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
let tr;
// tr element with same id
for(let id in correct_answers) {
    tr = document.getElementById(id);
    tr.cells[correct_answers[id]].style.color = "#3f8d41";
}
