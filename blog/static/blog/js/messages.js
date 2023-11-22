/*-- 

メッセージを4秒間表示して消す

--*/
document.addEventListener("DOMContentLoaded", function () {
    /*-- メッセージを4秒間表示 --*/
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 4000);
});