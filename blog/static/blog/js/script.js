/*--- 

バーガーメニューを表示・非表示にするためのプログラム

----*/
let open;
const menu = document.querySelector("#nav-menu");

/*-- メニューを閉じる --*/
const closeMenu = () => {
    setTimeout(function () {
        menu.style.display = "none";
        open = false;
        document.removeEventListener('mouseup', closeMenu)
    }, 100);
}

/*-- メニューを開く --*/
const openMenu = () => {
    if (open) {
        menu.style.display = "none";
        open = false;
    } else {
        menu.style.display = "block";
        open = true;
        document.addEventListener('mouseup', closeMenu)
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // マイページで「全て表示」ボタンでブログを表示
    let button = document.getElementsByClassName('show-posts');
    for (btn of button) {
        btn.addEventListener("click", function () {
            let posts = this.nextElementSibling;
            if (this.classList.contains('show')) {
                this.classList.remove('show');
                this.classList.add('hide');
                posts.classList.remove('hide');
                posts.classList.add('show');
            }
        });
    }

    // マイページ「折りたたむ」ボタンでブログを隠す
    let hideButton = document.getElementsByClassName('hide-posts');
    for (hideBtn of hideButton) {
        hideBtn.addEventListener("click", function () {
            let posts = this.parentElement;
            posts.classList.remove('show');
            posts.classList.add('hide');
            // 「全て表示」ボタンを表示
            posts.previousElementSibling.classList.add('show');
            posts.previousElementSibling.classList.remove('hide');
        });
    }

    // post like & unlike
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
                    alert("エラー発生。もう一度お試しください。");
                }
            })
        });
    }

    // ブックマーク機能
    let bmBtns = document.getElementsByClassName('bookmark');
    for (bmBtn of bmBtns) {
        bmBtn.addEventListener("click", function () {
            let csrftoken = getCookie('csrftoken');
            let url = 'bookmark/';
            let bMark = bmBtn.lastElementChild.classList.contains('fa-bookmark-o');
            console.log(bMark);
            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function (response) {
                    // ブックマークがクリックされたらアイコンを塗りつぶす
                    if (bMark) {
                        bmBtn.innerHTML = '<i class="fa fa-bookmark" aria-hidden="true"></i>';
                        bmBtn.setAttribute('title', "ブックマークより削除");
                    } else {
                        // ブックマークから削除されたら、輪郭だけのアイコンを表示
                        bmBtn.innerHTML = '<i class="fa fa-bookmark-o" aria-hidden="true"></i>';
                        bmBtn.setAttribute('title', "ブックマークに追加");
                    }
                },
                error: function (response) {
                    alert("エラー発生。もう一度お試しください。");
                }
            })
        });
    }
});