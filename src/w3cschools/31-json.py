"""
JSON é uma sintaxe para armazenar e trocar dados.
JSON é texto escrito com notação de objeto JavaScript.
JSON em Python
Python tem um pacote integrado chamado json, que pode ser usado para trabalhar com dados JSON.
"""

import json

# Converter de Json para Python
x =  '{"nome":"Pessoa1", "idade":30, "Cidade":"Jundiai"}'

# Parse X
y = json.loads(x)

# Resultado
print(y["idade"])


# Converter de Python para JSON
# Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o json.dumps() método.

a = {
    "name": "Jhon",
    "idade": 45,
    "cidade": "São Paulo"
}

# converter
a = json.dumps(a)
print(a)
