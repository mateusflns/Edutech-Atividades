from random import randrange
from time import sleep
from os import system

# ---------  Constantes  ---------

LETRAS = 'qwertyuiopasdfghjklzxcvbnm'

PALAVRAS = (
        'Bailarina;Futebol;Estatua;Pintor;Frio;Bebe;Mimico;Escova;'
        'dentes;Lapis;Livro;Astronauta;Amor;odio;Cego;Cadeira;Sacola;'
        'Professor;Medico;Calculadora;Artista;Vitoria;Pescador;Internet;'
        'Basquete;Semente;Policial;Amargo;Bilhete;Xadrez;Banana;Microbio;'
        'Romance;Carteira;Maquina;lavar;Prancha;surfe;Debate;Lixo;Sombra;'
        'Cadeado;Massagem;borboleta;Cavalo;Cachorro;Caranguejo;Chimpanze;'
        'Coelho;Jacare;Elefante;Galinha;Girafa;Leao;Gato;Sapo;Veado;Tigre;'
        'Grilo;Formiga;Abelha;Hipopotamo;Golfinho;Tigre;Capivara;Esquilo;'
        'Rato;PorcoTemplo;Capsula;Estrada;Planeta;terra;Estojo;Paraiso;'
        'Estrela;Trem;Infinito;macaAcender;Afilhado;Ardiloso;aspero;'
        'Assombracao;Asterisco;Basquete;Caminho;Champanhe;Chiclete;'
        'Chuveiro;Coelho;Contexto;Convivencia;Coracao;Desalmado;'
        'Eloquente;Esfirra;Esquerdo;Excecao;Fugaz;Gororoba;Heterossexual'.split(';')
    )

# ---------  Funcoes  ---------


def get_input_number(frase):
    number = input(frase)
    negative = False
    if number[0] == '-':
        number = number[1:]
        negative = True
        
    if not number.isnumeric():
        print('Por favor insira um numero')
        number = get_input_number(frase)
    
    if negative:
        return int(number) * -1
    else:
        return int(number)


def check_random(lista,word): #lento 
    numero = -1
    while numero in lista:
        numero = randrange(0,100)

    l = lista.append(numero)

    if PALAVRAS[numero] == word:
        print(f'A palava escolhida foi {PALAVRAS[numero]} com numero {numero + 1}')
    else:
        check_random(lista,word)


def check_loop(palavra): #velocidade linear ao tamanho da lista de PALAVRAS
    for i in PALAVRAS:
        if i == palavra:
            print(f'A palava escolhida foi {i} com numero {PALAVRAS.index(i) + 1}')


def check_hangman(palavra,delay=1):
    numero = -1
    lista = [-1]
    forca = []
    for i in palavra:
        forca.append(i.lower())
    system('cls')
    acertos = ['*'] * len(palavra)
    vidas = get_input_number('Quantas vidas o computador deve ter? (-1 para vidas infinitas) :')
    n = 0
    system('cls')
    
    
    # ---------  Gerando nova letra aleatoria  ---------
    
    while True:
        while True:
            numero = randrange(-1,len(LETRAS))
            if numero not in lista:
                lista.append(numero)
                break
        letra = LETRAS[numero].lower()
        
        print(f'O computador tentou a letra {letra}')
        new = 0

        
        # ---------  Checando se a letra exite na palavra  ---------
        
        if letra in forca:
            for i in forca:
                if i == letra:
                    acertos[forca.index(i)] = i
                    forca[forca.index(i)] = 0
                    new += 1
        

        # ---------  Checando se a letra existe ou nao na palavra  ---------
        
        if new > 0:
            system('cls')     
            print(f'O computador acertou a letra {letra}')
            sleep(delay)
            print(acertos)
            n += new
        else:
            sleep(delay)
            print('O computador errou, nao foi dessa vez')
            vidas -= 1
        sleep(delay)
        

        # ---------  Checando se o computador venceu ou morreu  ---------
        
        if n == len(forca):
            system('cls')
            final = ''
            for i in acertos:
                final += i

            print(f'O computador consegui adivinhar a palavra')    
            print(f'A palavra e {final}')
            break
        elif vidas == 0:
            system('cls') 
            print('O computador nao conseguiu adivinhar a palavra')
            break


def main():
    numero = get_input_number('Digite um numero entre 1 a 100 :')

    palavra = PALAVRAS[numero-1]
    lista = [-1]
    
    for i in PALAVRAS:
        check_hangman(i,0)   

    check_hangman(palavra,1)
    #check_hangman(palavra,0) # "instant" hangman
    #check_random(lista,palavra)
    #check_loop(palavra)
    


if __name__ == '__main__':    
    main()
