from flask import request,make_response,jsonify,abort,render_template,send_file,url_for
from io import BytesIO
from .bp import produtos
from ..models import produto
from ..db import db

@produtos.route('/<id>')
def index_produto(id):
    produto_pedido = db.session.query(produto).filter_by(id=id).first()

    if produto_pedido != None:
        json = jsonify({'id' : produto_pedido.id, 'Nome' : produto_pedido.nome_produto,'preço' : produto_pedido.preço,'descrição' : produto_pedido.descrição})
    
    return f'{produto_pedido.__repr__()}'

@produtos.route("/imagem/<int:id>")
def imagem(id):
    produto_existe = db.session.query(produto).filter_by(id=id).first()

    imagem = send_file(BytesIO(produto_existe.imagen),mimetype="image/jpeg")

    return imagem



@produtos.route('/view/<id>')
def view_produto(id):
    produto_existe = db.session.query(produto).filter_by(id=id).first()

    print(produto_existe)

    imagem = url_for('produto.imagem',id = id)

    

    if produto_existe != None:
        return render_template('produto.html',imagem = imagem,nome = produto_existe.nome_produto,preço = produto_existe.preço)
    
    return abort(404)