import Produto from "./produtos_class.js";
import Load from "./load.js"

const url = '/'

let more = document.getElementById('more')
let autal = 6

const voce_pode_gostar_conteiner  = document.getElementById("voce_pode_gostar");
const promoçoes_dia  = document.getElementById("promoçoes_dia");



let section = Array.from(document.getElementsByTagName("section"));

function criar_produtos(array,local){

    while(local.firstChild){
        local.removeChild(local.firstChild);
    }

    for(let element of array){
        let produto_var = new Produto(element.Nome,element.Preço,element.Descrição,element.Imagem,element.promoções,local)
        produto_var.criar_card
    }
}

async function fetch_url(url,local){
    const load  = new Load(local)
    try{
        load.criar
        let result = await fetch(url)
        if(!result.ok){
            throw new Error("err : " + result.statusText);
        }
        result = await result.json()
        criar_produtos(result,local)
        return result
    }
    catch(e){
        console.error('Erro na requisição:', e)
    }
}


async function pedir_produto(quantia,local,filter){
    if(filter){
        let url_quantia = url + `produtos/?quantia=${quantia}&${filter}`
        return fetch_url(url_quantia,local)

    }
    let url_quantia = url + `produtos/?quantia=${quantia}`
    return fetch_url(url_quantia,local)
}

//teste, o primeiro paramentro é a quantia, o segundo onde os itens vão ficar

window.addEventListener("load", ()=>{
    pedir_produto(autal,voce_pode_gostar_conteiner)
    pedir_produto(autal,promoçoes_dia,'promoção_hj=True')
})

more.addEventListener('click',()=>{
    autal = autal + 3
    pedir_produto(autal,voce_pode_gostar_conteiner)
})