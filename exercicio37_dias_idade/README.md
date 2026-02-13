# Exercício – Conversão de Idade de Dias para Anos, Meses e Dias

Neste exercício, o programa lê a idade de uma pessoa expressa em dias e a converte para anos, meses e dias.

## Conceitos Utilizados

- Entrada de dados com `input()`
- Conversão de tipos (`int`)
- Operações matemáticas básicas (divisão inteira e resto da divisão)
- Uso de variáveis
- Saída de dados com `print`
- Formatação de saída com f-string

## Lógica do Exercício

1. O usuário informa a idade em dias.
2. O programa calcula a quantidade de anos dividindo o total de dias por 365 (dias em um ano).
3. O programa calcula a quantidade de meses restantes dividindo o resto da divisão dos dias por 365 por 30 (dias em um mês).
4. O programa calcula os dias restantes usando o resto da divisão do valor anterior por 30.
5. O valor convertido em anos, meses e dias é exibido na tela.
