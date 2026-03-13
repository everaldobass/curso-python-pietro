"""
Especifique um tipo de variável
Pode haver momentos em que você queira especificar um tipo em uma variável. Isso pode ser feito com fundição. Python é uma linguagem orientada a objetos e, como tal, usa classes para definir tipos de dados, incluindo seus tipos primitivos.
A conversão em python é, portanto, feita usando funções construtoras:
int() - constrói um número inteiro a partir de um literal inteiro, um literal flutuante (removendo todos os decimais) ou uma string literal (desde que a string represente um número inteiro)
flutuador() - constrói um número float a partir de um literal inteiro, um literal float ou um literal de string (desde que a string represente um float ou um inteiro)
str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais inteiros e literais flutuantes
"""

# Especificando um tipo de variável
x = int(1)    # x será 1
y = float(2.8)  # y será 2.8
z = str("3")  # z será '3'

print(type(x))
print(type(y))
print(type(z))