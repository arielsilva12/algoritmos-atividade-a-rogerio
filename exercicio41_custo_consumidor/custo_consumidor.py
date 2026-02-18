# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicado ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os imposto de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor

#Entrada
custo_fabrica = float(input('Qual o valor do custo de fábrica: '))

#Processamento
valor_distribuidor = 0.28 * custo_fabrica
valor_impostos = 0.45 * custo_fabrica
custo_consumidor = valor_distribuidor + valor_impostos + custo_fabrica

#Saída
print(f'O custo do consumidor é de R$ {custo_consumidor:.2f}')