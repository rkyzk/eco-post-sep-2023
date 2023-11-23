/*
 post like & unlike
*/
document.addEventListener("DOMContentLoaded", function () {
    let likeBtns = document.getElementsByClassName('like-btn');
    for (likeBtn of likeBtns) {
        likeBtn.addEventListener("click", function () {
            let csrftoken = getCookie('csrftoken');
            let url = 'post_like/';
            let likesCount = parseInt(likeBtn.nextElementSibling.textContent);
            let like = likeBtn.lastElementChild.classList.contains('fa-regular');
            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function (response) {
                    // いいねがクリックされたらハートを塗りつぶして数に１追加
                    if (like) {
                        likeBtn.innerHTML = '<i class="fa-solid fa-heart heart"></i>';
                        likeBtn.nextElementSibling.textContent = likesCount + 1;
                    } else {
                        // いいね解除。ハートを輪郭だけにして、数を１減らす。
                        likeBtn.innerHTML = '<i class="fa-regular fa-heart heart"></i>';
                        likeBtn.nextElementSibling.textContent = likesCount - 1;
                    }
                },
                error: function (response) {
                    likeBtn.parentElement.nextElementSibling.textContent = "エラー発生。もう一度お試しください。";
                    likeBtn.parentElement.nextElementSibling.classList.remove("hide");
                    likeBtn.parentElement.nextElementSibling.classList.add("show");
                    setTimeout(() => {
                        likeBtn.parentElement.nextElementSibling.classList.remove("show");
                        likeBtn.parentElement.nextElementSibling.classList.add("hide");
                    }, 3000);
                }
            })
        });
    }
});