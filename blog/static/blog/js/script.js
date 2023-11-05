// バーガーメニューをクリックしてメニューを表示するためのプログラム
let open;
const menu = document.querySelector("#nav-menu");

// メニューを閉じる
const closeMenu = () => {
    setTimeout(function () {
        menu.style.display = "none";
        open = false;
        document.removeEventListener('mouseup', closeMenu)
    }, 100);
}

// メニューを開く
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
// コメントフォームを消して、元のコメントを表示
const hideForm = (event) => {
    let comment = event.parentElement.parentElement.parentElement;
    let textBox = event.parentElement.previousElementSibling;
    let icons = comment.nextElementSibling;
    icons.classList.remove('d-none');
    icons.classList.add('d-flex');
    comment.innerText = textBox.textContent;
}

// コメント更新の際、元のコメントを取得してフォームに表示
showCommentEditForm = (event) => {
    // 他のコメントフォームが開いていたら閉じる
    let shownForm = document.getElementById('save-comment-form');
    if (shownForm) {
        let cancelBtn = shownForm.lastElementChild.lastElementChild;
        hideForm(cancelBtn);
    }
    let id = event.dataset.id;
    let url = 'get_comment/';
    let icons = event.parentElement.parentElement;
    let comment = icons.previousElementSibling;
    var content = comment.textContent;
    // 元のコメントを取得
    $.ajax({
        url: url,
        type: 'GET',
        data: {
            id: id
        },
        success: function (response) {
            content = response['content'];
            // フォームを作成
            let commentBox = '<span id="comment-validation" class="hide" style="color: red;">' +
                'コメントを入力してください</span>' +
                '<form class="d-flex" id="save-comment-form" data-id=' +
                id + ' method="POST"><textarea type="text"' +
                ' class="update-form" id="comment">' +
                content + '</textarea><div>' +
                '<button class="blue-btn" type="submit" value="' + content +
                '" id="save-cmmt-btn">保存</button>' +
                '<button class="blue-btn mt-1" onClick="hideForm(this)">' +
                'キャンセル</button></div></form>';
            comment.innerHTML = commentBox;
            $('#comment').focus();
        },
        error: function (response) {
            // 元のコメントを表示
            comment.textContent = content;
            let alert = new bootstrap.Alert("エラー発生。もう一度お試しください。");
            setTimeout(() => {
                alert.close();
            }, 4000);
        },
        complete: function (response) {
            // 更新・削除のアイコンを再表示
            icons.classList.remove("d-flex");
            icons.classList.add("d-none");
        }
    })
}

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
                let alert = new bootstrap.Alert("エラー発生。もう一度お試しください。");
                setTimeout(() => {
                    alert.close();
                }, 4000);
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
    // メッセージを５秒間表示
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 5000);

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
});