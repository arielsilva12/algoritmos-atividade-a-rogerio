# Ler um número inteiro de 4 dígitos, calcular e escrever a soma dos elementos que o compõem

#Entrada
numero = int(input('Digite um número inteiro de 4 dígitos: '))

#Processamento
milhar = numero // 1000
resto1 = numero % 1000
centena = resto1 // 100
resto2 = resto1 % 100
dezena = resto2 // 10
unidade = resto2 % 10
soma = milhar + centena + dezena + unidade

#Saída
print(f'A soma dos elementos do número {numero} é igual a {soma}')
