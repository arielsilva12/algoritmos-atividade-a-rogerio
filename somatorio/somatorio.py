#Entrada
limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))

#Processamento
soma_dos_pares = limite_inferior + limite_superior
quantidade_de_pares = (limite_superior - limite_inferior + 1) / 2

somatorio = soma_dos_pares * quantidade_de_pares

#Saída
print(f"O somatório de {limite_inferior} até {limite_superior} é {somatorio}")
