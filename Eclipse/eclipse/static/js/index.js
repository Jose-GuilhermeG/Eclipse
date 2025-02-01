import Produto from "./produtos_class.js";

const url = '/'

const voce_pode_gostar_conteiner  = document.getElementById("voce_pode_gostar");

function criar_produtos(array,local){
    for(let element of array){
        let produto_var = new Produto(element.Nome,element.Preço,element.Descrição,element.Imagem,local)
        produto_var.criar_card
    }
}

async function fetch_url(url,local){
    try{
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


function pedir_produto(quantia,local){
    let url_quantia = url + `produtos/quantia/${quantia}`
    return fetch_url(url_quantia,local)
}

//teste, o primeiro paramentro é a quantia, o segundo onde os itens vão ficar
pedir_produto(6,voce_pode_gostar_conteiner)