# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
# import os
# from dotenv import load_dotenv  # type: ignore

# load_dotenv()

# print(os.environ)
# print(os.getenv('BD_PASSWORD'))

# ENVIANDO E-MAILS SMTP COM PYHTON
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta http-equiv="X-UA-Compatible" content="IE=edge" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Arquivo para o e-mail</title>
#   </head>
#   <body>
#     Olá ${nome},
#     <br />
#     Estou testando
#     <span style="color: red; font-weight: bold;">este e-mail</span>
#     em HTML.
#     <br />
#     <br />

#     <em>
#       Atenciosamente,
#       <br />
#       Luiz Otávio.
#     </em>
#   </body>
# </html>

# import os
# import pathlib
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from string import Template
# from dotenv import load_dotenv  # type: ignore

# load_dotenv()

# Caminho arquivo HTML
# CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
# remetente = os.getenv('FROM_EMAIL', '')
# destinatario = remetente

# Configurações SMTP
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_username = os.getenv('FROM_EMAIL', '')
# smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
# with open(CAMINHO_HTML, 'r') as arquivo:
#     texto_arquivo = arquivo.read()
#     template = Template(texto_arquivo)
#     texto_email = template.substitute(nome='Helena')

# Transformar nossa mensagem em MIMEMultipart
# mime_multipart = MIMEMultipart()
# mime_multipart['from'] = remetente
# mime_multipart['to'] = destinatario
# mime_multipart['subject'] = 'Este é o assunto do e-mail'
# corpo_email = MIMEText(texto_email, 'html', 'utf-8')
# mime_multipart.attach(corpo_email)

# Envia o e-mail
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.ehlo()
#     server.starttls()
#     server.login(smtp_username, smtp_password)
#     server.send_message(mime_multipart)
#     print('E-mail enviado com  sucesso!')

# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
# import os
# import shutil
# from pathlib import Path
# from zipfile import ZipFile

# # Caminhos
# CAMINHO_RAIZ = Path(__file__).parent
# CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_304_diretorio_zip'
# CAMINHO_COMPACT = CAMINHO_RAIZ / 'aula304_compactado.zip'
# CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula304_descompactado'

# shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
# Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
# shutil.rmtree(str(CAMINHO_COMPACT).replace('.zip', ''), ignore_errors=True)
# shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
# CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


# def criar_arquivos(qtd: int, zip_dir: Path):
#     for i in range(qtd):
#         texto = 'arquivo_%s' % i
#         with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
#             arquivo.write(texto)


# criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando um zip e adicionando arquivos
# with ZipFile(CAMINHO_COMPACT, 'w') as zip:
#     for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
#         for file in files:
# print(file)
# zip.write(os.path.join(root, file), file)
# Criando o zip com o caminho e os arquivos a serem zipados

# Lendo arquivos de um zip
# with ZipFile(CAMINHO_COMPACT, 'r') as zip:
#     for arquivo in zip.namelist():
#         print(arquivo)

# Extraindo arquivos de um zip
# with ZipFile(CAMINHO_COMPACT, 'r') as zip:
#     zip.extractall(CAMINHO_DESCOMPACTADO)

# sys.argv - Executando arquivos com argumentos no sistema
# import sys

# argumentos = sys.argv
# qtd_argumentos = len(argumentos)

# if qtd_argumentos <= 1:
#     print('Você não passou argumentos')
# else:
#     try:
#         print(f'Você passou os argumentos {argumentos[1:]}')
#         print(f'Faça alguma coisa com {argumentos[1]}')
#         print(f'Faça outra coisa com {argumentos[2]}')
#     except IndexError:
#         print('Faltam argumentos')

# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
# from argparse import ArgumentParser

# parser = ArgumentParser()

# parser.add_argument(
#     '-b', '--basic',
#     help='Mostra "Olá mundo" na tela',
# type=str, # Tipo do argumento
# metavar='STRING',
# default='Olá mundo', # Valor padrão
# required=False,
# action='append',  # Recebe o argumento mais de uma vez
# nargs='+', # Recebe mais de um valor
# )
# parser.add_argument(
#     '-v', '--verbose',
#     help='Mostra logs',
#     action='store_true'
# )
# args = parser.parse_args()

# if args.basic is None:
#     print('Você não passou o valor de b.')
#     print(args.basic)
# else:
#     print('O valor de basic:', args.basic)

# print(args.verbose)

# Básico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
# import requests

# http:// -> 80
# https:// -> 443
# url = 'http://localhost:3333/'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())  # GERA ERRO -> RESPOSTA NÃO É JSON
# print(response.text)

# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs

# import requests
# from bs4 import BeautifulSoup

# url = 'http://localhost:3333/'
# response = requests.get(url=url)
# # raw_html = response.text
# bytes_html = response.content
# parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
# # if parsed_html.title is not None:
# #     print(parsed_html.title.text)
# top_jobs_ = parsed_html.select_one('#intro > div > div > article > h2')
# if top_jobs_ is not None:
#     print(top_jobs_.text)
#     parent_ = top_jobs_.parent
#     if parent_ is not None:
#         for p in parent_.select('p'):
#             print(p.text)

# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4
# import subprocess
# import sys

# # print(sys.platform)
# # sys.platform = linux, linux2, darwin, win32

# cmd = ['ls -lah /']
# ENCODING = 'utf_8'
# SYSTEM = sys.platform

# if SYSTEM == "win32":
#     cmd = ['ping', '127.0.0.1']
#     ENCODING = 'cp850'


# proc = subprocess.run(
#     cmd, capture_output=True,
#     text=True, encoding=ENCODING,
#     shell=True, check=True
# )

# print()

# # print(proc.args)
# # print(proc.stderr)
# print(proc.stdout)
# # print(proc.returncode)

# (Parte 1) Threads - Executando processamentos em paralelo
# from threading import Lock, Thread
# from time import sleep

# class MeuThread(Thread):
#     def __init__(self, texto: str, tempo: int):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread('Thread 1', 5)
# t1.start()

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 3', 2)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


# def vai_demorar(texto: str, tempo: int):
#     sleep(tempo)
#     print(texto)


# t4 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t4.start()

# t5 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t5.start()

# t6 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t6.start()

# for i in range(20):
#     print(i)
#     sleep(.5)


# t7 = Thread(target=vai_demorar, args=('Olá mundo !', 10))
# t7.start()
# t7.join()

# while t7.is_alive():
#     print('Esperando a thread')
#     sleep(2)

# print('Thread acabou!')

# class Ingressos:
#     def __init__(self, estoque: int) -> None:
#         self.estoque = estoque
#         self.lock = Lock()

#     def comprar(self, quant: int):
#         self.lock.acquire()
#         if self.estoque < quant:
#             print('Não temos ingressos suficientes.')
#             self.lock.release()
#             return

#         sleep(1)
#         self.estoque -= quant
#         print(f'Você comprou {quant} ingresso(s).'
#               f'Temos {self.estoque} ingresso(s)')

#         self.lock.release()


# if __name__ == '__main__':
#     ingressos = Ingressos(10)
#     for i in range(1, 20):
#         t = Thread(target=ingressos.comprar, args=(i,))
#         t.start()
