#Ler 2 números, calcular e escrever a divisão da soma pela subtração dos números.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = soma / subtracao
print(f"A divisao da soma pela subtração dos números é: {divisao}")
