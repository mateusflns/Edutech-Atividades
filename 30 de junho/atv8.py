#Exercicio 8:
#Desenvolva um programa que receba duas notas de um aluno e calcule sua média.

# --------- LENDO A ENTRADA DO USUARIO ---------

entrada = input('digite as notas que deseja somar, separando-as com virgula:')


# --------- CALCULANDO A MEDIA ---------

notas = [int(i) for i in entrada.split(',')]
media = sum(notas) / len(notas)


# --------- EXIBINDO O RESULTADO AO USUARIO ---------

print(f'A sua media e:{media}')