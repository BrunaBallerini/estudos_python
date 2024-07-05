# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# pylint: disable=missing-module-docstring, no-name-in-module

# PySide6 para GUI (interface gráfica) com Qt em Python - Instalação
# - A seção original desse curso usou PyQt5 (estamos atualizando para PySide6)
# - Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
# - Qt é uma biblioteca usada para a criação de GUI (interface gráfica
#   do usuário) escrita em C++.
#   - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
#   biblioteca para a criação de interfaces gráficas sem ter que usar outra
#   linguagem de programação.
# - PySide6 é uma referencia à versão 6 da Qt (Qt 6)
# - Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

# Por que mudei de PyQt para PySide na atualização?
# - PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
#   projeto Qt for Python project - https://doc.qt.io/qtforpython/
# - Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente
#   similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você
#   ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes
#   basta trocar o nome de PySide para PyQt e vice-versa.
# - A maior diferença entre PyQt e PySide está na licença:
#   PyQt usa GPL ou commercial e PySide usa LGPL.
#   Em resumo: com PySide, você tem a permissão uso da biblioteca para fins
#   comerciais, sem ter que compartilhar o código escrito por você para o
#   público.
#   Licenças são tópicos complexos, portanto, se oriente sobre elas
#   antes de usar qualquer software de terceiros.
#   https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

# from pathlib import Path

# ROOT_FILE = Path(__file__).parent
# print(ROOT_FILE)
# import PySide6.QtCore
# print(PySide6.__version__)

# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
# import sys

# from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
#                                QPushButton, QWidget)

# # from PySide6.QtWidgets import (QHBoxLayout, QVBoxLayout)

# app = QApplication(sys.argv)  # Gerencia o loop da aplicação
# window = QMainWindow()  # Possivel colocar menu e barra de status
# central_widget = QWidget()  # Widget genérico
# window.setCentralWidget(central_widget)
# window.setWindowTitle('MInha Janela')
# layout = QGridLayout()  # Layout
# central_widget.setLayout(layout)  # Relaciona o widget central e layout

# botao1 = QPushButton('Texto do botão 1')
# botao1.setStyleSheet('font-size: 40px;')
# # botao.show()  # Adiciona o widget na hierarquia e exibe a janela

# botao2 = QPushButton('Texto do botão 2')
# botao2.setStyleSheet('font-size: 40px;')
# # botao2.show()  # Adiciona o widget na hierarquia e exibe a janela

# botao3 = QPushButton('Texto do botão 3')
# botao3.setStyleSheet('font-size: 40px;')

# # layout
# layout.addWidget(botao1, 1, 1, 1, 1)
# layout.addWidget(botao2, 1, 2, 1, 1)
# layout.addWidget(botao3, 2, 1, 1, 2) # Inserindo outros widgets na hierarquia


# # statusBar
# status_bar = window.statusBar()
# status_bar.showMessage('Mostrar mensagem na barra')

# # Slot é um metodo executado quanto um signal é disparado


# def slot_1(status_bar_):
#     status_bar_.showMessage('Slot Executado')


# def started_function(function):
#     def wrapper(status_bar_):
#         return function(status_bar_)
#     return wrapper


# teste = started_function(slot_1)


# def slot_2(checked):
#     print(checked)


# def slot_3(action):
#     def inner():
#         slot_2(action.isChecked())
#     return inner


# # menuBar
# menu_bar = window.menuBar()
# primeiro_menu = menu_bar.addMenu('Menu 1')
# primeira_acao = primeiro_menu.addAction('Ação 1')
# # primeira_acao.triggered.connect(lambda: slot_1(status_bar)) # Signal (slot)
# primeira_acao.triggered.connect(lambda: teste(status_bar))  # Signal (slot)

# segunda_acao = primeiro_menu.addAction('Ação 2')
# segunda_acao.setCheckable(True)
# segunda_acao.toggled.connect(slot_2)  # Signal (slot)
# # segunda_acao.triggered.connect(lambda: slot_1(status_bar))
# segunda_acao.hovered.connect(slot_3(segunda_acao))  # Signal (slot)
# # Código do professor
# # primeiro_menu = menu_bar.addMenu('Primeiro Menu')
# # primeira_acao = primeiro_menu.addAction('Primeira ação')

# botao1.clicked.connect(slot_3(segunda_acao))

