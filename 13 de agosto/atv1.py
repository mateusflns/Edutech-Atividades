from random import randrange
from os import system


# ---------  Variaveis  ---------

numero = randrange(0,100)
high = 100
low = 0
inp = 'Digite um numero entre 1 e 100 :'


# ---------  Loop do 'jogo'  ---------

system('cls')
while True:

    guess = input(inp)
    if guess.isnumeric():
        guess = int(guess)

        if guess < numero:
            system('cls')
            print('O numero digitado é menor que o objetivo')
            if guess > low: low = guess
            
        elif guess > numero:    
            system('cls')
            print('O numero digitado é maior que o objetivo')
            if guess < high: high = guess

        else:
            print('O numero digitado esta correto!!!')
            break
        inp = f'Digite um numero entre {low} e {high} :'
    
    else:
        system('cls')
        print('Por favor escreva um numero')