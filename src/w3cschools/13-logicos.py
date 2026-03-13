# Operadores Lógicos
# Operadores lógicos são usados para combinar instruções condicionais:

#   Operator	Description	Example	Try it
"""   and 	Returns True if both statements are true	x < 5 and  x < 10	
      or	Returns True if one of the statements is true	x < 5 or x < 4	
      not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

# Exemplos de operadores lógicos:
x = 5
print(f"x > 3 and x < 10: {x > 3 and x < 10}")  # returns True
print(f"x > 3 or x < 4: {x > 3 or x < 4}")    # returns True
print(f"not(x > 3 and x < 10): {not(x > 3 and x < 10)}")  # returns False

