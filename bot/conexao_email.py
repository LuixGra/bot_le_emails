import imaplib
import email
from email.header import decode_header
import os

import time



def buscaMails(ultimos_emails, mail, interface):
    for email_id in ultimos_emails:
            #buscar mails ppor id
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            

            #pegando conteudo do email
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    email_cru = response_part[1]
                    msg = email.message_from_bytes(email_cru)
                    print(msg)
                    time.sleep(1)
                for part in msg.walk():

                    #verifica se o email tem anexo
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    #obtem o nome do anexo
                    filename = part.get_filename() 

                    #se arquivo não nulo
                    if bool(filename):
                        #cria o caminho do arquivo
                        filepath = os.path.join(interface.pasta_download, filename)
                        with open(filepath, 'wb') as f:
                            f.write(part.get_payload(decode=True)) #escreve o conteudo decodificado
                        print('Arquivo baixado com sucesso')
                        
                        time.sleep(2)



def pegaUser(interface):
    if not interface.text_email.get() or not interface.text_senha.get() or interface.text_senha.get() == '' or interface.text_email.get() == '':
        interface.status_label.config(text="Informações inválidas")
        return None, None
    else:
        email = interface.text_email.get()
        senha = interface.text_senha.get()
        return email,senha


def Conectar(interface, EMAIL, SENHA):
    IMAP_SERVER = "imap.gmail.com"
    NUM_EMAILS = 5

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    interface.status_label.config(text='Tentando conectar')

    time.sleep(3)
        
    mail.login(EMAIL,SENHA)
    mail.select("inbox")
    status, messages = mail.search(None, 'UNSEEN SUBJECT "Codigo de Barras"')

    interface.status_label.config(text="Conexão sucedida")
    email_ids = messages[0].split()

    time.sleep(1)
    ultimos_emails = email_ids[-NUM_EMAILS:]


    buscaMails(ultimos_emails, mail, interface)



    mail.close()
    mail.logout()

    interface.status_label.config(text="Download concluido")



def Entrar(interface):
    EMAIL, SENHA = pegaUser(interface)
    

    if EMAIL != None and SENHA != None:
        ultimos_emails = Conectar(interface, EMAIL, SENHA)



    else:
        interface.status_label.config(text="Erro nas informações")
    
    
