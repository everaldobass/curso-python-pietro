# Operadores de identidade
# Operadores de identidade são usados para comparar os objetos, não se eles forem iguais, mas se eles forem realmente o mesmo objeto, com o mesmo local de memória:

#   Operator	Description	Example	Try it
"""   is 	Returns True if both variables are the same object	x is y  
      is not	Returns True if both variables are not the same object	x is not y
"""

# Exemplos de operadores de identidade:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(f"x is y: {x is y}")      # returns False
print(f"x is z: {x is z}")      # returns True
print(f"x is not y: {x is not y}")  # returns True