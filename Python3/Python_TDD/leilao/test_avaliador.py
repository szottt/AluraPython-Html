from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    # test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    def setUp(self):
        self.igor = Usuario('igor')
        self.lance_do_igor = Lance(self.igor, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        hugo = Usuario('hugo')
        lance_do_hugo = Lance(hugo, 100.0)

        self.leilao.propoe(lance_do_hugo)
        self.leilao.propoe(self.lance_do_igor)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        hugo = Usuario('hugo')
        lance_do_hugo = Lance(hugo, 100.0)

        self.leilao.propoe(self.lance_do_igor)
        self.leilao.propoe(lance_do_hugo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_igor)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        hugo = Usuario('hugo')
        lance_do_hugo = Lance(hugo, 100.0)
        marcela = Usuario('marcela')

        lance_da_marcela = Lance(marcela, 200.0)

        self.leilao.propoe(lance_do_hugo)
        self.leilao.propoe(self.lance_do_igor)
        self.leilao.propoe(lance_da_marcela)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)