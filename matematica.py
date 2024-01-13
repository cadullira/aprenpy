# Funções builtin -> são internas, ou seja, já presentes no python não precisa importar nada

# valores = [10, 2, 3 , 2, 4, 4, 6, 8, 2, 9, 3, 0, 1, 10, 8, 9]
# a, b, c, d, e, f = 10, 2, 1, -4, 3, 30.93024824

# print(max(valores)) # busca o maior valor dentro de uma lista
# print(min(valores)) # busca o menor valor dentro de uma lista
# print(abs(d)) # mostra o valor absoluto de um número, ou seja, a diferença de um número até o zero (0), absoluto de -5 é 5, o de 5 também 5
# print(pow(a, c)) # exponenciação, primeiro argumento da função pow é a base, o segundo a potência, no exemplo, 10 elevado a 1
# print(pow(b, e))
# print(round(f, 2)) # arredonda, primeiro argumento o número para arredondar, o segundo quantas casas decimais
# print(round(f, 4))

# importando a função math
import math

x = 8
y = 100

raiz_quadrada = math.sqrt(x) # raiz quadrada
print(math.ceil(raiz_quadrada)) # arredonda para cima
print(math.floor(raiz_quadrada)) # arredonda para baixo
print(round(raiz_quadrada, 2)) # função builtin para arredondamento
logaritmo = math.log10(x) # calcular logaritmo de um número base 10
print(math.factorial(100)) # calcular fatorial
print(x / math.inf) # numero dividido pelo infinito