# Escrever um algoritmo, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escrever a distância entre eles, conforme a fórmula: D = [(x2-x1)² + (y1 - y2)²]¹/²

#Entrada
x1 = int(input('Insira o valor de x1, que irá compor o eixo das abscissas do ponto 1: '))
y1 = int(input('Insira o valor de y1, que irá compor o eixo das ordenadas do ponto 1: '))
x2 = int(input('Insira o valor de x2, que irá compor o eixo das abscissas do ponto 2: '))
y2 = int(input('Insira o valor de y2, que irá compor o eixo das ordenadas do ponto 2: '))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

#Saída
print(f'A distância entre os dois pontos 1 e 2 é igual a {d:.2f}')
