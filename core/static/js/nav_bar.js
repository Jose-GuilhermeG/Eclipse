//variaveis
const pesquisa_input = document.getElementById("pesquisa");
const pesquisa_button = document.getElementById("pesquisar_button");

//eventos
pesquisa_input.addEventListener('keypress',(e)=>{
    if(e.key == 'Enter' && pesquisa_input.value){
        window.location.href = `/pesquisa/${pesquisa_input.value}/`;
    }else{
        alert('menssagem de erro temporaria : digite algo valido')
    }
})

pesquisa_button.addEventListener("click",(e)=>{
    if(pesquisa_input.value){
        window.location.href = `/pesquisa/${pesquisa_input.value}/`;
    }else{
        alert('menssagem de erro temporaria : digite algo valido')
    }
})