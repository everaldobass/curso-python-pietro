# Funções Python
"""
Uma função é um bloco de código que só é executado quando é chamado.
Como resultado, uma função pode retornar dados.
Uma função ajuda a evitar a repetição de código.

Em Python, uma função é definida usando o def palavra-chave, seguida de um nome de função e parênteses:
"""
# Criando uma função
def minha_funcao():
    print("Olá, esta é minha função!")
# Chamando a função
minha_funcao()

# Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}!")  
saudacao("Alice")  # Retorna "Olá, Alice!"

# Função com retorno
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado
resultado = soma(5, 3)
print(resultado)  # Retorna 8

# Função com retorno
def subtracao(a, b):
    return a - b

# Chamando a função e armazenando o resultado
resultado = subtracao(50, 20)
print(resultado)  # Retorna 30


# Função com retorno
def multiplicacao(a, b):
    return a * b

# Chamando a função e armazenando o resultado
resultado = multiplicacao(5, 3)
print(resultado)  # Retorna 15



# Função com retorno
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."
    
# Chamando a função e armazenando o resultado
resultado = divisao(10, 2)  
print(resultado)  # Retorna 5.0


