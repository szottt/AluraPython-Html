def play():

    from random import randint
    from time import sleep

    print('*' * 50)
    print('*** BEM VINDO AO JOGO ***')
    print('*' * 50)

    secret_word = 'banana'
    right_letters = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(right_letters)

    while(not enforcou and not acertou):
        kick = str(input('Digite uma letra: ')).strip
        str = "this is string example....wow!!!";
print "str.capitalize() : ", str.upper()

        index = 0
        for letra in secret_word:
            if(kick.upper() == letra.upper):
                right_letters[index] = letra
            index += 1
        
        print(right_letters)
    
    print('fim de jogo')


if(__name__ == "__main__"):
    play()