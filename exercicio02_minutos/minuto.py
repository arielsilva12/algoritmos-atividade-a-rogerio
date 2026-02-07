# Ler um valor em horas e um valor em minutos, calcular o total 
#de minutos e exibir o resultado.

#Entrada
horas = int(input("Digite o valor em horas: "))
minutos = int(input("Digite o valor em minutos: "))

#Processamento
total_minutos = horas * 60 + minutos

#Saída
print(f'O total de minutos é: {total_minutos}')
