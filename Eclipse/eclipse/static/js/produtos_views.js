const url = '/user/carrinho/add'
const cookies = document.cookie

function pegar_cookie_user(cookies){
    let cookies_separados =  cookies.split(';')
    let user = String()
    for(let cookie_number in cookies_separados) {
        if(cookies_separados[cookie_number].includes('access')){
            user = cookies_separados[cookie_number].split('=')[1]
            return user
        }
    }
}


