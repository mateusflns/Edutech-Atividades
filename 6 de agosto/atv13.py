entrada = float(input('Digite o valor do produto R$:').replace(',','.'))
valor = str(round(entrada-(entrada*0.05),2))

if len(valor.split('.')[1]) == 1:
    valor += '0'

print(f'Esse produto custara R$:{valor} com 5% de desconto')