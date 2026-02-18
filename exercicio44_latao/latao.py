#Sabendo que latão é constituido de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário

#Entrada
quantidade_latao = float(input('Insira a quantidade total de latão(em kg): '))

#Processamento
cobre = quantidade_latao * 0.7
zinco = quantidade_latao * 0.3

#Saída
print(f'Em {quantidade_latao:.2f} kg de latão há {cobre:.2f} kg de cobre e {zinco:.2f} kg de zinco')

