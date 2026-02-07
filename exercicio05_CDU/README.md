# Exercício – Soma da Centena, Dezena e Unidade (CDU)

Neste exercício, o programa lê um número inteiro de 3 dígitos e calcula a soma de seus dígitos: centena, dezena e unidade.

Embora o enunciado original não exigisse validação da entrada, foi implementada uma verificação adicional para garantir que o usuário informe corretamente um número com exatamente 3 dígitos, evitando resultados incorretos.

## Conceitos Utilizados
- Entrada de dados com `input()`
- Conversão de tipos (`int`)
- Operadores matemáticos:
  - Divisão inteira (`//`)
  - Módulo / resto da divisão (`%`)
- Estrutura condicional (`if`)
- Estrutura de repetição (`while`)
- Validação de dados de entrada
- Saída de dados com `print`
- Uso de f-string para formatação da saída

## Lógica do Exercício
1. O usuário informa um número inteiro
2. O programa verifica se o número possui exatamente 3 dígitos (entre 100 e 999)
   - Caso não seja válido, o programa solicita uma nova entrada
3. Após receber um número válido, o programa:
   - Calcula a centena, dezena e unidade
   - Soma esses três valores
4. O resultado da soma é exibido na tela
