class Produto{
    constructor(Nome,Preço,Descricao,Imagem,promoções,local){
        this.Nome = Nome;
        this.Preço = Preço;
        this.Descricao = Descricao;
        this.Imagem = Imagem;
        this.promoções = promoções
        this.local = local;
    }

    //card do produto
    get criar_card(){
        this.card = document.createElement("div");
        this.img_card = document.createElement("img");
        this.Nome_card = document.createElement("h1");
        if(this.Nome.length > 18){
            this.Nome_card.style.fontSize = '1.2em'
        }
        this.Preço_card = document.createElement("h2");
        this.button_comprar = document.createElement("button");
        this.desconto_card = this.criar_desconto_card;
        
        //eventos
        this.img_card.addEventListener("click",()=>{
            window.location = '/produtos/' + this.Nome
        })

        //classes para css
        this.card.className = "produto";
        this.img_card.className = "produto_imagem";
        this.Nome_card.className = "nome_produto";
        if(this.desconto_card == null) {this.Preço_card.className = "produto_preço";}
        else{this.Preço_card.className =  'antigo_preço'}
        
        this.button_comprar.className = "produto_button";
        
        //valores viziveis
        this.img_card.src = this.Imagem
        this.Nome_card.textContent = this.Nome
        this.Preço_card.textContent = 'R$' + this.Preço
        this.button_comprar.textContent = 'comprar';
        
        //append
        
        if(this.desconto_card == null) {
            this.card.append(this.img_card,this.Nome_card,this.Preço_card,this.button_comprar)
        }
        else{
            this.card.append(this.img_card,this.Nome_card,this.Preço_card,this.desconto_card,this.button_comprar)
            
        }
        
        this.local.append(this.card);

    }

    get criar_desconto_card(){
        if(this.promoções.length != 0){
            for(let promo of this.promoções){
                if(promo.estado == 'Valido'){
                    let desconto_card = document.createElement("span");
                    desconto_card.className = 'desconto'
                    let valor = this.Preço - ((this.Preço * promo.Desconto)/100)
                    desconto_card.textContent = 'R$' + valor
                    return desconto_card
                }

            return null
            }
        }

        return null
    }
}

export default Produto;