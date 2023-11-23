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