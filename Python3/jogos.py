import forca
import adivinhacao

def escolhe_jogo():
    print('*' * 50)
    print('*** ESCOLHA SEU JOGO***')
    print('*' * 50)

    print('(1) Forca (2) Adivinhação')

    game = int(input('Qual jogo: '))

    if(game == 1):
        print("Jogando Forca")
        forca.play()
    elif(game == 2):
        print('Jogando Adivinhação')
        adivinhacao.play()

if(__name__ == "__main__"):
    escolhe_jogo()
    