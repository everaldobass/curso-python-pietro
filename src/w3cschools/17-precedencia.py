# Precedência do Operador
# A precedência do operador descreve a ordem em que as operações são executadas.

# A ordem de precedência do operador é (do mais alto para o mais baixo):
""" 
1. Parênteses ()
2. Exponenciação ** 
3. Multiplicação *, Divisão /, Módulo %, Divisão Inteira //
4. Adição +, Subtração -
5. Operadores de Comparação: ==, !=, >, <, >=, <=
6. Operadores de Atribuição: =, +=, -=, *=, /=, %=, **=, //=
7. Operadores Lógicos: and, or, not
8. Operadores Bitwise: &, |, ^, ~, <<, >>   
"""
# Exemplos de precedência do operador:

# returns 20, porque a multiplicação é executada antes da adição e o resultado da multiplicação é 10, e 10 + 10 é 20
resultado = 10 + 5 * 2
print(f"O resultado de 10 + 5 * 2 é: {resultado}")  

# returns 30, porque os parênteses alteram a ordem de execução, fazendo a adição ser executada antes da multiplicação
resultado = (10 + 5) * 2
print(f"O resultado de (10 + 5) * 2 é: {resultado}")  

# returns 30, porque a exponenciação é executada antes da multiplicação e adição
resultado = 10 + 5 * 2 ** 2
print(f"O resultado de 10 + 5 * 2 ** 2 é: {resultado}") 

# returns False, porque a comparação é executada antes do operador lógico e o resultado da comparação é False, e False and True é False
resultado = 10 > 5 and 5 < 3
print(f"O resultado de 10 > 5 and 5 < 3 é: {resultado}")

# returns True, porque a comparação é executada antes do operador lógico e o resultado da comparação é True, e True or False é True
resultado = 10 > 5 or 5 < 3
print(f"O resultado de 10 > 5 or 5 < 3 é: {resultado}")  
