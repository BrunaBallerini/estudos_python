# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

class Livro:
    livros: list[object] = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return (f"Livro: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"Ano de Publicação: {self.ano_publicacao}")

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [
            livro for livro in Livro.livros
            if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
