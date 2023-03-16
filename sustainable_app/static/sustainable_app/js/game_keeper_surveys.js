$(document).ready(function() {

    // Request to add location
    $('.remove-survey').on('click', function() {

        $survey_id = this.getAttribute('value');

        $.ajax({
            type: "POST",
            url: "/game_keeper/surveys_remove/",
            data: {
                survey_id: $survey_id,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function() {
                window.location.reload();
            }
        });
    });
});

// get survey select box
const select = document.querySelector(".survey_select");

// wiping the survey select box
$(".survey_select").empty();

// populating survey select box
let newOption;
for(let id in survey_options) {
    newOption = new Option(survey_options[id], id);
    select.add(newOption, undefined);
}
