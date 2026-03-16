# Python Conjuntos
"""
Conjuntos são usados para armazenar vários itens em uma única variável.
Um conjunto é uma coleção desordenada e imutável.
Os conjuntos são escritos com chaves.
"""

# Criando um conjunto
frutas = {"maçã", "banana", "laranja"}
print(frutas)

# Verificando se um item está no conjunto
print("maçã" in frutas)  # Retorna True, porque "maçã" está no conjunto
print("uva" in frutas)   # Retorna False, porque "uva" não está no conjunto


# Tamanho do conjunto
print(len(frutas))  # Retorna o número de itens no conjunto
# Adicionando itens ao conjunto
frutas.add("abacaxi")
print(frutas)  # Retorna o conjunto com o novo item
# Removendo itens do conjunto
frutas.remove("banana")
print(frutas)  # Retorna o conjunto sem o item removido

# Juntando conjuntos
conjunto1 = {"a", "b", "c"} 
conjunto2 = {1, 2, 3}
conjunto_junto = conjunto1.union(conjunto2)
print(conjunto_junto)  # Retorna o conjunto com os itens de ambos os conjuntos  

# Listando métodos de conjunto
print(dir(frutas))  # Retorna uma lista de métodos disponíveis para conjuntos       
# Conjuntos não permitem itens duplicados

frutas.add("maçã")  # Tentar adicionar "maçã" novamente
print(frutas)  # Retorna o conjunto sem itens duplicados
# Conjuntos são desordenados, não é possível acessar itens por índice
# print(frutas[0])  # Isso causará um erro, porque conjuntos não são ordenados



