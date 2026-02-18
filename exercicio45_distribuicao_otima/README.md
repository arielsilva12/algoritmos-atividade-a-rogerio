# Exercício – Distribuição Ótima de Notas em Caixa Eletrônico

Neste exercício, o programa lê um valor inteiro correspondente a uma quantia em dinheiro para saque e calcula a quantidade de notas necessárias para compor esse valor, utilizando o critério da distribuição ótima, ou seja, minimizando a quantidade de notas de menor valor.

## Conceitos Utilizados
- Entrada de dados com `input()`
- Conversão de tipos (`int`)
- Divisão inteira (`//`)
- Operador resto (`%`)
- Uso de variáveis
- Saída de dados com `print`
- Decomposição de valores monetários

## Lógica do Exercício
1. O usuário informa o valor total a ser sacado
2. O programa calcula a quantidade máxima possível de notas de 50 reais
3. O restante do valor é utilizado para calcular a quantidade de notas de 10 reais
4. O processo é repetido para notas de 5 reais
5. O valor restante é convertido em moedas de 1 real
6. A quantidade de cada tipo de nota (ou moeda) é exibida na tela
