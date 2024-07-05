class Lista:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, posicao):
        return self.item[posicao]

    def __len__(self):
        return len(self.item)


meu_objeto = Lista([1, 2, 4])
contador = 0
for i in meu_objeto:
    contador += 1

if len(meu_objeto) == contador:
    print('São iguais!')
else:
    print('Não são iguais!')

class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return "{} - {}".format(self.titulo, self.diretor)

    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo


class Playlist:
    def __init__(self, programa):
        self.programa = programa

    def __getitem__(self, item):
        return self.programa[item]


land = Filme("La La Land", "Damien Chazelle")
poderoso = Filme("O Poderoso Chefão", "Francis Ford Coppola")
teoria = Filme("A Teoria de Tudo", "James Marsh")

meus_filmes = [land, poderoso, teoria]

for filme in meus_filmes:
    print(filme)

minha_playlist = Playlist(meus_filmes)
filme_procurado = Filme("A Teoria de Tudo", "James Marsh")

for filme in minha_playlist:
    if filme_procurado == filme:
        print("Tenho o filme!")
    else:
        print("Não tenho")
