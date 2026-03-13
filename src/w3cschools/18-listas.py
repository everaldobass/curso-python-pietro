# Listas
"""
As listas são usadas para armazenar vários itens em uma única variável.
As listas são um dos 4 tipos de dados integrados em Python usados para armazenar coleções de dados, os outros 3 são Tupla, Definir, e Dicionário, todos com qualidades e usos diferentes.
As listas são criadas usando colchetes:
"""

# Criando uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Ordem de criação da lista
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Acessando itens da lista
print(frutas[0])  # Acessa o primeiro item da lista
print(frutas[1])  # Acessa o segundo item da lista
print(frutas[2])  # Acessa o terceiro item da lista 

# Modificando itens da lista
frutas[0] = "uva"
print(frutas)

# Adicionando itens à lista
frutas.append("abacaxi")
print(frutas)

# Removendo itens da lista
frutas.remove("banana")
print(frutas)

# Permitira duplicação de itens na lista
frutas.append("laranja")
print(frutas)

# Classificando itens da lista
frutas.sort()
print(frutas)

# Invertendo a ordem dos itens da lista
frutas.reverse()
print(frutas)

# Verificando se um item está na lista
print("maçã" in frutas)  # Retorna False, porque "maçã" foi modificado para "uva"
print("uva" in frutas)   # Retorna True, porque "uva" está na lista


# Tamanho da lista
print(len(frutas))  # Retorna o número de itens na lista 

# copiar uma lista
frutas_copia = frutas.copy()
print(frutas_copia)

# listar metodos de lista
print(dir(frutas))

# Juntando listas
frutas2 = ["melancia", "abacate"]
frutas.extend(frutas2)
print(frutas)   


