
def play():

    from random import randint
    from time import sleep

    secret_number = randint(1,100)

    ########################   Cores   ########################
    color = {
            'limpa':'\033[m',
            'azul':'\033[4;34m',
            'vermelho':'\033[1;31m' 
    }

    ######################## variaveis ########################
    nivel = 0
    attemp = 0
    round = 1
    score = 1000


    print('*-' * 20)
    print("""Nosso jogo funciona da seguinte maneira...
    Primeiro vamos escolher um numero entre 0 e 100 e depois que voce escolher a dificuldade vamos começar
    """)
    print("""
    EScolha o nivel da Dificuldade
    (1) Moises (2) Boss (3) DEUS 
    """)


    nivel = int(input('Defina seu nivel: '))

    if(nivel == 1):
        attemp = 20
    elif(nivel == 2):
        attemp = 10
    else:
        attemp = 5

    print('*-' * 20)
    print('Preparando o jogo...')
    sleep(2)
    print('Pronto vamos jogar!')



    #attemp = int(input('Em quantas tentativas voce pode nos responder: '))
    #print(secret_number)


    while(round <= attemp):
        print(f'Tentativa numero {round} de {attemp}')


        kick = int(input(f'Digite seu {round}º palpite: '))
        if (kick <= 0 or kick > 100):
            print('{}Digite um numero valido na sua proxima tentativa{}'.format(color['vermelho'],color['limpa']))
            continue

        win = kick == secret_number
        bigger = kick > secret_number
        smaller = kick < secret_number

        if(win):
            print('{}Parabens voce acertou e fez {} pontos{}'.format(color['azul'],score,color['limpa']))
            break
        else:
            if(bigger):
                print('O seu chute foi maior do que o numero secreto')
            elif(smaller):
                print('O seu chute foi menor do que o numero secreto')

            missed_score = abs(secret_number - kick)
            score = score - missed_score

        
        if(round == attemp and kick != secret_number):
            print('{}Voce perdeu!!{}'.format(color['vermelho'],color['limpa']))

        round = round + 1



    print('Fim de jogo')

if(__name__ == "__main__"):
    play()