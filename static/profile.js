

function replaceAvatar(results) {
    $("#avatar").attr("src",results);
}

function showAvatar(evt) {
    $.get('/profile-change-avatar', replaceAvatar);
}

$('#get-avatar-btn').on('click', showAvatar);
