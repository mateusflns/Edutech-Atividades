#Exercicio 4:
#Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.


# --------- VARIAVEIS E CONSTANTES ---------

posneg = 'positivo'

tipo = 0
letras = 'qwertyuiopaasdfghjklzxcvbnm'
numeros = '1234567890'

# --------- LENDO A ENTRADA DO USUARIO ---------

entrada = input("Digite algo :")


for i in letras:
    if i.upper() in entrada.upper():
        tipo = 3

if tipo == 0:
    for i in numeros:
        if i in entrada:
            tipo = 2

if tipo == 2:
    if '.' in entrada:
        tipo = 1

# --------- COMUNICANDO O RESULTADO AO USUARIO ---------

if tipo == 1:
    print('A sua entrada é um numero decimal')
elif tipo == 2:
    print('A sua entrada é um numero')
elif tipo == 3:
    print('A sua entrada é alfanumerica')
else:
    print('A sua entrada não contem numeros ou letras')