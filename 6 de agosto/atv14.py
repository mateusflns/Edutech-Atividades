entrada = float(input('Digite o valor do seu salario R$:').replace(',','.'))
valor = str(round(entrada+(entrada*0.15),2))

if len(valor.split('.')[1]) == 1:
    valor += '0'

print(f'O seu salario com 15% de aumento sera R$:{valor}')