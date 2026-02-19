# Exercícios - Aula 2

## Objetivo

Fixar o conteúdo aprendido sobre tipos de dados, conversão (casting), operadores aritméticos, de comparação e lógicos, atribuição composta e entrada do usuário com `input()`.

---

## Exercício 1: Reatribuição de variáveis

Simule um contador que começa em zero e é atualizado duas vezes (primeiro para 1, depois para 2). Ao final, o programa deve exibir o valor atual do contador.

---

## Exercício 2: Tipos e `type()`

Elabore quatro exemplos de dados que representem, na prática, um número inteiro, um número decimal, um texto e um valor verdadeiro ou falso (por exemplo, o resultado de uma comparação). Use `type()` para inspecionar e exibir o tipo de cada um e confira se corresponde ao que você esperava.

---

## Exercício 3: Conversão de tipos (casting)

Você tem duas strings que representam números: `"100"` e `"50"`. Sem alterar o fato de serem texto no código, observe o que acontece ao usar o operador `+` entre elas e, em seguida, o que acontece quando você as converte para inteiros e soma. Exiba ambos os resultados e explique a diferença.

---

## Exercício 4: Operadores aritméticos

A partir dos números 15 e 4, calcule e exiba a divisão comum, a divisão inteira e o resto da divisão. Em seguida, calcule e exiba 3 elevado à potência 4. Use os operadores aritméticos vistos na aula.

---

## Exercício 5: Precedência e parênteses

Escreva em Python a expressão `2 + 3 * 4` e a expressão `(2 + 3) * 4`. Execute-as, exiba os resultados e confira se a ordem em que as operações são feitas (com e sem parênteses) altera o valor final. Explique a diferença.

---

## Exercício 6: Atribuição composta

Simule um saldo inicial de 100. Aplique, em sequência e sobre a mesma variável, um acréscimo de 25, uma retirada de 30 e a duplicação do valor restante, usando apenas operadores de atribuição composta. Ao final, exiba o saldo resultante.

---

## Exercício 7: Operadores de comparação

Defina dois números em variáveis e exiba o resultado (True ou False) das comparações: um é maior que o outro, um é menor ou igual ao outro, são iguais e são diferentes. Use os operadores de comparação da aula.

---

## Exercício 8: Operadores lógicos

Imagine um cenário com idade de uma pessoa (17 anos), se ela tem ingresso, se é feriado e a idade de um idoso (66 anos). Usando `and`, `or` e `not`, exiba o resultado lógico de: (1) a pessoa pode entrar somente se tiver 18 anos ou mais e tiver ingresso; (2) há direito a desconto se for feriado ou a pessoa tiver 65 anos ou mais; (3) a negação de "ter 18 anos ou mais". Ajuste depois alguns valores (por exemplo, a idade) e observe como os resultados mudam.

---

## Exercício 9: `input()` e casting

Escreva um programa que pergunte o nome e a idade do usuário, armazene as respostas (lembre-se de converter a idade para o tipo adequado aos cálculos) e exiba uma mensagem de saudação que inclua nome e idade. Use f-string para formatar a saída.

---

## Exercício 10: Calculadora com entrada

Escreva um programa que leia dois números (permitindo decimais), calcule a soma, a subtração, o produto e a divisão do primeiro pelo segundo e exiba cada resultado em uma linha, com um rótulo que indique qual operação foi feita. Assuma que o usuário não digitará 0 como segundo número (divisão por zero será tratada em aulas futuras).

---

## Exercício 11: Maior de idade

Leia a idade do usuário e exiba o resultado de verificar se ela é maior ou igual a 18 (True ou False). Não use `if`: apenas calcule a expressão e imprima o valor booleano.

---

## Exercício 12: Tudo junto

Escreva um programa que leia o preço unitário de um produto e a quantidade comprada, calcule o total a pagar e exiba esse valor formatado (por exemplo, "Total: R$ ..."). Inclua também a exibição do tipo de uma das variáveis lidas, usando `type()`, para revisar tipos.

**Desafio:** calcule o total usando atribuição composta: comece com `total = preco` e depois faça `total *= quantidade` e imprima o resultado.

---

## Dicas importantes

- `input()` sempre retorna string; use `int()` ou `float()` para cálculos.
- Divisão com `/` retorna float; com `//` retorna inteiro (truncado).
- Comparações e combinações com `and`/`or`/`not` resultam em `True` ou `False`.
- Na dúvida sobre ordem das operações, use parênteses.
- Evite digitar letras quando o programa espera número (para não gerar `ValueError`); isso será tratado em aulas futuras.

---

## Desafio extra (opcional)

Escreva um programa que leia o ano de nascimento e o ano atual (como inteiros), calcule a idade aproximada e exiba esse valor. Em seguida, exiba o resultado de verificar se a pessoa tem 18 anos ou mais (True ou False), usando apenas operadores e sem usar `if`.