# Ler um número inteiro (3 dígitos), calcular e escrever a soma dos seus dígitos.

numero = int(input("Digite um número inteiro de 3 dígitos: "))

while numero < 100 or numero > 999:
    print("Número inválido. Por favor, digite um número inteiro de 3 dígitos.")
    numero = int(input("Digite um número inteiro de 3 dígitos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

soma_digitos = centena + dezena + unidade
print(f"A soma dos dígitos é: {soma_digitos}")


        


