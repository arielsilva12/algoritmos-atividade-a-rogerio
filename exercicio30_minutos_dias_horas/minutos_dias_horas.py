#Ler um número inteiro de minutos, calcular e escrever quantos dias, quantas horas e quantos minutos ele corresponde

#Entrada
minutos_totais = int(input('Insira a quantidade total de minutos: '))

#Processamento
dias = minutos_totais // 1440
resto = minutos_totais % 1440
horas = resto // 60
minutos = resto % 60

#Saída
print(f'A quantidade inserida corresponde a {dias} dias, {horas} horas e {minutos} minutos')