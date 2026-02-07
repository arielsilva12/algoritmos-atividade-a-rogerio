# Ler um numero inteiro (3 ígitos) e escrever o número inverso.

numero = int(input("Digite um número inteiro de 3 dígitos: "))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
inverso = unidade * 100 + dezena * 10 + centena
print(F"O número inverso é: {inverso}")
