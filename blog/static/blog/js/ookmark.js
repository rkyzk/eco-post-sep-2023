 /*
 ブックマークに記事を追加・削除する
*/
 document.addEventListener("DOMContentLoaded", function () {
     let bmBtns = document.getElementsByClassName('bookmark');
     for (bmBtn of bmBtns) {
         bmBtn.addEventListener("click", function () {
             let csrftoken = getCookie('csrftoken');
             let url = 'bookmark/';
             let bMark = bmBtn.lastElementChild.classList.contains('fa-bookmark-o');
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
                     bmBtn.parentElement.nextElementSibling.textContent = "エラー発生。もう一度お試しください。";
                     bmBtn.parentElement.nextElementSibling.classList.remove("hide");
                     bmBtn.parentElement.nextElementSibling.classList.add("show");
                     // エラーメッセージを３秒間表示
                     setTimeout(() => {
                         bmBtn.parentElement.nextElementSibling.classList.remove("show");
                         bmBtn.parentElement.nextElementSibling.classList.add("hide");
                     }, 3000);
                 }
             })
         });
     }
 });