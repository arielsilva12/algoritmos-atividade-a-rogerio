#Ler um número inteiro (3 dígitos), calcular e escrever a soma do número com o seu inverso

#Entrada
numero = int(input('Digite um número inteiro de 3 dígitos: '))

#Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade * 100 + dezena * 10 + centena
soma = numero + inverso

#Saída
print(f'A soma do número {numero} com o seu inverso {inverso} é igual a {soma}')
