import tkinter as tk
from tkinter import filedialog
from conexao_email import*


pasta = ''


email = ''
senha = ''




class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.title("Email Pythoning Bot")
        self.text_email = tk.StringVar()
        self.text_senha = tk.StringVar()
        

    def labelNome(self):
        self.label_nome = tk.Label(self.root, text="Email: ", font=("Comic Sans", 12)) 
        self.label_nome.pack(pady=0, ipadx=10)

        

    def entryNome(self):
        self.entry_nome = tk.Entry(self.root, textvariable=self.text_email)
        self.entry_nome.pack(pady=0, ipadx=50)

    def labelSenha(self):
        self.label_senha = tk.Label(self.root, text="Senha(de app): ", font=("Comic Sans", 12))
        self.label_senha.pack(pady=1, ipadx=10)

    def entrySenha(self):
        self.entry_senha = tk.Entry(self.root, textvariable=self.text_senha, show='*')
        self.entry_senha.pack(pady=1, ipadx=50)

    def labelPasta(self):
        self.label_pasta = tk.Label(self.root, text=" 'Pasta' ", font=("Comic Sans", 12))
        self.label_pasta.pack(pady=30, ipadx=10)
    

    def escolhePasta(self):
        self.pasta_download = filedialog.askdirectory()
        if self.pasta_download:
            self.label_pasta.config(text=self.pasta_download)

    def btnPasta(self):
        self.btn_pasta = tk.Button(self.root, text="Selecione a Pasta", command=lambda: self.escolhePasta())
        self.btn_pasta.pack(pady=40, ipadx=10, padx=20) 
    
    def buttonEntrar(self):
        self.btn_entrar = tk.Button(self.root, text="Entrar", command=lambda: Entrar(self))
        self.btn_entrar.pack(pady=50, ipadx=20)
        
    def statusLabel(self):
        self.status_label = tk.Label(self.root, text="Status", font=('Comic Sans', 12))
        self.status_label.pack(pady=40, ipadx=50)
      

def pegaUser(interface):
    if not interface.text_email.get() or not interface.text_senha.get() or interface.text_senha.get() == '' or interface.text_email.get() == '':
        interface.status_label.config(text="Informações inválidas")
        return None, None
    else:
        email = interface.text_email.get()
        senha = interface.text_senha.get()
        return email,senha



import imaplib
import email
from email.header import decode_header
import os

import time

'''
def Entrar(interface):
    EMAIL, SENHA = pegaUser(interface)
    IMAP_SERVER = "imap.gmail.com"
    NUM_EMAILS = 5

    if EMAIL != None and SENHA != None:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)

        interface.status_label.config(text='Tentando conectar')

        
        mail.login(EMAIL,SENHA)
        mail.select("inbox")
        status, messages = mail.search(None, 'UNSEEN SUBJECT "Codigo de Barras"')

        interface.status_label.config(text="Conexão sucedida")
        email_ids = messages[0].split()

        ultimos_emails = email_ids[-NUM_EMAILS:]
        
        for email_id in ultimos_emails:
            #buscar mails ppor id
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            
            #pegando conteudo do email
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    email_cru = response_part[1]
                    msg = email.message_from_bytes(email_cru)
                    print(msg)

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
                        interface.status_label.config(text=f"Arquivo baixado com sucesso{filename} em {filepath}")
                        time.sleep(2)







        mail.close()
        mail.logout()

    else:
        interface.status_label.config(text="Erro nas informações")
    
    

'''


def criaInterface():
    
    interface = Interface()
    
    

    interface.labelNome()
    interface.entryNome()
    interface.labelSenha()
    interface.entrySenha()
    interface.labelPasta()
    
    interface.btnPasta()
    interface.statusLabel()
    interface.buttonEntrar()
    
    


    return interface






