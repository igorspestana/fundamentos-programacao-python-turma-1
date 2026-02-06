# Exercícios - Encontro 1

## Objetivo
Fixar o conteúdo aprendido sobre variáveis, tipos de dados e a função `print()`.

---

## Exercício 1: Primeiro programa
Crie um programa que imprima na tela a mensagem: "Olá, Python!"

---

## Exercício 2: Variáveis básicas
Crie variáveis para armazenar:
- Seu nome
- Sua idade
- Sua cidade

Depois, imprima cada variável em uma linha separada usando `print()`.

---

## Exercício 3: Imprimindo variáveis juntas
Usando as variáveis do exercício anterior, imprima todas as informações em uma única linha usando vírgulas.

Exemplo de saída esperada:
```
João, 20, São Paulo
```

---

## Exercício 4: Formatação com f-string
Usando f-string, crie uma mensagem que diga:
"Meu nome é [seu nome], tenho [sua idade] anos e moro em [sua cidade]."

Substitua os valores entre colchetes pelas suas variáveis.

---

## Exercício 5: Informações pessoais
Crie variáveis para armazenar:
- Seu animal de estimação favorito (ou "nenhum" se não tiver)
- Sua comida favorita
- Seu hobby favorito

Imprima uma frase completa usando f-string no formato:
"Gosto de [hobby], adoro comer [comida] e meu animal favorito é [animal]."

---

## Exercício 6: Números e texto
Crie variáveis numéricas para:
- Quantidade de irmãos que você tem
- Quantidade de pets que você tem (ou 0 se não tiver)

Imprima usando f-string:
"Tenho [quantidade] irmão(s) e [quantidade] pet(s)."

---

## Exercício 7: Concatenação com +
Usando o operador `+` para concatenar strings, crie uma mensagem que diga:
"Python é uma linguagem de programação."

Dica: você pode dividir a frase em partes e concatená-las.

---

## Exercício 8: Conversão de tipos
Crie três variáveis numéricas:
- O ano em que você nasceu
- O ano atual
- Sua idade

Imprima usando apenas concatenação com `+` (sem f-string):
"Eu nasci em [ano] e tenho [idade] anos."

---

## Exercício 9: Múltiplas mensagens
Crie um programa que imprima três mensagens diferentes, cada uma em uma linha:
1. "Estou aprendendo Python!"
2. "Python é divertido!"
3. "Vou me tornar um programador!"

---

## Exercício 10: Informações completas
Crie um programa completo que:
1. Armazene seu nome, idade, cidade e profissão (ou "estudante") em variáveis
2. Imprima uma apresentação completa usando f-string. Use um `print()` para cada linha, no formato:

```
Nome: [nome]
Idade: [idade] anos
Cidade: [cidade]
Profissão: [profissão]
```

**Desafio:** refaça a impressão usando apenas um `print()`, mantendo o mesmo formato (uma informação por linha). Dica: use `\n` dentro da string para quebrar linha.

---

## Dicas importantes

- Texto (strings) sempre deve estar entre aspas: `"texto"`
- Números não devem estar entre aspas: `20` (não `"20"`)
- Para concatenar texto e números com `+`, use `str()` para converter números em texto
- F-strings são mais fáceis: `f"Texto {variavel}"`
- Sempre feche as aspas que você abrir
- Use comentários `#` para explicar seu código se necessário

---

## Desafio extra (opcional)

Crie um programa que simule uma receita de bolo. Use variáveis para:
- Nome da receita
- Tempo de preparo (em minutos)
- Quantidade de ingredientes principais (número)

Imprima uma mensagem formatada como:
"Receita: [nome] | Tempo: [tempo] minutos | Ingredientes: [quantidade] principais"
