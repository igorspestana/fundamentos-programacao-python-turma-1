# Aula 2 — Operadores e Manipulação de Dados

> **Objetivo da aula:**
> Entender como o Python faz cálculos e comparações, como funciona a lógica booleana e como receber entrada do usuário com `input()` e converter tipos (casting) para trabalhar com números.

---

## 1) Revisão rápida: variáveis podem mudar

Em Python, uma variável é apenas um *nome* que aponta para um valor. Você pode **reatribuir**:

```python
idade = 31
idade = 32
```

Isso é normal e comum: programas funcionam atualizando valores ao longo do tempo.

---

## 2) Tipos que você vai usar hoje: `int`, `float`, `str`, `bool`

### O que é um tipo de dado?

> Tipos em programação são classificações formais que definem a natureza de um dado, determinando quais valores ele pode assumir, como é armazenado na memória e quais operações podem ser realizadas sobre ele.

Exemplos:
- `int` (inteiros)
- `float` (números decimais)
- `str` (texto)
- `bool` (verdadeiro/falso)

### `int` (inteiros)
Números inteiros:

```python
itens = 3
```

### `float` (números decimais)
Números com parte decimal:

```python
preco = 19.90
```

### `str` (texto)
Texto entre aspas:

```python
nome = "Maria"
```

### `bool` (verdadeiro/falso)
O resultado de comparações e lógica:

```python
e_maior = idade >= 18
```

Para inspecionar o tipo, use `type()`:

```python
print(type(idade))
print(type(preco))
print(type(nome))
print(type(e_maior))
```

---

## 3) Conversão de tipos (casting): `int()`, `float()`, `str()`

Exemplos:

```python
idade_texto = "31"
idade = int(idade_texto)           # 31

altura_texto = "1.75"
altura = float(altura_texto)       # 1.75

numero = 42
texto = str(numero)                # "42"
```

### Armadilha comum: soma de texto vs soma numérica

```python
print("10" + "20")        # "1020" (concatenação de strings)
print(int("10") + int("20"))  # 30 (soma numérica)
```

### Outra armadilha: conversão inválida
Se o usuário digitar algo que não é número, `int()` / `float()` vão gerar um erro (`ValueError`). Por enquanto, vamos só aprender *que isso pode acontecer* e evitar entrada inválida nos exercícios.

---

## 4) Operadores aritméticos (matemática)

Operadores aritméticos mais usados:

- `+` adição
- `-` subtração
- `*` multiplicação
- `/` divisão (o resultado costuma ser `float`)
- `//` divisão inteira (descarta a parte decimal)
- `%` módulo (resto da divisão)
- `**` potenciação

Exemplos:

```python
print(10 + 3)     # 13
print(10 - 3)     # 7
print(10 * 3)     # 30
print(10 / 3)     # 3.333...
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 3)     # 8
```

### Precedência de operadores (ordem das operações)
O Python segue as regras usuais da matemática:

- Parênteses primeiro: `( )`
- Depois potenciação: `**`
- Depois multiplicação/divisão: `*`, `/`, `//`, `%`
- Depois adição/subtração: `+`, `-`

Na dúvida, **use parênteses**.

---

## 5) Operadores de atribuição compostos

Em vez de escrever:

```python
idade = idade + 1
```

Você pode escrever:

```python
idade += 1
```

Outros comuns:

```python
total -= 5
preco *= 2
valor /= 10
```

---

## 6) Operadores de comparação (relacionais)

Comparações retornam um booleano (`True` ou `False`):

- `==` igual
- `!=` diferente
- `>` maior que
- `>=` maior ou igual
- `<` menor que
- `<=` menor ou igual

Exemplos:

```python
print(10 > 3)     # True
print(10 == 10)   # True
print(10 != 5)    # True
```

---

## 7) Operadores lógicos (lógica booleana)

Com valores booleanos você pode combinar condições:

- `and` (as duas condições precisam ser verdadeiras)
- `or` (pelo menos uma condição precisa ser verdadeira)
- `not` (inverte o booleano)

Usando **+** para “verdadeiro” e **-** para “falso”, o resultado de `and` e `or` fica assim:

| `and` | + | - |
|-------|---|---|
| **+** | + | - |
| **-** | - | - |

| `or`  | + | - |
|-------|---|---|
| **+** | + | + |
| **-** | + | - |

Para o `not`: **not + = -** e **not - = +** (ele só inverte).

Exemplos:

```python
idade = 20
tem_documento = True

pode_entrar = (idade >= 18) and tem_documento
print(pode_entrar)
```

Ideia importante:

> Um programa muitas vezes decide o que fazer com base em **condições**.

Na próxima aula você vai usar isso diretamente com `if` / `else`.

---

## 8) Recebendo entrada do usuário com `input()`

`input()` sempre retorna **texto** (`str`):

```python
nome = input("Qual é o seu nome? ")
print(type(nome))  # <class 'str'>
```

Para usar o valor como número, use `int()` ou `float()` como na seção de conversão de tipos (seção 3).

---

## 9) Juntando tudo: programas pequenos e úteis

### Exemplo 1: calculadora simples (dois números)

```python
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
print(f"Soma: {a + b}")
print(f"Produto: {a * b}")
```

### Exemplo 2: comparações + lógica

```python
idade = input("Digite a sua idade: ")
idade_permitida = 18

print(int(idade) >= idade_permitida)
```