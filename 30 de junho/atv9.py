#Exercicio 9:
#Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.

# --------- LENDO A ENTRADA DO USUARIO ---------

entrada = int(input('Digite uma distancia em metros:'))


# --------- EXIBINDO OS VALORES PARA O USUARIO ---------

print(f'{entrada} metros coresponde a {entrada*100} centimetros ou {entrada*1000} milimetros')