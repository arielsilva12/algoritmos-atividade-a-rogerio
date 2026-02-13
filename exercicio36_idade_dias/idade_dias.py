# Ler a idade de uma pessoa em anos, meses e dias e escrever apenas em dias

#Entrada
anos = int(input('Digite a idade em anos: '))
meses = int(input('Digite a quantidade de meses:'))
dias = int(input('Digite a quantidade de dias:'))

#Processamento
total_dias = anos * 365 + meses * 30 + dias

#Saída
print(f'A idade total em dias é: {total_dias} dias.')
