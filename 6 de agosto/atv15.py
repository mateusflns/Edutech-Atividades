entrada = float(input('Digite uma temperatura em celcius para ser convertida em farenheit :').replace(',','.'))
valor = str(round(((9*entrada)/5)+32,2))

print(f'{entrada}°C equivale a {round(((9*entrada)/5)+32,2)}°F')