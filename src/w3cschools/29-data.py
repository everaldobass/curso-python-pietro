# Datas Python
"""
Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo nomeado datetime para trabalhar com datas como data objetos.
"""

import datetime

hoje =  datetime.datetime.now()
print(hoje)


# Retorne o ano e o nome do dia da semana:
ano = datetime.datetime.now()
print(ano.year)
print(ano.strftime("%A"))


# Criando objetos de data
""" 
Para criar uma data, podemos usar o datetime() classe (construtor) do datetime módulo.
O datetime() classe requer três parâmetros para criar uma data: ano, mês, dia.
"""
objdata =  datetime.datetime(2026, 3, 17)
print(objdata)



# O método strftime()
"""
O datetime object tem um método para formatar objetos de data em strings legíveis.
O método é chamado strftime(), e recebe um parâmetro, format, para especificar o formato da string retornada
"""
mes =  datetime.datetime(2026, 3, 17)
print(mes.strftime("%B"))

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))