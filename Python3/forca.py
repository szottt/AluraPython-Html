import random


def play():

    
    print_opening_message()
    secret_word = carry_secret_word()
    right_letters = initialize_hit_letters(secret_word)
    print(right_letters)


    reinforce = False
    hit = False
    mistakes = 0

    while(not reinforce and not hit):

        kick = request_kick()

        if(kick in secret_word):
            correct_kick_mark(kick, right_letters, secret_word)

        else:
            mistakes += 1
            draw_gallows(mistakes)

        reinforce = mistakes == 7
        hit = "_" not in right_letters
        print(right_letters)

        
    if(hit):
        print_winner_message()
    else:
        print_loser_message(secret_word)



def print_opening_message():
    print('*' * 50)
    print('*** BEM VINDO AO JOGO ***')
    print('*' * 50)

def carry_secret_word():
    archive = open('palavras.txt' , 'r')
    words = []
    for line in archive:
        line = line.strip().upper()
        words.append(line)
    archive.close()
    number = random.randint(0, len(words))
    secret_word = words[number]
    return secret_word

def initialize_hit_letters(word):
    return ["_" for letter in word]

def request_kick():
    kick = input('Digite uma letra: ').strip().upper()
    return kick

def correct_kick_mark(kick, right_letters, secret_word):
    index = 0
    for letra in secret_word:
        if(kick == letra):
            right_letters[index] = letra
        index += 1

def print_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_gallows(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    play()