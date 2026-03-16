# Tuplas
"""
Tuplas são usadas para armazenar vários itens em uma única variável.
Tuple é um dos 4 tipos de dados integrados em Python usados para armazenar coleções de dados, os outros 3 são Lista, Definir, e Dicionário, todos com qualidades e usos diferentes.
Uma tupla é uma coleção ordenada e imutável.
As tuplas são escritas com colchetes redondos.
"""

# Criando uma tupla
frutas = ("maçã", "banana", "laranja")
print(frutas)

# Acessando itens da tupla
print(frutas[0])  # Acessa o primeiro item da tupla
print(frutas[1])  # Acessa o segundo item da tupla
print(frutas[2])  # Acessa o terceiro item da tupla


# Tuplas são imutáveis, não é possível modificar os itens da tupla
# frutas[0] = "uva"  # Isso causará um erro 
# Verificando se um item está na tupla
print("maçã" in frutas)  # Retorna True, porque "maçã" está na tupla
print("uva" in frutas)   # Retorna False, porque "uva" não está na tupla

# Tamanho da tupla
print(len(frutas))  # Retorna o número de itens na tupla


# Juntando tuplas
tupla1 = ("a", "b", "c")
tupla2 = (1, 2, 3)
tupla_junta = tupla1 + tupla2
print(tupla_junta)  # Retorna ("a", "b", "c", 1, 2, 3)

# Repetindo tuplas
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Retorna ("a", "b", "c", "a", "b", "c")


# Listando métodos de tupla
print(dir(frutas))  # Retorna uma lista de métodos disponíveis para tuplas  

# Contando itens em uma tupla
print(frutas.count("maçã"))  # Retorna o número de vezes que "maçã" aparece na tupla
print(frutas.count("uva"))   # Retorna o número de vezes que "uva" aparece na tupla 


# Encontrando o índice de um item na tupla
print(frutas.index("banana"))  # Retorna o índice de "banana" na tupla

# Tuplas com um único item
tupla_unica = ("maçã",)  # A vírgula é necessária para criar uma tupla com um único item
print(tupla_unica)  # Retorna ("maçã",)