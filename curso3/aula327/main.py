# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# ROOT_FOLDER = Path(__file__).parent
# ORIGINAL_FOLDER = ROOT_FOLDER / 'pdfs_originais'
# NEW_FOLDER = ROOT_FOLDER / 'arquivos_alterados'
# NEW_FOLDER.mkdir(exist_ok=True)
# ORIGINAL_FILE = ROOT_FOLDER / 'pdfs_originais' / 'R20231124.pdf'
# print(ORIGINAL_FILE)

# reader = PdfReader(ORIGINAL_FILE)
# print(len(reader.pages))
# for page in reader.pages:
# print(page.extract_text())
# print(page.images)

# page0 = reader.pages[0]
# image0 = page0.images[1]
# print(image0)
# image_path = NEW_FOLDER / image0.name
# with open(image_path, 'wb') as image:
#     image.write(image0.data)

# writer = PdfWriter()
# writer.add_page(page0)
# NEW_FILE_PATH = NEW_FOLDER / 'page0.pdf'
# with open(NEW_FILE_PATH, 'wb') as file:
#     writer.write(file)

# NEW_FILE_PATH = NEW_FOLDER / 'new_pdf.pdf'
# with open(NEW_FILE_PATH, 'wb') as file:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(file)

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as file:
#         writer.add_page(page)
#         writer.write(file)

# merger = PdfMerger()

# files = [
#     NEW_FOLDER / 'page1.pdf',
#     NEW_FOLDER / 'page0.pdf'
# ]

# for file in files:
#     merger.append(file)

# with open(NEW_FOLDER / 'merged.pdf', 'wb') as file:
#     merger.write(file)


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_alterados'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20231124.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

# page0 = reader.pages[0]
# imagem0 = page0.images[0]

# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore

files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()
