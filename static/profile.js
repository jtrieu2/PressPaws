
// function replaceAvatar(results) {
//     $("#avatar").attr("src",results);
// }
// function showAvatar(evt) {
//     $.get('/profile-change-avatar', replaceAvatar);
// }
// $('#get-avatar-btn').on('click', showAvatar);

// add bookmark button - capture the name of the shelter 
// send to the server as a form and then have a post button at the end of the form so that when they click on that it will be sent to the server
// function that catches the post will store in database
// separate function will take from back end and put in here
// webscraping  -- 

function displayWord(evt) {
	evt.preventDefault();

	let inputdata = {'message':'hello'}

	    $.post("/grab-data-from-frontend", inputdata, function(){})

}
$("#get-avatar-btn").on('click', displayWord);