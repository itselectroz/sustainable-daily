const Surveys = [
{
    surveyTitle: "Best Building",
    surveyDesc: "What is the best building on campus?",
    surveOptions: "Henderson, Forum, Amory, Northcott Theatre",
},
{
    surveyTitle: "Best Building",
    surveyDesc: "What is the best building on campus?",
    surveOptions: "Henderson, Forum, Amory, Northcott Theatre",
},
{
    surveyTitle: "Best Building",
    surveyDesc: "What is the best building on campus?",
    surveOptions: "Henderson, Forum, Amory, Northcott Theatre",
},

]

// fill in locations table
Surveys.forEach(survey => {
    const tr = document.createElement("tr");
    const trContent = `
        <td>${survey.surveyTitle}</td>
        <td>${survey.surveyDesc}</td>
        <td>${survey.surveOptions}</td>
        <td><a href="#"><span class="material-symbols-sharp">cancel</span></a></td>
    `

    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
});
