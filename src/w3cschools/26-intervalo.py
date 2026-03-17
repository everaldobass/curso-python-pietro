# Intervalo Python
"""
O embutido range() A função retorna uma sequência imutável de números, comumente usada para fazer um loop um número específico de vezes.
Este conjunto de números tem seu próprio tipo de dados chamado range.
"""

# Criando intervalos
a =  range(10)
print(a)

# Chamada range() com três argumentos
"""
Se a função range for chamada com três argumentos, o terceiro argumento representa o step valor.
O valor do passo significa a diferença entre cada número na sequência. É opcional e, se não for fornecido, o padrão é 1.
range(3, 10, 2)retorna uma sequência de cada número de 3 a 9, com passo 2:
"""
y =  range(3,10,2)

for i in range(10):
 print(i)

# Usando lista para exibir intervalos
"""
O objeto range é um tipo de dado que representa uma sequência imutável de números e não pode ser exibido diretamente.
Portanto, os intervalos são frequentemente convertidos em listas para exibição.
"""
print(list(range(5)))


# Faixas de corte
# Como outras sequências, os intervalos podem ser fatiados para extrair uma subsequência.
r = range(10)
print(r[2])


# Teste de associação
# Os intervalos suportam testes de associação com o in operador.
r = range(0,10,2)
print(6 in r)

# Comprimento
# Os intervalos suportam o len() função para obter o número de elementos no intervalo.
r = range(0,10,2)
print(len(r))