#Ler um valor em Fahrenheit, calcular e escrever o valor correspondente em Celsius.

#Entrada
fahrenheit = float(input("Digite o valor da temperatura em Fahrenheit: "))

#Processamento
celsius = (fahrenheit - 32) * 5/9

#Saída
print(f'O valor correspondente em Celsius é: {celsius:.2f}°C')
