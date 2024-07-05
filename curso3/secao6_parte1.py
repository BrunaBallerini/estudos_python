# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
# import math
# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# import os
# import shutil
# from datetime import datetime, timedelta
# from itertools import count

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# from dateutil.relativedelta import relativedelta
# from pytz import timezone

# data1 = datetime(2023, 4, 25, 17, 35, 12)
# print(data1)
# data_str = '2023-04-25 17:35:12'
# data_fmt = '%Y-%m-%d %H:%M:%S'
# data2 = datetime.strptime(data_str, data_fmt)
# print(data2)
# data3 = datetime.now(timezone('Asia/Tokyo'))
# print(data3)
# data4 = datetime.now()
# print(data4.timestamp())
# print(datetime.fromtimestamp(1701093377.57883))
# data_inicio = datetime.strptime('20/08/1989 10:45:00', '%d/%m/%Y %H:%M:%S')
# data_fim = datetime.strptime('27/11/2023 12:26:00', '%d/%m/%Y %H:%M:%S')
# print(data_fim > data_inicio)
# delta = data_fim - data_inicio
# print(delta.total_seconds())
# delta2 = timedelta(days=90)
# data_inicio2 = datetime.strptime('1989/08/20 10:45:00', '%Y/%m/%d %H:%M:%S')
# print(data_fim + delta2)
# print(data_inicio2 + relativedelta(years=24))
# delta3 = relativedelta(data_fim, data_inicio)
# print(delta3)
# data5 = datetime.strptime('2023-11-27 12:50:12', '%Y-%m-%d %H:%M:%S')
# print(data5.strftime('%d/%m/%Y %H:%M'), data5.year)

# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# valor_emprestimo = 1_000_000
# data_inicio_emprestimo = datetime(2020, 12, 20)

# delta_anos = relativedelta(years=7)
# data_final_emprestimo = data_inicio_emprestimo + delta_anos
# print(f'Data final: {data_final_emprestimo.strftime("%d/%m/%Y")}')

# data_parcela = data_inicio_emprestimo
# data_parcelas = []

# while data_final_emprestimo > data_parcela:
#     data_parcelas.append(data_parcela)
#     delta_mes = relativedelta(months=1)
#     data_parcela += delta_mes

# numeros_parcelas = len(data_parcelas)
# print(f'Numeros parcelas: {numeros_parcelas}')
# valor_mensal = valor_emprestimo / numeros_parcelas

# for data in data_parcelas:
#     print(f'{data.strftime("%d/%m/%Y")}, R$ {valor_mensal:,.2f}')

# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
# import calendar

# print(calendar.calendar(1989))
# print(calendar.month(1989, 8))
# last_day = calendar.monthrange(2024, 8)
# print(last_day, list(calendar.day_name))
# day_week, last_day = calendar.monthrange(2024, 8)
# print(day_week, last_day)
# print(f'{last_day} - {calendar.day_name[day_week]}')
# my_day = calendar.weekday(2023, 8, 20)
# day = list(calendar.day_name)
# print(day[my_day])


# month_august = calendar.monthcalendar(2024, 8)
# for week in month_august:
#     for day in week:
#         if day == 0:
#             continue
#         print(day, end=' ')
#     print()
# print(week)

# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# import calendar
# import locale

# locale.setlocale(locale.LC_ALL, '')  # TERMINAL locale -a | grep 'pt'
# print(calendar.calendar(1989))

# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
# import os

# os.system('clear')
# os.system('echo "Hello World"')
# print('a' * 10)

# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
# import os

# caminho = os.path.join('/Documentos/python', 'curso3', 'arquivo.txt')
# print(caminho)
# diretorio, arquivo = os.path.split(caminho)
# print(arquivo)
# nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)
# print(os.path.exists('/home/bruna/Documentos/python/curso3'))
# print(os.path.abspath('.'))
# print(caminho)
# print(os.path.basename(caminho))
# print(os.path.basename(diretorio))
# print(os.path.dirname(caminho))

# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# import os

# path_ = os.path.join('/home/bruna/Imagens')
# for pasta in os.listdir(path_):
#     caminho_completo = os.path.join(path_, pasta)
#     if not os.path.isdir(caminho_completo):
#         continue
#     for imagens in os.listdir(caminho_completo):
#         print(imagens)

# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
# import os
# from itertools import count

# path_ = os.path.join('/home/bruna/Imagens')
# counter = count()

# for root, dir_, files in os.walk(path_):
#     the_counter = next(counter)
#     print(the_counter, 'Root: ', root)
#     print(' ', the_counter, 'Dir: ', dir_)
#     print('     ', the_counter, 'Files: ', files)

# BEM INTERESSANTE
# from itertools import count  # IMPORTA UM CONTADOR
# counter = count()  # CRIA UMA INSTANCIA
# the_counter = next(counter)  # CHAMA O PRÓXIMO VALOR - INFINITO

# HORÁRIO PARA MEDICAMENTO
# date = datetime.now()
# delta = relativedelta(days=5)
# final_date = date + delta

# print(f'Final date: {final_date}')

# medication_time = datetime(2023, 11, 27, 6, 00, 00)
# delta_hour = relativedelta(hours=8)
# medication_hour = []

# while final_date > date:
#     while final_date > medication_time:
#         medication_time += delta_hour
#         medication_hour.append(medication_time)
#     delta_day = relativedelta(days=1)
#     date += delta_day
#     # print(f'Date: {date}')

# for date in medication_hour:
#     print(date.strftime('%d/%m/%Y %H:%M'))

# Original:
# Stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

# def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
#     # Formata um tamanho, de bytes para o tamanho apropriado

#     # Se o tamanho for menor ou igual a 0, 0B.
#     if tamanho_em_bytes <= 0:
#         return "0B"

#     # Tupla com os tamanhos
#     #                      0    1     2     3     4     5
#     abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
#     # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
#     # math.log vai retornar o logaritmo do tamanho_em_bytes
#     # com a base (1000 por padrão), isso deve bater
#     # com o nosso índice na abreviação dos tamanhos
#     indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
#     # Por quanto nosso tamanho deve ser dividido para
#     # gerar o tamanho correto.
#     potencia = math.pow(base, indice_abreviacao_tamanhos)
#     # Nosso tamanho final
#     tamanho_final = tamanho_em_bytes / potencia
#     # A abreviação que queremos
#     abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
#     return f'{tamanho_final:.2f} {abreviacao_tamanho}'


# caminho = os.path.join('/home/bruna/Imagens')
# counter = count()

# for root, dirs, files in os.walk(caminho):
#     the_counter = next(counter)
#     print(the_counter, 'Pasta atual', root)

#     for dir_ in dirs:
#         print('  ', the_counter, 'Dir:', dir_)

#     for file_ in files:
#         caminho_completo_arquivo = os.path.join(root, file_)
#         tamanho = os.path.getsize(caminho_completo_arquivo)
#         # stats = os.stat(caminho_completo_arquivo)
#         #tamanho = stats.st_size
#         print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))

# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

# HOME = os.path.expanduser('~')
# DESKTOP = os.path.join(HOME, 'Área de Trabalho')
# PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
# NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
# # shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
