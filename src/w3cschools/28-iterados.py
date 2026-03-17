# Iteradores Python
"""
Um iterador é um objeto que contém um número contável de valores.
Um iterador é um objeto que pode ser iterado, o que significa que você pode percorrer todos os valores.
Tecnicamente, em Python, um iterador é um objeto que implementa o protocolo iterador, que consiste nos métodos


Iterador vs Iterável
Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. Eles são iteráveis contêineres do qual você pode obter um iterador.

Todos esses objetos têm um iter() método usado para obter um iterador:
"""

mytuple = ("apple", "banana", "uva")
myut = iter(mytuple)

print(next(myut))


# Percorrendo um iterador
# Também podemos usar um for loop para iterar através de um objeto iterável:
mytuple = ("Banana", "Laranja", "Maça")

for x in mytuple:
    print(x)
