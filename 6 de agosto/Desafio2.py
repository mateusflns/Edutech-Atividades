from datetime import date
from random import randrange
from os import system

codigo_banco = input('Digite o codigo do banco :')
preco = int(input('Digite o preco desse boleto R$:').replace(',','.'))


data_hoje = date.today()
data_hoje = [data_hoje.day, data_hoje.today().month, data_hoje.today().year]

if data_hoje[1] < 10:
    data_hoje[1] = '0' + str(data_hoje[1])
if data_hoje[0] < 10:
    data_hoje[0] = '0' + str(data_hoje[0])

random = randrange(1000,10000)


codigo_boleto = (
    codigo_banco + ' | ' + str(random) + str(data_hoje[0]) +
    str(data_hoje[1]) + str(data_hoje[2]) + 8 * '0' + str(preco)
)

system('cls')
print(codigo_boleto)