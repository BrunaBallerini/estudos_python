class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return "{} - {} - {}".format(self._nome, self.ano, self._likes)

    def __repr__(self):
        return str(self.ano)


class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} - {}".format(self._nome, self.ano, self.duracao, self._likes)

    def __repr__(self):
        return str(self.ano)


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __srt__(self):
        return "{} - {} - {} - {}".format(self._nome, self.ano, self.temporadas, self._likes)

    def __repr__(self):
        return str(self.ano)


class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def lista(self):
        return self._programas

    @property
    def nome(self):
        return self._nome.title()


vingadores = Filmes("vingadores", 2020, 160)
vingadores.nome = "vingadores - a guerra infinita"
vingadores.dar_likes()
supernatural = Series("supernatural", 2007, 10)
supernatural.dar_likes()
tmep = Filmes('todo mundo em panico', 1999, 100)
tmep.dar_likes()
tmep.dar_likes()
demolidor = Series('demolidor', 2016, 2)
demolidor.dar_likes()
demolidor.dar_likes()

filmes_series = [vingadores, supernatural, demolidor, tmep]

minha_playlist = Playlist('fim de semana', filmes_series)

print(vingadores in minha_playlist)

for programa in minha_playlist:
    print(programa)

print(len(minha_playlist))
print(minha_playlist.nome)

# evolucao:
# print("{} - {} - {}.".format(vingadores.nome, vingadores.duracao, vingadores.likes))
# print("{} - {} - {}.".format(supernatural.nome, supernatural.temporadas, supernatural.likes))
# for programa in filmes_series:
#  if hasattr(programa,'duracao'):
#    particularidade = programa.duracao
#  elif hasattr(programa,'temporadas'):
#    particularidade = programa.temporadas
#  print("{} - {} - {}.".format(programa.nome, particularidade, programa.likes))

# for programa in filmes_series:
#  particularidade = programa.duracao if hasattr(programa,'duracao') else hasattr(programa,'temporadas')
#  print("{} - {} - {}.".format(programa.nome, particularidade, programa.likes))
# print(repr(supernatural)) - forma de imprimir como console
# tentativa de dar input na lista de filmes_series
# filmes_series = []
# playlist = 0
# while playlist < 2:
#  programas = input("Digite sua o programa de sua preferencia: ")
#  filmes_series.append(programas)
#  playlist += 1
# lista = ['palavra1', 'palavra2', 'palavra3']
# print('palavra1' in lista)
#@property
#def tamanho(self):
#    return len(self._programas)
