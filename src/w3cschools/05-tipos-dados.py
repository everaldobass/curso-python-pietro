# Python Tipos de dados
"""
Tipos de dados integrados
Na programação, o tipo de dados é um conceito importante.
Variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes.
Python possui os seguintes tipos de dados integrados por padrão, nestas categorias:


Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de sequência:	list, tuple, range
Tipo de mapeamento:	dict
Tipos de conjuntos:	set, frozenset
Tipo Booleano:	bool
Tipos binários:	bytes, bytearray, memoryview
Nenhum Tipo:	NoneType
"""

# Obtendo o tipo de dados
texto = "\nObtendo o tipo de dados"
print(type(texto))

# Tipos numéricos

## 1. Tipos Numéricos
#Utilizados para cálculos matemáticos e armazenamento de valores quantitativos. 

## int (Inteiros): Números sem casas decimais, positivos ou negativos.
idade = 25

# float (Ponto Flutuante): Números com casas decimais.
preco = 19.99
# complex (Complexos): Números com uma parte real e uma parte imaginária (representada por j).
complexo = 3 + 5j 

# 2. Tipos de Texto
# str (String): Cadeias de caracteres delimitadas por aspas simples (') ou duplas (").
texto = "Python tipo texto" 

# 3. Tipos Booleanos
# bool (Booleano): Representa valores lógicos: Verdadeiro (True) ou Falso (False).
ligado = True
desligado = False 

## 4. Tipos de Sequência (Coleções)
# Estruturas que permitem armazenar múltiplos itens em uma única variável. 

# list (Lista): Coleção ordenada e mutável (pode ser alterada após a criação).
lista_frutas = ["maçã", "banana", "uva"]

# tuple (Tupla): Coleção ordenada, mas imutável (não pode ser alterada).
coordenadas = (10, 20)

# range: Gera uma sequência de números, comum em loops.
range_numeros = range(5) #(gera 0, 1, 2, 3, 4) 

# 5. Tipos de Mapeamento e Conjuntos
# dict (Dicionário): Coleção de pares chave-valor, onde cada valor é acessado por uma chave única.
dicionario_usuario = {"nome": "Ana", "idade": 30}

# set (Conjunto): Coleção não ordenada de itens únicos (sem duplicatas).
set_conjunto_cores = {"azul", "verde", "vermelho"} 
