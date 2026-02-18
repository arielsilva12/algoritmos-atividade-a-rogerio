#Algoritmo para gerencia os saques de um caixa eletrônico utilizando o critério da "Distribuição Ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível

#Entrada
quantia_solicitada = int(input('Insira a quantidade total de dinheiro para saque: '))

#Processamento
notas_50 = quantia_solicitada // 50
resto1 = quantia_solicitada % 50
notas_10 = resto1 // 10
resto2 = resto1 % 10
notas_5 = resto2 // 5
resto3 = resto2 % 5
notas_1 = resto3 // 1

#Saída
print(f'A distribuição das notas para saque ficou da seguinte maneira: {notas_50} notas de 50 reais, {notas_10} notas de 10 reais, {notas_5} notas de 5 reais e {notas_1} moedas de 1 real')

