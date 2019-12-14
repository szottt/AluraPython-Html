def play():

    from random import randint
    from time import sleep

    print('*' * 50)
    print('*** BEM VINDO AO JOGO ***')
    print('*' * 50)

    secret_word = 'banana'.upper()
    right_letters = ["_" for letter in secret_word]

    reinforce = False
    acertou = False
    erros = 0

    print(right_letters)

    while(not reinforce and not acertou):
        kick = input('Digite uma letra: ').strip().upper()

        if(kick in secret_word):

            index = 0
            for letra in secret_word:
                if(kick == letra):
                    right_letters[index] = letra
                index += 1
        else:
            erros += 1

        reinforce = erros == 6

        acertou = "_" not in right_letters

        print(right_letters)
        
    if(acertou):
        print('Voce ganhou')
    else:
        print('Voce errou')
    print('fim de jogo')

if(__name__ == "__main__"):
    play()