#Ler um valor em quilograma, calcular e escrever o equivalente em gramas.

#Entrada
quilograma = float(input('Digite o valor do peso em quilogramas (kg): '))

#Processamento
gramas = quilograma * 1000

#Saída
print(f'O valor correspondente em gramas(g) é: {gramas:.0f} g')
