/* 
コメント更新のためのプログラム
*/

/*
 クッキー取得
 https://docs.djangoproject.com/en/dev/ref/csrf/#ajaxより引用
*/
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

/* 更新したコメントを保存、表示 */
$(document).on('submit', '#save-comment-form', function (e) {
    e.preventDefault();
    let csrftoken = getCookie('csrftoken');
    let id = this.dataset.id;
    let url = 'update_comment/';
    let comment = document.getElementById("comment").value;
    var originalCmmt = document.getElementById("save-cmmt-btn").value;
    var validation = this.previousElementSibling;
    var editedLabel = validation.parentElement.
    previousElementSibling.previousElementSibling.previousElementSibling;

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
                // エラーメッセージを３秒表示
                editedLabel.nextElementSibling.nextElementSibling.textContent = "エラー発生。もう一度お試しください。";
                editedLabel.nextElementSibling.nextElementSibling.classList.remove("hide");
                editedLabel.nextElementSibling.nextElementSibling.classList.add("show");
                setTimeout(() => {
                    editedLabel.nextElementSibling.nextElementSibling.classList.add("hide");
                    editedLabel.nextElementSibling.nextElementSibling.classList.remove("show");
                }, 3000);
            },
            complete: function (response) {
                // 更新・削除アイコン表示
                icons.classList.remove('d-none');
                icons.classList.add('d-flex');
            }
        })
    }
});