$(document).ready(function () {
    // Confirm before deleting the post
    const DELETE_POST = "Are you sure you want to delete your post?  You won't be able to retrieve the draft."
    $('#delete-post').submit(function (e) {
        return confirm(DELETE_POST);
    });

    // Confirm before deleting comment
    const DELETE_COMMENT = "Are you sure you want to delete your comment?"
    $('#delete-comment').submit(function () {
        return confirm(DELETE_COMMENT);
    })
});