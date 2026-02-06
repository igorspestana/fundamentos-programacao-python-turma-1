# Encontro 1 — Fundamentos + Primeiro Código em Python

> **Objetivo da aula:**
> Configurar o ambiente de desenvolvimento para programar em Python.
> Entender *o que é programação*, *o que estamos fazendo quando escrevemos código* e **rodar nosso primeiro programa sozinho**.

---

## 1. Preparar o ambiente

⚠️ Essa parte SEMPRE leva mais tempo do que o planejado. Aceite isso.

### Instalar Python

No site oficial do Python, [https://www.python.org/downloads/](https://www.python.org/downloads/), você pode baixar o instalador do Python.

> Atualmente o link para download do instalador do Python 3.14.3 versão para Windows é: 
[https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe](https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe). 
> Esse link pode ser alterado, então sempre verifique a versão mais recente.
>
> Para outros sistemas operacionais, como Linux e macOS, o processo é similar, mas o link de download é diferente. Verifique a seção de downloads do site oficial do Python para mais informações.

Execute o instalador e siga as instruções. Marque a opção "Add Python to PATH" para que o Python seja adicionado ao PATH do sistema. Dessa forma, você poderá executar o Python diretamente no terminal.

Abra o terminal e verifique se o Python foi instalado corretamente executando o comando:

```bash
python --version
```

Se o comando acima mostrar a versão do Python instalada, o Python foi instalado corretamente.

### Instalar VS Code

O VS Code (Visual Studio Code) é um programa usado para escrever, editar e executar códigos de computador. É uma junção de editor de texto, navegador de arquivos e terminal.

No site oficial do VS Code, [https://code.visualstudio.com/download](https://code.visualstudio.com/download), você pode baixar o instalador do VS Code..

Execute o instalador e siga as instruções. Dica: marque a opção “Open with Code” para que o VS Code apareça no menu de contexto ao clicar com o botão direito do mouse em arquivos ou pastas.

---

## 2. Introdução ao Terminal

### O que é terminal?

> “Uma forma de conversar com o computador por texto.”

### Por que usar terminal?

* Mais controle
* Você vê o que realmente acontece
* Funciona em qualquer computador

Comandos básicos:

```bash
ls - listar arquivos e pastas
cd - mudar de diretório
pwd - mostrar o diretório atual
```

---

## 3. Conceitos Fundamentais

### O que é um programa?

> “Um programa é uma lista de instruções que o computador segue exatamente, sem pensar.”

Exemplo humano:

* Receita de bolo
* Manual de montagem

💡 Ideia chave:

> “Computadores são rápidos, mas burros.”

### O que é algoritmo?

> “Um passo a passo para resolver um problema.”

Exemplo:

* Escovar os dentes
* Fazer café

### Diferença entre algoritmo e programa

* Algoritmo → ideia
* Programa → algoritmo escrito em uma linguagem de programação que o computador entende

### O que é linguagem de programação?

> “Uma forma padronizada de escrever instruções para o computador.”

É uma abstração criada para possibilitar a comunicação entre o programador e o computador.

*Abstração é o processo de esconder os detalhes de um sistema complexo, mostrando apenas as partes essenciais.*

### Linguagem natural vs linguagem de programação

* Português → ambíguo
* Python → exato

Exemplo:

> “Escreva a frase: 'Hello, world!'”
> vs
> `print("Hello, world!")`

### Níveis de linguagem de programação

Basicamente, existem duas categorias de linguagens de programação:

Uma **linguagem de alto nível** é feita para ser fácil de ler e escrever por pessoas, usando palavras próximas do inglês e escondendo os detalhes do funcionamento do computador.
Exemplos: Python, JavaScript, Java, C++, etc.
Uma **linguagem de baixo nível** é mais próxima da linguagem que o computador (linguagem de máquina) realmente entende, exigindo mais cuidado e conhecimento técnico, mas dando mais controle sobre a máquina.
Exemplos: Assembly, C, C++, etc.

* Linguagem de alto nível → mais próxima da linguagem humana
* Linguagem de baixo nível → mais próxima da linguagem de máquina
* Linguagem de máquina é a forma mais básica de programação, composta apenas por números (0 e 1), que o computador entende diretamente.

**Linguagem de alto nível (Python)**
```python
print("Hello, world!")
```

**Representação didática em linguagem de máquina:**
```
01001000 01100101 01101100 01101100 01101111 00101100
00100000 01110111 01101111 01110010 01101100 01100100 00100001
```

#### Curiosidade (não é obrigatório entender, mas é interessante):

Um computador funciona usando eletricidade, e a menor informação que ele entende é o **bit**, que pode ser **0 ou 1**.
O **bit** não é a eletricidade em si, mas a forma de representar se há energia passando (1) ou não (0), como um interruptor ligado ou desligado.
Bilhões desses pequenos interruptores, chamados transistores, trabalham juntos formando combinações de bits, que permitem ao computador representar números, letras, imagens e executar programas.

**Analogia para ilustrar:**

> Imagine uma parede com bilhões de interruptores:
>
> Ligado = 1
> Desligado = 0
>
> Um único interruptor não diz muita coisa, mas vários interruptores ligados e desligados em sequência conseguem representar letras, números e até imagens. O computador faz isso em altíssima velocidade.

ou 

> O computador funciona parecido com o código Morse:
>
> Um sinal curto ou ausência de sinal = 0
> Um sinal longo ou presença de sinal = 1
>
> Sozinhos, os sinais não dizem nada, mas combinações deles formam mensagens completas.
> O computador só troca “pontos e traços” por energia ligada ou desligada.


### O que é sintaxe?

> “O conjunto de regras que dizem como escrever corretamente um comando em uma linguagem de programação.”

Exemplo em diferentes linguagens de programação:

**Em Java:**
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

**Em JavaScript:**
```javascript
console.log("Hello, world!");
```

**Em Python:**
```python
print("Hello, world!")
```


💡 Ideia chave:

> “Computador não entende intenção, só sintaxe.”

### Linguagem interpretada vs compilada

Uma **linguagem interpretada** é lida e traduzida em linguagem de máquina na hora da execução, linha por linha, por um interpretador.
Uma **linguagem compilada** é transformada antes de rodar em um arquivo de linguagem de máquina (ou muito próxima disso), usando um compilador.

* Linguagem interpretada → traduz linha por linha
* Linguagem compilada → traduz tudo antes

### Python é interpretado

> “Você escreve e executa na hora.”

### Java é compilado

> “Você compila e executa depois.”

#### Curiosidade:
Quando você instala o Python, não está instalando só a linguagem, mas também o programa que a executa (chamado de interpretador ou motor) e um conjunto de ferramentas prontas para usar.

O principal é o interpretador Python, que é o programa que lê seu código e executa as instruções no computador. Junto com ele vem a biblioteca padrão, que já traz várias funções prontas (para arquivos, datas, matemática, internet etc.), além do pip, que serve para baixar novas bibliotecas, e um modo interativo, onde você pode testar comandos na hora.

* a linguagem são as regras;
* o motor é o interpretador;
* as ferramentas vêm junto na instalação.

### O que é dado e informação?

> “Dado é valor bruto. Informação é dado com significado.”

* **Dado** → valor bruto, isolado, sem contexto ou significado por si só, como um número ou uma palavra solta.
* **Informação** → dado depois de organizado e interpretado, ganhando sentido e utilidade

Exemplo:

* `10` → dado
* `"João"` → dado
* `João tem 10 anos` → informação

💡 Ideia chave:

> “Programar é transformar dados em informação.”

---

## 4. Introdução ao Python

### O que é Python?

Python é uma linguagem de programação de alto nível, criada para ser fácil de ler e escrever, usando uma sintaxe próxima da linguagem humana. Isso significa que quem programa em Python consegue entender o código quase como se estivesse lendo frases, o que reduz erros e facilita o aprendizado.

### Python é considerada uma linguagem inferior por ser fácil de ler e escrever?

Ser fácil de ler e escrever não torna uma linguagem pior, apenas significa que ela foi pensada para priorizar clareza e produtividade. Python troca um pouco de controle de baixo nível por menos complexidade, o que permite escrever programas mais rápido, com menos erros e manutenção mais simples. Ele não é “linguagem de iniciante”, é uma linguagem **bem projetada para resolver problemas reais com menos dor de cabeça**.


### O que dá pra fazer com Python?

* **Automatizar tarefas**: Renomear arquivos, gerar relatórios, ler planilhas, integrar sistemas.

* **Criar sites e APIs**: Backends de aplicações web, sistemas internos, serviços na nuvem.

* **Analisar dados**: Trabalhar com planilhas grandes, gráficos, estatísticas e relatórios.

* **Inteligência Artificial e Machine Learning**: Treinar modelos, criar chatbots, sistemas de recomendação.

* **Scripts e ferramentas internas**: Programas pequenos que ajudam equipes a ganhar tempo.

* **Jogos, desktop e testes**: Protótipos, ferramentas visuais e testes automatizados.

---

## 5. Primeiro código em Python

A partir daqui você vai escrever e executar código. Use o editor de texto para criar um arquivo `.py` e rode-o no terminal com `python nome_do_arquivo.py`.

### Primeiro programa

A função `print()` é uma das mais usadas em Python: ela exibe na tela o que você colocar entre os parênteses.

Exemplo:

```python
print("Hello, World!")
```

Ao executar o arquivo, o terminal mostra a mensagem entre aspas. As aspas fazem parte da sintaxe: elas indicam que aquilo é um **texto** (uma string). O computador não imprime as aspas, só o conteúdo.

### Erro faz parte

Quando algo está escrito de forma inválida, o Python para e mostra uma mensagem de erro. Um exemplo comum é esquecer de fechar as aspas:

```python
# print("Hello, World!)   # aspas não fechada = erro de sintaxe
```

Erros de sintaxe são úteis: eles apontam onde o código não está de acordo com as regras da linguagem. Ler a mensagem e a linha indicada ajuda a corrigir.

### Variáveis: guardando valores

Uma **variável** é um nome que você dá a um valor para usar depois. Em Python você cria atribuindo com `=`:

```python
nome = "João"
idade = 20
```

Regras práticas:

* **Texto** deve ficar entre aspas (simples ou duplas).
* **Números** não devem ficar entre aspas.

Assim o Python diferencia texto de número. Você pode exibir o conteúdo das variáveis com `print()`:

```python
print(nome)
print(idade)
```

### Usando variáveis junto com print

Há várias formas de mostrar variáveis e mensagens juntas.

**Vários argumentos separados por vírgula:**

```python
print(nome, idade)
print("Nome:", nome)
print("Idade:", idade)
```

A vírgula insere um espaço entre os valores.

**F-string (recomendado):**

Coloque um `f` antes das aspas e use chaves `{}` para incluir variáveis dentro do texto:

```python
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade}")
print(f"Meu nome é {nome} e tenho {idade} anos")
```

**Concatenação com `+`:**

É possível juntar textos com o sinal `+`. Porém, em Python não se concatena texto e número diretamente. É preciso converter o número em texto com `str()`:

```python
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos")
```

Se tentar `"texto " + idade` sem converter, o Python gera um erro. A função `str()` transforma o número em string para a concatenação funcionar.

Resumo:

* `print(nome, idade)` — vários valores separados por vírgula.
* `print(f"... {nome} ...")` — f-string, boa para frases com variáveis.
* `"texto " + str(numero)` — concatenação quando precisar juntar texto e número com `+`.