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
    def nome(self, nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
supernatural = Serie('supernatural', 2007, 17)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

supernatural.dar_likes()
supernatural.dar_likes()

# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {supernatural.nome} - Likes: {supernatural.likes}')
print(f'{vingadores.nome} - {vingadores.duracao} - {vingadores.likes}')
print(f'{supernatural.nome} - {supernatural.temporadas} - {supernatural.likes}')