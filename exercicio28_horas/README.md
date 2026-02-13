# Exercício – Conversão de Horas para Semanas, Dias e Horas Restantes

Neste exercício, o programa lê um valor inteiro informado em horas e calcula quantas semanas, dias e horas esse valor representa.

## Conceitos Utilizados

- Entrada de dados com `input()`
- Conversão de tipos (`int`)
- Operações matemáticas básicas (divisão inteira e resto da divisão)
- Uso de variáveis
- Saída de dados com `print`
- Formatação de saída com f-string

## Lógica do Exercício

1. O usuário informa um valor inteiro representando a quantidade total de horas.
2. O programa calcula a quantidade de semanas dividindo as horas por 168 (7 dias x 24 horas).
3. O programa calcula a quantidade de dias restantes dividindo o resto da divisão das horas por 168 por 24 (horas em um dia).
4. O programa calcula as horas restantes usando o resto da divisão do valor anterior por 24.
5. O valor convertido em semanas, dias e horas restantes é exibido na tela.
