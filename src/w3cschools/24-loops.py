# Loops Python

"""
Python tem dois comandos de loop primitivos:
enquanto laços
para laços
O loop while

Com o enquanto loop podemos executar um conjunto de instruções desde que uma condição seja verdadeira.
"""
# Exemplo de uso do while loop
contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# O loop for é usado para iterar sobre uma sequência (que pode ser uma lista, tupla, dicionário, conjunto ou string).
# Exemplo de uso do for loop   
# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


# Iterando sobre uma string
for letra in "Python":
    print(letra) 
