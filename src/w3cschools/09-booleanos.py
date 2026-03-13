## Valores Booleanos
"""
Na programação, muitas vezes você precisa saber se uma expressão é True ou False.
Você pode avaliar qualquer expressão em Python e obter uma de duas respostas, True ou False.
Quando você compara dois valores, a expressão é avaliada e o Python retorna a resposta booleana:
"""
print(10 > 9)  # returns True
print(10 == 9) # returns False
print(10 < 9)  # returns False

print(bool("Hello"))  # returns True
print(bool(15))       # returns True


# Imprima uma mensagem com base em se a condição é True ou False:
print("Exercicio para saber se um número é maior que outro")
a = 200
b = 330
if b > a:
  print("\nb é maior que a", a)
else:
  print("\nb não é maior que a" , a)
