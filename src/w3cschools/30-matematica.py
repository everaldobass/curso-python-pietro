# Matemática
"""
Python tem um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático, que permite executar tarefas matemáticas em números.
Funções matemáticas integradas
O min() e max() funções podem ser usadas para encontrar o menor ou maior valor em um iterável:
"""

a = min(1,2,3,4,5,10,25)
b = max(5,10,25,30,35,40,45)

print(a)
print(b)

# O abs() a função retorna o valor absoluto (positivo) do número especificado:
vabs =  abs(-7.25)
print("Valor absoluto: ", vabs)

# O função retorna o valor de x elevado a y (xvocê).pow(x, y)
x = pow(4,3)
print(x)

# O Módulo de Matemática
"""
Python também possui um módulo integrado chamado math, que amplia a lista de funções matemáticas.
Para utilizá-lo, você deve importar o math módulo:
"""

import math

y = math.sqrt(64)
print("Raiz quadrada", y)