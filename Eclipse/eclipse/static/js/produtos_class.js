class Produto{
    constructor(Nome,Preço,Descricao,Imagem,local){
        this.Nome = Nome;
        this.Preço = Preço;
        this.Descricao = Descricao;
        this.Imagem = Imagem;
        this.local = local;
    }

    //card do produto
    get criar_card(){
        this.card = document.createElement("div");
        this.img_card = document.createElement("img");
        this.Nome_card = document.createElement("h1");
        this.Preço_card = document.createElement("h2");
        this.button_comprar = document.createElement("button");
        

        //classes para css
        this.card.className = "";
        this.img_card.className = "";
        this.Nome_card.className = "";
        this.Preço_card.className = "";
        this.button_comprar.className = "";

        //valores viziveis
        this.img_card.src = this.Imagem
        this.Nome_card.textContent = this.Nome
        this.Preço_card.textContent = this.Preço
        this.button_comprar.textContent = 'comprar';

        //append
        this.card.appendChild(this.img_card)
        this.card.append(this.Nome_card);
        this.card.append(this.Preço_card);
        this.card.append(this.button_comprar);
        this.local.append(this.card);

    }
}

export default Produto;