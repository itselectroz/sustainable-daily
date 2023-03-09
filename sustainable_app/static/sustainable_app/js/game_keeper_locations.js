// $(document).ready(function() {

//     // Request to add location
//     $('.create-button').on('click', function() {

//         $username = this.getAttribute('value');

//         $.ajax({
//             type: "POST",
//             url: "locations_add/",
//             data: {
//                 username: $username,
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             },
//             success: function() {
//                 window.location.reload();
//             }
//         });
//     });
// });

// const Locations = [
// {
//     locationName: "Recycle Harrison",
//     locationType: "Recycle Bin",
//     locationClue: "Near a car park",
//     locationImage: "Link to image",
// },
// {
//     locationName: "Water Henderson",
//     locationType: "Water Fountain",
//     locationClue: "In a cafe",
//     locationImage: "Link to image",
// },
// {
//     locationName: "Recycle Forum",
//     locationType: "Recycle Bin",
//     locationClue: "Up some stairs",
//     locationImage: "Link to image",
// },

// ]

// // fill in locations table
// Locations.forEach(location => {
//     const tr = document.createElement("tr");
//     const trContent = `
//         <td>${location.locationName}</td>
//         <td>${location.locationType}</td>
//         <td>${location.locationClue}</td>
//         <td>${location.locationImage}</td>
//         <td><a href="#"><span class="material-symbols-sharp">cancel</span></a></td>
//     `

//     tr.innerHTML = trContent;
//     document.querySelector('table tbody').appendChild(tr);
// });


