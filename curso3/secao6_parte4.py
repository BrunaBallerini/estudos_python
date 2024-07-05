
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
#
# Lifo  e fifo
# pilha e fila

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear
# from collections import deque

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # ✅ Legal (LIFO com lista)
# #  0  1  2  3  4  5  6  7  8  9
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista.append(10)
# #  0  1  2  3  4  5  6  7  8  9  10
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista.append(11)
# #  0  1  2  3  4  5  6  7  8  9  10, 11
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# ultimo_removido = lista.pop()
# #  0  1  2  3  4  5  6  7  8  9  10
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Último: ', ultimo_removido)
# print('Lista:', lista)
# #  0  1  2  3  4  5  6  7  8  9  10
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print()


# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 🚫 Ruim (FIFO com lista)
# #  0  1  2  3  4  5  6  7  8  9
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista.insert(0, 10)
# #   0  1  2  3  4  5  6  7  8  9, 10
# # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista.insert(0, 11)
# #  0   1   2  3  4  5  6  7  8  9, 10 11
# # [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# primeiro_removido = lista.pop(0)  # 11
# #  0   1  2  3  4  5  6  7  8  9, 10
# # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('Primeiro: ', primeiro_removido)  # 11
# print('Lista:', lista)  # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print()

# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante

# ✅ Legal (FIFO com deque)

# fila_correta: deque[int] = deque()
# fila_correta.append(3)  # Adiciona no final
# fila_correta.append(4)  # Adiciona no final
# fila_correta.append(5)  # Adiciona no final
# fila_correta.appendleft(2)  # Adiciona no começo
# fila_correta.appendleft(1)  # Adiciona no começo
# fila_correta.appendleft(0)  # Adiciona no começo
# print(fila_correta)  # deque([0, 1, 2, 3, 4, 5])
# fila_correta.pop()  # 5
# fila_correta.popleft()  # 0
# print(fila_correta)  # deque([1, 2, 3, 4])

# openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalação)
# Com essa biblioteca será possível ler e escrever dados em células
# específicas, formatar células, inserir gráficos,
# criar fórmulas, adicionar imagens e outros elementos gráficos às suas
# planilhas. Ela é útil para automatizar tarefas envolvendo planilhas do
# Excel, como a criação de relatórios e análise de dados e/ou facilitando a
# manipulação de grandes quantidades de informações.
# Instalação necessária: pip install openpyxl
# Documentação: https://openpyxl.readthedocs.io/en/stable/

# from pathlib import Path

# from openpyxl import Workbook
# from openpyxl.worksheet.worksheet import Worksheet

# ROOT_FOLDER = Path(__file__).parent
# WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

# workbook = Workbook()
# Nome para a planilha
# sheet_name = 'Minha planilha'
# Criamos a planilha
# workbook.create_sheet(sheet_name, 0)
# Selecionou a planilha
# worksheet: Worksheet = workbook[sheet_name]
# worksheet: Worksheet = workbook.active

# Remover uma planilha
# workbook.remove(workbook['Sheet'])

# Criando os cabeçalhos
# worksheet.cell(1, 1, 'Nome')
# worksheet.cell(1, 2, 'Idade')
# worksheet.cell(1, 3, 'Nota')

# students = [
#     # name, age, grade
#     ['João', 14, 5.5],
#     ['Maria', 13, 9.7],
#     ['Luiz', 15, 8.8],
#     ['Alberto', 16, 10],
# ]

# for i, student_row in enumerate(students, start=2):
#     for j, student_column in enumerate(student_row, start=1):
#         worksheet.cell(i, j, student_column)

# for student in students:
#     worksheet.append(student)

# workbook.save(WORKBOOK_PATH)

# READING A WORKBOOK
# from pathlib import Path

# from openpyxl import load_workbook

# from openpyxl.cell import Cell
# from openpyxl.worksheet.worksheet import Worksheet

# ROOT_FOLDER = Path(__file__).parent
# WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

# Carregando um arquivo do excel
# workbook: Workbook = load_workbook(WORKBOOK_PATH)
# workbook = load_workbook(WORKBOOK_PATH)

# Nome para a planilha
# SHEET_NAME = 'Minha planilha'

# Selecionou a planilha
# worksheet: Worksheet = workbook[sheet_name]
# worksheet = workbook[SHEET_NAME]

# row: tuple[Cell]
# for row in worksheet.iter_rows(min_row=2):
#     for cell in row:
#         print(cell.value, end='\t')

#         if cell.value == 'Maria':
#             worksheet.cell(row=cell.row, column=2, value='23')
#     print()

# worksheet['B3'].value = 14

# workbook.save(WORKBOOK_PATH)

# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
# from pathlib import Path

# from PIL import Image

# ROOT_FOLDER = Path(__file__).parent
# ORIGINAL = ROOT_FOLDER / 'original.JPG'
# NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

# pil_image = Image.open(ORIGINAL)
# width, height = pil_image.size
# exif = pil_image.info['exif']

# width     new_width
# height    new_height
# new_width = 640
# new_height = round(height * new_width / width)

# new_image = pil_image.resize(size=(new_width, new_height))
# new_image.save(
#     NEW_IMAGE,
#     optimize=True,
#     quality=70,
#     exif=exif,
# )
