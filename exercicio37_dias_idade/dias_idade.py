# Ler uma idade de uma pessoa em dias e expressar em anos, meses e dias

#Entrada
total_dias = int(input('Digite a idade em dias: '))

#Processamento
anos = total_dias // 365
resto1 = total_dias % 365
meses = resto1 // 30
dias = resto1 % 30

#Saída
print(f'A idade é:{anos} anos, {meses} meses e {dias} dias')


