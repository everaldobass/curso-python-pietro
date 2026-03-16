# A declaração de correspondência do Python
"""
Em vez de escrever muitos if..else declarações, você pode usar o match declaração.
O match a instrução seleciona um dos muitos blocos de código a serem executados.

O match a expressão é avaliada uma vez.
O valor da expressão é comparado com os valores de cada um case.
Se houver uma correspondência, o bloco de código associado será executado.

A sintaxe do match declaração é a seguinte:
"""
# Exemplo de uso do match declaração
status = 418

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(400))  # Retorna "Bad request"
print(http_error(404))  # Retorna "Not found"
print(http_error(418))  # Retorna "I'm a teapot"
print(http_error(500))  # Retorna "Something's wrong with the internet"



# Exemplo de uso do match declaração com padrões de sequência
print("\nExemplo de uso do match declaração com padrões de sequência")

dia = "Domingo"

def dia_da_semana(dia):
    match dia:
        case "segunda-feira":
            return "Hoje é segunda-feira"
        case "terça-feira":
            return "Hoje é terça-feira"
        case "quarta-feira":
            return "Hoje é quarta-feira"
        case "quinta-feira":
            return "Hoje é quinta-feira"
        case "sexta-feira":
            return "Hoje é sexta-feira"
        case "Sábado":
            return "Hoje é sábado"
        
        case "Domingo":
            return "Hoje é domingo"
        case _:
            return "Não é um dia da semana válido"
        
print(dia_da_semana(dia))  # Retorna "Hoje é segunda-feira"


