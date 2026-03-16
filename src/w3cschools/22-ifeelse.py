## Condições Python e instruções If
"""
Python suporta as condições lógicas usuais da matemática:

É igual a: a == b
Não é igual a: um!= b
Menos que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b
Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.
Uma "instrução if" é escrita usando o se palavra-chave.

"""

# Usando if para verificar uma condição
a = 33
b = 200
if b > a:
    print("b é maior que a")



# Usando elif para verificar várias condições
a = 33  
b = 33
if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")



# Usando else para executar um bloco de código se nenhuma das condições anteriores for verdadeira
a = 200
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")
else:
    print("a é maior que b")
