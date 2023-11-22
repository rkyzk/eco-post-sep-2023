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

/* ----- コメント更新のためのプログラム---------------*/


// クッキー取得
// https://docs.djangoproject.com/en/dev/ref/csrf/#ajaxより引用
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// 更新したコメントを保存、表示
$(document).on('submit', '#save-comment-form', function (e) {
    e.preventDefault();
    let csrftoken = getCookie('csrftoken');
    let id = this.dataset.id;
    let url = 'update_comment/';
    let comment = document.getElementById("comment").value;
    var originalCmmt = document.getElementById("save-cmmt-btn").value;
    var validation = this.previousElementSibling;
    var editedLabel = validation.parentElement.previousElementSibling.previousElementSibling;
    // テキストエリアが空だったら、バリデーションを表示
    if (comment.trim() === "") {
        validation.classList.remove('hide');
        validation.classList.add('show');
    } else {
        // 更新・削除アイコンを取得
        let commentParent = this.parentElement;
        let icons = commentParent.nextElementSibling;
        // コメントをバックエンドに送る
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                id: id,
                comment: comment,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (response) {
                commentParent.textContent = comment;
                // バリデーションが表示されていたら非表示にする
                if (validation.classList.contains('show')) {
                    validation.classList.remove('show');
                    validation.classList.add('hide');
                }
                // 「更新済み」ラベルがなかったら、次のページ更新まで表示させる
                if (editedLabel.textContent != '更新済み') {
                    editedLabel.nextElementSibling.classList.remove('hide');
                    editedLabel.nextElementSibling.classList.add('show');
                }
            },
            error: function (response) {
                commentParent.textContent = originalCmmt;
                alert("エラー発生。もう一度お試しください。");
            },
            complete: function (response) {
                // 更新・削除アイコン表示
                icons.classList.remove('d-none');
                icons.classList.add('d-flex');
            }
        })
    }
});

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