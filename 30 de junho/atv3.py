#Exercicio 3:
#Crie um script que exiba o nome da pessoa, e a sua data de aniversario formata

from datetime import date
from os import system, get_terminal_size

system("cls")


# --------- VARIAVEIS E CONSTANTES ---------

aniversario = False

terminal_columns = get_terminal_size().columns

data_hoje = date.today()

NUMEROS = '1234567890'

MESES_DICT = {
    1 : 'Janeiro',2 : 'Fevereiro',3 : 'Marco',4 : 'Abril',
    5 : 'Maio', 6 : 'Junho',7 : 'Julho',8 : 'Agosto',
    9 : 'Setembro', 10 : 'Outubro',11 : 'Novembro',12 : 'Dezembro'
}

MESES = []

data_final = ''

for i in range(1,13):
    MESES.append(MESES_DICT[i])

def titulo(titulo):
    text = round((terminal_columns - len(titulo))/2 - 1)
    while (text * 2 + len(titulo) + 2) - terminal_columns != 0:
        text = text + ((text * 2 + len(titulo) + 2) - terminal_columns * -1)
    print(text * '*' , titulo, text * '*' )


# --------- LOOP ENQUANTO A DATA FOR INVALIDA ---------

while True:
    nome = input('Digite o seu nome :')
    system('cls')

    data = input('Digite a sua data de nascimento (D/M/A) :')
    system('cls')


    # --------- FORMATACAO DA DATA DE NASCIMENTO ---------

    idx = 1
    for mes in MESES:
        if mes.upper() in data.upper():
            if idx < 10:
                idx = '0' + str(idx)
            data = (data.upper()).replace(mes.upper(),str(idx))
            break
        else:
            idx += 1

    for i in data:
        if i in NUMEROS:
            data_final += i


    # --------- FORMATACAO DO NOME ---------

    if ' ' in nome:
        nome = nome.split(' ')
        nome = nome[0].title()


    # --------- CHEQUE SE A DATA DE NASCIMENTO E VALIDA ---------

    if len(data_final) != 8:
        print('Data de nascimento invalida')
    else:
        break


# --------- CHEQUE SE O ANIVERSARIO E NESTE ANO OU NO OUTRO ---------

if int(data_final[2:4]) > data_hoje.month:
    ano = data_hoje.year
else:
    ano = data_hoje.year + 1

data_list = [data_final[0:2], data_final[2:4], str(ano)]


# --------- CHEQUE SE A DATA DE NASCIMENTO E VALIDA ---------

if int(data_list[0]) == data_hoje.day and int(data_list[1]) == data_hoje.month:
    print(f'Parabéns {nome}, o seu aniversario é hoje, Parabens!!!')
else:
    print(f'{nome} faz aniversario no dia {data_list[0]}, no mes de', 
    f'{MESES_DICT[int(data_final[2:4])]} no ano de {data_list[2]}\n',
    f'{data_list[0]}/{data_list[1]}/{data_list[2]}')