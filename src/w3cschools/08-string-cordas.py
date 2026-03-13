"""
Cordas
Strings em python são cercadas por aspas simples ou aspas duplas.
'olá' é o mesmo que "olá".
Você pode exibir uma string literal com o print() função:
"""
print("Strings em python são cercadas por aspas simples")
print('Strings em python são cercadas por aspas duplas')

"""
Você pode retornar um intervalo de caracteres usando a sintaxe slice.
Especifique o índice inicial e o índice final, separados por dois pontos, para retornar um parte da corda.
"""
b = "Hello, World!"
print(b[2:5])

# Modificar Strings
#Python possui um conjunto de métodos integrados que você pode usar em strings.

a = " letras maiúsculas! "
b = " letras minúsculas! "
c = " espaços em branco! "
d = " substituir texto! "
e = " dividir, texto! "

print(a.upper())  # retorna "Hello, World!" com todas as letras maiúsculas
print(b.lower())  # retorna "Hello, World!" com todas as letras minúsculas
print(c.strip())  # retorna "Hello, World!" sem espaços em branco no início ou no final
print(d.replace("H", "J"))  # retorna "Hello, World!" onde "H" é substituído por "J"
print(e.split(","))  # retorna uma lista onde a string é dividida em cada ocorrência de "," 
