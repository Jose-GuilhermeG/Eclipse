from email.message import EmailMessage
from smtplib import SMTP
from flask import url_for

User = 'projetoeclipseloja@gmail.com'
Senha = 'kslx mqml ytsd zbja'

Porta = 587
Server = 'smtp.gmail.com'

msg = EmailMessage()

def mandar_email(assunto,para,conteudo ):

    assert User
    assert Senha

    msg['subject'] = assunto
    msg['from'] = User
    msg['to'] = para
    msg.set_content(conteudo)

    try:
        with SMTP(Server,Porta) as server:
            server.starttls()
            server.login(User,Senha)
            server.send_message(msg)
            print(f'email mandado para {para} : {assunto} ')

            return 'email enviado'
    except Exception as e:
        print(e)
        return e
    


def recuperar_senha_email(user,token):
    assunto = 'Recuperar a senha de usuario'
    link = url_for(f'auth.recuperar_senha',nome = user.nome_user, token = token,_external = True)
    conteudo_email = f"""Olá {user.nome_user},
    Recebemos uma solicitação para redefinir a senha da sua conta. Se você não fez essa solicitação, por favor, ignore este e-mail.
    Para redefinir sua senha, clique no link abaixo:
    
    {link}
    
    Este link será válido por 24 horas. Após esse período, você precisará solicitar um novo link de recuperação.
    
    Se você tiver alguma dúvida ou precisar de ajuda, entre em contato com nossa equipe de suporte.
    
    
    Obrigado, Eclipse"""

    mandar_email(assunto,user.email_user,conteudo_email)
