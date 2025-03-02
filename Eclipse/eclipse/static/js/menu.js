const menu = document.getElementById("menu")
const menu_button = document.getElementById("menu_button")
let menu_open = false


menu_button.addEventListener("click",()=>{
    if(menu_open){
        menu.style.display = 'none'
        menu_open = false
    }
    else{
        menu.style.display = 'block'
        menu_open = true
    }
})
