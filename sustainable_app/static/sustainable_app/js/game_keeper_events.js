const Events = [
{
    eventTitle: "Computer Science Quiz",
    eventDateTime: "10/25/2006 14:30:59",
    eventLocation: "Alumni Lecture Theatre",
    eventOrganiser: "Matt Collinson",
},
{
    eventTitle: "Computer Science Quiz",
    eventDateTime: "10/25/2006 14:30:59",
    eventLocation: "Alumni Lecture Theatre",
    eventOrganiser: "Matt Collinson",
},
{
    eventTitle: "Computer Science Quiz",
    eventDateTime: "10/25/2006 14:30:59",
    eventLocation: "Alumni Lecture Theatre",
    eventOrganiser: "Matt Collinson",
},

]

// fill in locations table
Events.forEach(event => {
    const tr = document.createElement("tr");
    const trContent = `
        <td>${event.eventTitle}</td>
        <td>${event.eventDateTime}</td>
        <td>${event.eventLocation}</td>
        <td>${event.eventOrganiser}</td>
        <td><a href="#"><span class="material-symbols-sharp">cancel</span></a></td>
    `

    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
});
