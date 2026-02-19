#--------------------------------
# Bloco 1: Alterando valores (reatribuição)

# Atividade 1: Atualizar dados

idade = 31
print("Agora tenho", idade, "anos")  # Agora tenho 31 anos

nome = "Maria"
print("Agora meu nome é", nome)  # Agora meu nome é Maria

#--------------------------------
# Bloco 2: Tipos de dados

# Atividade 1: Texto vs número

print(type(nome))   # <class 'str'>
print(type(idade))  # <class 'int'>

#--------------------------------
# Bloco 3: Tipos que você vai usar hoje (int / float / str / bool)

# Atividade 1: Exemplos diretos de tipos
itens = 3
preco = 19.90
nome = "Maria"
idade = 20
e_maior = idade >= 18

print(itens, type(itens))      # 3 <class 'int'>
print(preco, type(preco))      # 19.9 <class 'float'>
print(nome, type(nome))        # Maria <class 'str'>
print(e_maior, type(e_maior))  # True <class 'bool'>

#--------------------------------
# Bloco 4: Conversão de tipos (casting)

idade = 31
idade_como_texto = str(idade)
print("Como texto:", idade_como_texto)  # Como texto: 31
print(type(idade_como_texto))           # <class 'str'>

# Strings vs números no "+"
numero1 = "10"
numero2 = "20"

print(type(numero1))  # <class 'str'>
print(type(numero2))  # <class 'str'>

soma_texto = numero1 + numero2
print(soma_texto)  # "1020" (concatenação de strings)

soma_numeros = int(numero1) + int(numero2)
print(soma_numeros)  # 30 (soma numérica)

#--------------------------------
# Bloco 5: Operadores aritméticos

print(10 + 3)     # 13 (adição)
print(10 - 3)     # 7 (subtração)
print(10 * 3)     # 30 (multiplicação)
print(10 / 3)     # 3.3333333333333335 (divisão float)
print(10 // 3)    # 3 (divisão inteira)
print(10 % 3)     # 1 (resto/módulo)
print(2 ** 3)     # 8 (potenciação)

# Parênteses ajudam a controlar a ordem das operações
print((2 + 3) * 4)  # 20
print(2 + (3 * 4))  # 14

#--------------------------------
# Bloco 6: Operadores de atribuição compostos (+=, -=, *=, /=)

# Equivalente a: x = x + valor
x = 10
x += 3
print(x)  # 13

x = 10
x -= 4
print(x)  # 6

x = 10
x *= 2
print(x)  # 20

x = 10
x /= 2
print(x)  # 5.0 (divisão retorna float)

#--------------------------------
# Bloco 7: Operadores de comparação (booleanos)

print(10 > 3)   # True
print(10 >= 10) # True
print(10 == 10) # True
print(10 != 5)  # True
print(3 < 2)    # False

#--------------------------------
# Bloco 8: Operadores lógicos (and / or / not)

"""
+ and + = +
+ and - = -
- and + = -
- and - = -

+ or + = +
+ or - = +
- or + = +
- or - = -

not + = -
not - = +
"""

idade = 20
tem_documento = True
tem_permissao = False

print(idade >= 18)                    # True
print(not idade >= 18)                # False
print((idade >= 18) and tem_documento)  # True
print((idade >= 18) and tem_permissao)  # False
print((idade >= 18) or tem_permissao)   # True
print(not tem_documento)              # False
print(not tem_permissao)              # True

#--------------------------------
# Bloco 9: input() retorna str (e precisa de casting)

# Atenção: rodar este arquivo vai pausar e esperar entrada aqui.
idade_digitada = input("Digite sua idade: ")
print(type(idade_digitada))  # <class 'str'>

idade_usuario = int(idade_digitada)
print("Daqui a 1 ano você terá", idade_usuario + 1)  # e.g. Daqui a 1 ano você terá 32 (depends on input)

preco_digitado = input("Digite um preço (ex.: 19.90): ")
preco = float(preco_digitado)
print("O dobro do preço é", preco * 2)  # e.g. O dobro do preço é 39.8 (depends on input)

# Python não permite somar int e str com "+"
# Descomente para ver o erro:
# print(int(numero1) + numero2)
