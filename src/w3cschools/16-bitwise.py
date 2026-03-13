# Operadores Bitwise
# Operadores bit a bit são usados para comparar números (binários):

#   Operator	Description	Example	Try it
"""   
& AND - Define cada bit como 1 se ambos os bits forem 1 x
| OR  - Define cada bit como 1 se um dos dois bits for 1 x | y
^ XOR - Define cada bit como 1 se apenas um dos dois bits for 1 x ^ y
~ NOT - Inverte todos os bits ~x
<<    - Deslocamento à esquerda com preenchimento de zeros Desloca para a esquerda inserindo zeros da direita e permitindo que os bits mais à esquerda sejam descartados x << n
>>    - Deslocamento à direita com sinal Desloca para a direita inserindo cópias do bit mais à esquerda da esquerda e permitindo que os bits mais à direita sejam descartados x >> n
"""
# Exemplos de operadores bit a bit:
x = 5  # em binário: 0101
y = 3  # em binário: 0011
print(f"x & y: {x & y}")  # returns 1 (em binário: 0001)
print(f"x | y: {x | y}")  # returns 7 (em binário: 0111)
print(f"x ^ y: {x ^ y}")  # returns 6 (em binário: 0110)
print(f"~x: {~x}")        # returns -6 (em binário: 1010)   
print(f"x << 1: {x << 1}")  # returns 10 (em binário: 1010)
print(f"x >> 1: {x >> 1}")  # returns 2 (em binário: 0010)