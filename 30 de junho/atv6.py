#Exercicio 4:
#faca um programa que mostra a soma entre dois valores e mostre o antecessor e o sucessor dele mesmo


# --------- LENDO A ENTRADA DO USUARIO ---------

x = int(input("Digite um numero :"))
y = int(input("Digite outro numero"))


# --------- COMUNICANDO O RESULTADO AO USUARIO ---------

resposta = x + y

print("A soma dos numeros é:", resposta)
print("O antecessor do numero é ", resposta - 1)
print("O sucessor do numero é ", resposta + 1)