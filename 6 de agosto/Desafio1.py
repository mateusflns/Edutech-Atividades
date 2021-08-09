from random import randrange
from os import system

funcionarios = []
salarios = []


while True:
    funcionarios.append(input('Digite o nome do novo funcionario :'))
    salarios.append(float(input('Digite o salario desse funcionario :').replace(',','.')))


    if len(funcionarios) % 3 == 0:
        for i in salarios:
            salarios[salarios.index(i)] = round(i * 1.05,2)
        system('cls')
        print('Todos os funcionarios acabam de ganhar um aumento no salario de 5%')
        

        
    if len(funcionarios) % 10 == 0:
        idx = 0
        system('cls')
        while idx < len(funcionarios):
            string = f'{funcionarios[idx]} com o salario de {salarios[idx]}'

            if type(salarios[idx]) == int:
                string = string + '.00'
            elif len(str(salarios[idx]).split('.')[1]) == 1:
                string = string + '0'

            print(string)
            idx += 1

        random = randrange(0,len(funcionarios))
        salarios[random] = round(salarios[random] * 1.1)
        
        print(
            f'Parabens {funcionarios[random]} voce recebeu um aumento no'
            f'salario de 10%, agora seu salario e R$:{salarios[random]}')

