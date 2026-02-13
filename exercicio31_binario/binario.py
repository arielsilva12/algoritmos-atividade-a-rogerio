#Ler um número inteiro (4 dígitos binário), calcular e escrever o equivalente na base decimal

#Entrada
binario = int(input('Digite um número inteiro de 4 dígitos binário: '))

#Processamento
b3 = binario // 1000
resto1 = binario % 1000
b2 = resto1 // 100
resto2 = resto1 % 100
b1 = resto2 // 10
b0 = resto2 % 10
decimal = b3 * 8 + b2 * 4 + b1 * 2 + b0 * 1

#Saída
print(f'O número binário {binario} é equivalente ao número decimal {decimal}.')


