"""
Números Python
Existem três tipos numéricos em Python:

int
float
complex
Variáveis de tipos numéricos são criadas quando você atribui um valor a elas:
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))  
print(type(z))

"""
Conversão de tipo
Você pode converter de um tipo para outro com o int(), float(), e complex() métodos:
"""

a = 3    # int
b = 3.8  # float
#c = 3j   # complex

# Conversão de tipo
a = float(a)  # converte int para float
b = int(b)    # converte float para int
#c = float(c)  # converte complex para float

print(type(a))
print(type(b))
# print(type(c))


""""
Número aleatório
Python não tem um random() função para faça um número aleatório, mas Python tem um módulo integrado chamado random que pode ser usado para fazer números aleatórios:
"""

import random
print(random.randrange(1, 10))