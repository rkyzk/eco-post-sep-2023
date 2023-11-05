// バーガーメニューをクリックしてメニューを表示
let open;
const menu = document.querySelector("#nav-menu");

const closeMenu = () => {
    setTimeout(function () {
        menu.style.display = "none";
        open = false;
        document.removeEventListener('mouseup', closeMenu)
    }, 100);
}

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
                'Please enter this field.</span>' +
                '<form class="d-flex" id="save-comment-form" data-id=' +
                id + ' method="POST"><textarea type="text"' +
                ' class="update-form" id="comment">' +
                content + '</textarea><div>' +
                '<button class="blue-btn" type="submit" value="' + content +
                '" id="save-cmmt-btn">save</button>' +
                '<button class="blue-btn mt-1" onClick="hideForm(this)">' +
                'cancel</button></div></form>';
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
            console.log("hi");
            icons.classList.remove("d-flex");
            icons.classList.add("d-none");
        }
    })
}

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

    // 「折りたたむ」ボタンでブログを隠す
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