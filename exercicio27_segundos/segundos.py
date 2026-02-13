#Ler um número inteiro de segundos, calcular e escrever quantas horas, quantos minutos e quantos segundos ele corresponde

#Entrada
segundos_totais = int(input('Digite a quantidade total de segundos: '))

#Processamento
horas = segundos_totais // 3600
resto = segundos_totais % 3600
minutos = resto // 60
segundos = resto % 60

#Saída
print(f'A quantidade total de segundos inseridas correspondem a {horas} horas, {minutos} minutos e {segundos} segundos')
