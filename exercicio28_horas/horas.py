#Ler um número inteiro de horas, calcular e escrever quantas semanas, quantos dias e quantas horas ele corresponde

#Entrada
horas_totais = int(input('Digite a quantidade total de horas: '))

#Processamento
semanas = horas_totais // (7*24)
resto = horas_totais % (7*24)
dias = resto // 24
horas = resto % 24

#Saída
print(f'A quantidade total de horas equivalem a {semanas} semanas, {dias} dias e {horas} horas')