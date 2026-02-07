#Ler o salário de um trabalhador e escrevr o seu novo salário com um aumento de 25%

salario = float(input("Digite o salário do trabalhador: "))
novo_salario = salario + (salario * 0.25)
print(f"O novo salário do trabalhador é: {novo_salario} R$")
