from dominio import Usuario, Lance, Leilao, Avaliador

igor = Usuario('igor')
hugo = Usuario('hugo')

lance_do_hugo = Lance(hugo, 100.0)
lance_do_igor = Lance(igor, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_hugo)
leilao.lances.append(lance_do_igor)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
