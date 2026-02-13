#Ler um numero inteiro de dias, calcular e escrever quantas semanas e quantos dias ele corresponde

#Entrada
dias_totais = int(input('Digite a quantidade total de dias: '))

#Processamento
semanas = dias_totais // 7
dias = dias_totais % 7

#Saída
print(f'A quantidade de dias inseridas correspondem a {semanas} semanas e {dias} dias')
