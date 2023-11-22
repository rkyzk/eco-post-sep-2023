/*

コメント更新アイコンが押下される際、元のコメントを取得して更新フォームに表示

 */

/*-- 更新フォームを消して、元のコメントを表示 --*/
const hideForm = (event) => {
    let comment = event.parentElement.parentElement.parentElement;
    let textBox = event.parentElement.previousElementSibling;
    let icons = comment.nextElementSibling;
    icons.classList.remove('d-none');
    icons.classList.add('d-flex');
    comment.innerText = textBox.textContent;
}

/*-- 更新フォームを表示 --*/
const showCommentEditForm = (event) => {
    // 他のコメントフォームが開いていたら閉じる
    let shownForm = document.getElementById('save-comment-form');
    if (shownForm) {
        let cancelBtn = shownForm.lastElementChild.lastElementChild;
        hideForm(cancelBtn);
    }
    let id = event.dataset.id;
    let url = 'get_comment/';
    let icons = event.parentElement.parentElement; // div .update-comment
    let comment = icons.previousElementSibling; // div .comment-form
    var content = comment.textContent;
    // 元のコメントをDBより取得
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
                'コメントを入力してください.</span>' +
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
            // アイコンを押す前に表示されていたコメントを表示
            comment.textContent = content;
            // エラーメッセージを３秒表示
            comment.previousElementSibling.textContent = "エラー発生。もう一度お試しください。";
            comment.previousElementSibling.classList.remove("hide");
            comment.previousElementSibling.classList.add("show");
            setTimeout(() => {
                comment.previousElementSibling.classList.add("hide");
                comment.previousElementSibling.classList.remove("show");
            }, 3000);
        },
        complete: function (response) {
            // 更新・削除のアイコンを非表示
            icons.classList.remove("d-flex");
            icons.classList.add("d-none");
        }
    })
}