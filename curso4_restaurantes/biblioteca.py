# pylint: disable=missing-module-docstring
# type: ignore

from exercicio import Livro

if __name__ == '__main__':

    livro1 = Livro("Aprendendo Python", "John Doe", 2020)
    livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

    print(livro1)
    print(livro2)

    livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
    print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
    livro3.emprestar()
    print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

    livro4 = Livro("Python in Practice", "Emily Coder", 2021)
    print(
        f"Antes de emprestar (biblioteca): Livro disponível? "
        f"{livro4.disponivel}")
    livro4.emprestar()
    print(
        f"Depois de emprestar (biblioteca): Livro disponível? "
        f"{livro4.disponivel}")
    print()
    Livro.livros = [livro1, livro2, livro3, livro4]
    ANO_ESPECIFICO = 2020
    livros_disponiveis_ano = Livro.verificar_disponibilidade(ANO_ESPECIFICO)
    print(f"Livros disponíveis em {ANO_ESPECIFICO}: ")
    for livros in livros_disponiveis_ano:
        print(f"{livros}")
