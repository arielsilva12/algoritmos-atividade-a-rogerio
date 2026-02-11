#Ler um valor inteiro de metros, calcular e escrever quantos quilômetros(km) e quantos metros ele corresponde.

#Entrada
valor_metros = int(input('Digite um valor inteiro de metros: '))

#Processamento
kilometros = valor_metros // 1000
metros = valor_metros % 1000

#Saída
print(f'O valor em metros fornecido equivale a {kilometros} km e {metros} m')