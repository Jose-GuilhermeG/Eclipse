from os import system
from requests import get
from app.models import produto
from app.db import db
from app import create_app

def menu_produtos():
    
    print('o que deseja trabalhar?')
    print('1-cadastrar produtos')

    escolha = input('Escolha: ')

    if escolha == '1':
        cadastrar_produtos()

def cadastrar_produtos():


    while True:
        nome_produto = input('Digite o nome do produto: ')
        preço_produto = float(input('Digite o preço do produto: '))
        imagem_link = input('link da imagem: ')
        descrição_produto = input('Digite a descrição do produto: ')

        url = imagem_link
        imagem = get(url)

        if imagem.status_code == 200:

            imagem = imagem.content
            produto_cadastrado = produto(nome_produto,preço_produto,imagem,descrição_produto)

            app = create_app()
            with app.app_context():
                
                db.session.add(produto_cadastrado)
                db.session.commit()                

            print('produto cadastrado')
        else: 
            print("Falha ao baixar a imagem. Status code:",imagem.status_code)

        
        continuar = input('Continuar(S/N)')

        if continuar.upper() == 'N':
            break
    

def menu():

    system('cls')

    print('o que deseja trabalhar?')
    print('1-produtos')

    escolha = input('Escolha: ')

    if escolha == '1':
        menu_produtos()


menu()