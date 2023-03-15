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
