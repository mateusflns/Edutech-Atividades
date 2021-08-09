entrada = float(input('Insira quantos reais voce deseja converter em dolares R$:').replace(',','.'))
dolar = 5.30

quantia = round(float(entrada/dolar),2)

print(f'Voce pode comprar ${quantia} dolares com R$:{entrada}')