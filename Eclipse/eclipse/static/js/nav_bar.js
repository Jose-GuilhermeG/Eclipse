import Get_requisição from './get.js'

const input_pesquisa = document.getElementById("pesquisa")
const produtos_pesquisa_local = document.getElementById("produtos_pesquisa_local")
const url = '/pesquisa/?pesquisa='

// Cria um elemento de produto com imagem, nome e preço
function criar_itens(Img,Nome,Preço){
    let conteiner = document.createElement('div')
    let img = document.createElement('img')
    let nome = document.createElement('h1')
    let preço = document.createElement('h2')

    img.src = Img
    nome.textContent = Nome
    preço.textContent = 'R$ ' + Preço

    conteiner.addEventListener('click',()=>{
        window.location = '/produtos/' + Nome
    })

    conteiner.className = 'conteiner_pesquisa'
    conteiner.append(img,nome,preço)

    return conteiner
}
// Mostra os itens no contêiner de produtos
function mostrar_itens(array){

    while(produtos_pesquisa_local.firstChild){
        produtos_pesquisa_local.removeChild(produtos_pesquisa_local.firstChild)
    }

    if(array != null){
        for(let element of array){
            let item = criar_itens(element.Imagem,element.Nome,element.Preço)
            produtos_pesquisa_local.appendChild(item)
        }
    }
    else{
        let mensagem = document.createElement('h1')
        mensagem.textContent = 'Nenhum produto encontrado'
        produtos_pesquisa_local.append(mensagem)
    }
}

async function realizar_pesquisa(valor){
    if(valor){
        let url_pesquisa = url + valor
        try{
            let requisição = await fetch(url_pesquisa)
            if(requisição.status != 200){
                return null
            }
            if(requisição.ok){
                requisição = await requisição.json()
                return requisição
            }

        }
        catch (e){
            console.error(e)
            return {'err' : 'erro interno, perdão'}
        }
    }

    return null
  
}
input_pesquisa.addEventListener('input',async ()=>{
    produtos_pesquisa_local.style.display = 'flex'
    mostrar_itens(await realizar_pesquisa(input_pesquisa.value))
})

input_pesquisa.addEventListener('keypress',(e)=>{
    if(e.key == 'Enter'){
        window.location = `/pesquisa/${input_pesquisa.value}`
    }
})

document.body.addEventListener('click',()=>{
    produtos_pesquisa_local.style.display = 'none'

})

