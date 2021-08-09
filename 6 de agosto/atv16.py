quilometrage = float(input('Quantos Kilometros foram percoridos pelo carro? :').replace(',','.'))
tempo = int(input('Por quantos dias esse carro foi alugado? :'))

preco = round(tempo*60+quilometrage*0.15,2)

print(f'O preco a pagar pelo aluguel desse carro e R$:{preco}')