#--------------------------------
# Bloco 1: Primeiro programa

# Atividade 1: Primeiro programa

print("Hello, World!")

#--------------------------------
# Bloco 2: Erro faz parte

# Atividade 2: Quebrar de propósito

# Para ver o erro, descomente a linha abaixo e execute o código
#print("Hello, World!)

#--------------------------------
# Bloco 3: Variáveis na prática

# Atividade 3: Guardando valores

nome = "João"
idade = 20

"""
Texto deve ser entre aspas
Números não devem ser entre aspas
"""

print(nome)
print(idade)

# Atividade 4: Usando variáveis juntas

print(nome, idade)
print("Nome:", nome)
print("Idade:", idade)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade}")
print("Meu nome é", nome)
print("Tenho", idade, "anos")
print(f"Meu nome é {nome} e tenho {idade} anos")
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos")

"""
Python não permite concatenar texto e números diretamente utilizando o sinal de +.
Para fazer isso, é necessário converter o número para texto usando a função str().
"""

# Para ver o erro, descomente a linha abaixo e execute o código.
# print("Meu nome é " + nome + " e tenho " + idade + " anos")