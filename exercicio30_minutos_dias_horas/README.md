# Exercício – Conversão de Minutos para Dias, Horas e Minutos Restantes

Neste exercício, o programa lê um valor inteiro informado em minutos e calcula quantos dias, horas e minutos esse valor representa.

## Conceitos Utilizados

- Entrada de dados com `input()`
- Conversão de tipos (`int`)
- Operações matemáticas básicas (divisão inteira e resto da divisão)
- Uso de variáveis
- Saída de dados com `print`
- Formatação de saída com f-string

## Lógica do Exercício

1. O usuário informa um valor inteiro representando a quantidade total de minutos.
2. O programa calcula a quantidade de dias dividindo os minutos por 1440 (quantidade de minutos em um dia).
3. O programa calcula as horas restantes dividindo o resto da divisão dos minutos por 1440 por 60 (quantidade de minutos em uma hora).
4. O programa calcula os minutos restantes usando o resto da divisão do valor anterior por 60.
5. O valor convertido em dias, horas e minutos restantes é exibido na tela.