# # central_widget.show()  # Central widget entra na hierarquia e mostra janela
# window.show()
# # Executa o loop da aplicação -  Procura eventos acontecendo durante o loop
# app.exec()

# MELORANDO O CÓDIGO
# import sys

# from PySide6.QtCore import Slot
# from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
#                                QPushButton, QWidget)

# app = QApplication(sys.argv)
# window = QMainWindow()
# central_widget = QWidget()
# window.setCentralWidget(central_widget)
# window.setWindowTitle('MInha Janela')
# layout = QGridLayout()
# central_widget.setLayout(layout)

# botao1 = QPushButton('Texto do botão 1')
# botao1.setStyleSheet('font-size: 40px;')

# botao2 = QPushButton('Texto do botão 2')
# botao2.setStyleSheet('font-size: 40px;')

# botao3 = QPushButton('Texto do botão 3')
# botao3.setStyleSheet('font-size: 40px;')

# # layout
# layout.addWidget(botao1, 1, 1, 1, 1)
# layout.addWidget(botao2, 1, 2, 1, 1)
# layout.addWidget(botao3, 2, 1, 1, 2)

# # statusBar
# status_bar = window.statusBar()
# status_bar.showMessage('Mostrar mensagem na barra')


# @Slot()
# def slot_1(status_bar_):
#     def inner():
#         status_bar_.showMessage('Slot Executado')
#     return inner


# @Slot()
# def slot_2(checked):
#     print(checked)


# @Slot()
# def slot_3(action):
#     def inner():
#         slot_2(action.isChecked())
#     return inner


# # menuBar
# menu_bar = window.menuBar()
# primeiro_menu = menu_bar.addMenu('Menu 1')
# primeira_acao = primeiro_menu.addAction('Ação 1')
# primeira_acao.triggered.connect(slot_1(status_bar))

# segunda_acao = primeiro_menu.addAction('Ação 2')
# segunda_acao.setCheckable(True)
# segunda_acao.toggled.connect(slot_2)
# segunda_acao.hovered.connect(slot_3(segunda_acao))

# botao1.clicked.connect(slot_3(segunda_acao))

# window.show()
# app.exec()


# Trabalhando com classes e herança no PySide6
# import sys

# from PySide6.QtCore import Slot
# from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
#                                QPushButton, QWidget)


# class MyWindow(QMainWindow):
#     def __init__(self, parent: QWidget | None = None) -> None:
#         super().__init__(parent)

#         self.central_widget = QWidget()

#         self.setCentralWidget(self.central_widget)
#         self.setWindowTitle('Minha Janela')

#         # Botão 1
#         self.botao1 = self.make_button('Botão 1')
#         self.botao1.clicked.connect(self.segunda_acao_marcada)

#         # Botão 2
#         self.botao2 = self.make_button('Botão 2')

#         # Botão 3
#         self.botao3 = self.make_button('Botão 3')

#         # grid_layout
#         self.grid_layout = QGridLayout()
#         self.central_widget.setLayout(self.grid_layout)
#         self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
#         self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
#         self.grid_layout.addWidget(self.botao3, 2, 1, 1, 2)

#         # statusBar
#         self.status_bar = self.statusBar()
#         self.status_bar.showMessage('Mostrar mensagem na barra')

#         # menuBar
#         self.menu_bar = self.menuBar()
#         self.primeiro_menu = self.menu_bar.addMenu('Menu 1')
#         self.primeira_acao = self.primeiro_menu.addAction('Ação 1')
#         self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar)

#         self.segunda_acao = self.primeiro_menu.addAction('Ação 2')
#         self.segunda_acao.setCheckable(True)
#         self.segunda_acao.toggled.connect(self.segunda_acao_marcada)
#         self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

#     @Slot()
#     def muda_mensagem_da_status_bar(self):
#         self.status_bar.showMessage('Slot Executado')

#     @Slot()
#     def segunda_acao_marcada(self):
#         print('Está marcado?', self.segunda_acao.isChecked())

#     def make_button(self, text):
#         botao = QPushButton(text)
#         botao.setStyleSheet('font-size: 80px;')
#         return botao


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec()

# DEFAULT_MARGIN = 15
# margins = [DEFAULT_MARGIN for _ in range(4)]
# print(*margins)

# i = 's'
# float(i)
