import Get_requisição from "./get.js"

const url = '/user/carrinho/add'
const produto = document.getElementById('nome').innerText
const imagem_produto = document.getElementById("produto_imagem")
const padrão = imagem_produto.src
let carrinho_button = document.getElementById("carrinho_button")
const quantia_select = document.getElementById("quantia")


async function Add_carrinho(){
    let corpo = {
        "method": "POST",
        "headers" : {
            'Content-Type':'application/json'
        },
        "body": JSON.stringify({
            "produto": produto,
            'quantia' : quantia_select.value,
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

const lista_cores = document.getElementById("lista_cores")

let produto_nome = window.location.href
produto_nome = produto_nome.split('/')
produto_nome = produto_nome[produto_nome.length-1]


const req = new Get_requisição('/produtos',[`nome=${produto_nome}`])
const result_req= await req.result() 
if(result_req[0].cores.length != 0){
    result_req.forEach(element => {
    for(let cor of element.cores){
        let cor_element = document.createElement('div')
        cor_element.className = "cor_disponivel"
        cor_element.style.backgroundColor = cor.Cor_code
        cor_element.addEventListener('click',()=>{
            imagem_produto.src = cor.Imagem
        })
        lista_cores.appendChild(cor_element)

    }
});
}
else{
    let cor_element = document.createElement("h1")
    cor_element.textContent = 'Mais Nenhuma cor disponivel '
    lista_cores.appendChild(cor_element)
}
