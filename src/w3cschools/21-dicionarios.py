# Python Dicionários

""""
Dicionário
Dicionários são usados para armazenar valores de dados em pares chave:valor.
Um dicionário é uma coleção ordenada*, mutável e não permitir duplicatas.
"""

# Criando um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)

# Acessando itens do dicionário
print(pessoa["nome"])  # Acessa o valor associado à chave "nome"    
print(pessoa["idade"])  # Acessa o valor associado à chave "idade"
print(pessoa["cidade"])  # Acessa o valor associado à chave "cidade"

# Modificando itens do dicionário
pessoa["idade"] = 31
print(pessoa)  # Retorna o dicionário com o valor atualizado    


# Adicionando itens ao dicionário
pessoa["profissão"] = "Engenheiro"
print(pessoa)  # Retorna o dicionário com o novo item

# Removendo itens do dicionário
del pessoa["cidade"]
print(pessoa)  # Retorna o dicionário sem o item removido

# Verificando se uma chave está no dicionário
print("nome" in pessoa)  # Retorna True, porque "nome" é uma
print("cidade" in pessoa)  # Retorna False, porque "cidade" foi removida do dicionário

# Tamanho do dicionário
print(len(pessoa))  # Retorna o número de itens no dicionário

# Listando métodos de dicionário
print(dir(pessoa))  # Retorna uma lista de métodos disponíveis para dicionários


# Juntando dicionários
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario_junto = {**dicionario1, **dicionario2}
print(dicionario_junto)  # Retorna o dicionário com os itens de ambos os dicionários

# Dicionários não permitem chaves duplicadas, mas permitem valores duplicados
dicionario_junto["a"] = 10  # Modificando o valor da chave "a"
print(dicionario_junto)  # Retorna o dicionário com o valor atualizado

# Dicionários são ordenados a partir do Python 3.7, mas não é possível acessar itens por índice
# print(dicionario_junto[0])  # Isso causará um erro, porque dicionários não são acessados por índice, mas sim por chave    

