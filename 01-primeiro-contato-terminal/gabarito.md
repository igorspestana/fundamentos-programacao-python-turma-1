# Gabarito — Exercícios da Aula 1

Este arquivo traz soluções de referência para `exercicios.md` (Aula 1).

Observações:
- Substitua os valores de exemplo pelos seus.
- As soluções focam em: variáveis, tipos de dados básicos, `print()`, f-strings e `str()` para concatenação.

---

## Exercício 1: Primeiro programa

```python
print("Olá, Python!")
```

---

## Exercício 2: Variáveis básicas

```python
name = "João"
age = 20
city = "São Paulo"

print(name)
print(age)
print(city)
```

---

## Exercício 3: Imprimindo variáveis juntas

```python
name = "João"
age = 20
city = "São Paulo"

print(name, age, city)
```

---

## Exercício 4: Formatação com f-string

```python
name = "João"
age = 20
city = "São Paulo"

print(f"Meu nome é {name}, tenho {age} anos e moro em {city}.")
```

---

## Exercício 5: Informações pessoais

```python
pet = "nenhum"
food = "pizza"
hobby = "ler"

print(f"Gosto de {hobby}, adoro comer {food} e meu animal favorito é {pet}.")
```

---

## Exercício 6: Números e texto

```python
siblings = 2
pets = 0

print(f"Tenho {siblings} irmão(s) e {pets} pet(s).")
```

---

## Exercício 7: Concatenação com +

```python
part1 = "Python é uma "
part2 = "linguagem de "
part3 = "programação."

print(part1 + part2 + part3)
```

---

## Exercício 8: Conversão de tipos (apenas +, sem f-string)

```python
birth_year = 2005
current_year = 2026
age = current_year - birth_year

print("Eu nasci em " + str(birth_year) + " e tenho " + str(age) + " anos.")
```

---

## Exercício 9: Múltiplas mensagens

```python
print("Estou aprendendo Python!")
print("Python é divertido!")
print("Vou me tornar um programador!")
```

---

## Exercício 10: Informações completas

### Versão A (um `print()` por linha)

```python
name = "João"
age = 20
city = "São Paulo"
job = "estudante"

print(f"Nome: {name}")
print(f"Idade: {age} anos")
print(f"Cidade: {city}")
print(f"Profissão: {job}")
```

### Desafio (um único `print()` com `\n`)

```python
name = "João"
age = 20
city = "São Paulo"
job = "estudante"

print(
    f"Nome: {name}\n"
    f"Idade: {age} anos\n"
    f"Cidade: {city}\n"
    f"Profissão: {job}"
)
```

---

## Desafio extra (opcional): Receita de bolo

```python
recipe_name = "Bolo de chocolate"
prep_time_minutes = 45
main_ingredients_count = 6

print(
    f"Receita: {recipe_name} | "
    f"Tempo: {prep_time_minutes} minutos | "
    f"Ingredientes: {main_ingredients_count} principais"
)
```

