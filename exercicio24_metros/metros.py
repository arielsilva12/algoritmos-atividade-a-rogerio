#Ler um valor em metros, calcular e escrever o equivalente em centímetros

#Entrada
valor_metro = float(input('Digite o valor em metros (m): '))

#Processamento
valor_cm = valor_metro * 100

#Saída
print(f'O valor fornecido em metros equivale a {valor_cm:.0f} centímetros')