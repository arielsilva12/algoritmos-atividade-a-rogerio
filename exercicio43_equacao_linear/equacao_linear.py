#Um sistema de equações lineares do tipo ax + by = c; dx + ey = f, pode ser resolvido segundo mostrado abaixo x = ce - bf / ae - bd; y = af - cd/ ae - bd. Escrever um algoritmo que leia os coeficientes aa,b,c,d,e e f, calcular e escrever os valores de x e y

#Entrada
a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))
d = int(input('Insira o valor de d: '))
e = int(input('Insira o valor de e: '))
f = int(input('Insira o valor de f: '))

#Processamento
x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

#Saída
print(f'O valor de x vale {x:.2f} e o valor de y vale {y:.2f}')