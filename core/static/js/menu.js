//variaveis
const button_menu = document.getElementById("menu_button");
const menu = document.getElementById("menu");

//temporario
let click = false;

//eventos
button_menu.addEventListener("click", () => {
    if (click) {
        menu.style.display = "none";
        click = false;
    }else{
        menu.style.display = "block";
        click = true;
    }
});