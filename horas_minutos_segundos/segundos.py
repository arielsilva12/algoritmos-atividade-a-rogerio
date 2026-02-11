#Ler um valor inteiro que represente a quantidade de segundos, calcular e escrever quantas horas, minutos e segundos esse valor corresponde

#Entrada
segundos_totais = int(input('Digite o valor total de segundos: '))

#Processamento
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

#Saída
print(f'O valor total de segundos inseridos equivale a {horas} horas, {minutos} minutos e {segundos} segundos')