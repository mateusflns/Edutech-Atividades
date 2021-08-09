from os import system

system('cls')


# --------- VARIAVEIS ---------

titulo = 8*"*" + 'TABUADA' + 8*"*"


# --------- LENDO A ENTRADA DO USUARIO ---------

print(titulo)

entrada = int(input('insira o numero :'))


# --------- EXIBINDO OS VALORES PARA O USUARIO ---------

system('cls')

print(titulo)

for i in range(1,11):
    if i < 10:
        print(f'{entrada}x0{i} == {entrada*i}')
    else:
        print(f'{entrada}x{i} == {entrada*i}')