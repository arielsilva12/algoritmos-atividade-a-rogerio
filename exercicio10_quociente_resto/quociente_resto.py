#Ler 2 número inteiro, calcular e escrever o quociente e o resto da divisão do primeirio pelo segundo

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
quociente = numero1 // numero2
resto = numero1 % numero2
print(f"O quociente da divisão é {quociente} e o resto é {resto}")
