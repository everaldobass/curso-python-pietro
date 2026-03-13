# Python Operadores de Associação
# Operadores de associação são usados para testar se uma sequência é apresentada em um objeto:

#   Operator	Description	Example	Try it
"""   
`in` Retorna verdadeiro se uma sequência com o valor especificado estiver presente no objeto `x` em `y`.
`not in` Retorna verdadeiro se uma sequência com o valor especificado não estiver presente no objeto `x` em `y`.
"""

# Exemplos de operadores de associação:
x = "Hello, World!"
print(f"'Hello' in x: {'Hello' in x}")  # returns True
print(f"'Python' in x: {'Python' in x}")  # returns False
print(f"'World' not in x: {'World' not in x}")  # returns False