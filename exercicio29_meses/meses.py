#Ler um número total de meses, calcular e escrever quantos anos e quantos meses ele corresponde

#Entrada
meses_totais = int(input('Digite a quantidade total de meses a serem convertidos: '))

#Processamento
anos = meses_totais // 12
resto = meses_totais % 12
meses_restantes = resto

#Saída
print(f'A quantidade de meses inseridas correspondem a {anos} anos e {meses_restantes} meses')
