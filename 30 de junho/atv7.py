#Exercicio 7:
#Leia um número, mostre seu dobro, triplo, e raíz quadrada.

from math import sqrt


# --------- LENDO A ENTRADA DO USUARIO ---------

input = int(input("Digite um numero :"))


# --------- EXIBINDO O RESULTADO AO USUARIO ---------

print("o dobro do seu numero é:", input * 2)
print("o triplo do seu numero é:", input * 3)
print("a raiz quadrada do seu numero é:", sqrt(input))