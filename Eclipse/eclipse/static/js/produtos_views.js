const url = '/user/carrinho/add'
const produto = document.getElementById('nome').innerText
let carrinho_button = document.getElementById("carrinho_button")

async function Add_carrinho(){
    let corpo = {
        "method": "POST",
        "headers" : {
            'Content-Type':'application/json'
        },
        "body": JSON.stringify({
            "produto": produto,
            'quantia' : 1,
        }),
    }
    try{
        let requisição = await fetch(url,corpo)
        if(requisição.ok){
            window.location.href = "/user/carrinho"
        }

    }
    catch(e){
        console.log(e)
        return e
    }
}

carrinho_button.addEventListener("click",()=>{
    Add_carrinho()
})