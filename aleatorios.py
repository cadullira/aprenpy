import random

# #random números inteiros entre 1 e 100
#valor = random.randint(1, 100) 
#print(valor)

# for i in range(5):
#     valor = random.randint(1, 60)
#     print(valor)

# random numero com ponto flutuante entre 0 e 1
#valor = random.random()
# usando * 10 para obter numeros aleatorios entre 0 e 10, a função round (built-in) vai arrendondar o número em quantas casas decimais desejar
#print(f'{round(valor * 10, 2)}')

# números aleatórios com pontos fluantes, onde poderei informar entre que intervalo
# valor = random.uniform(1, 100)

# print(f'{round(valor, 3)}')

lista = [1, 30, 2, 93, 81, 5, 6, 10, 45, 29]

#random em uma lista já definida
# o metódo choice escolhe um valor
sorteado = random.choice(lista)
print(f'Número sorteado na lista: {sorteado}')

# o método sample escolhe mais de um valor da lista
# são passados como argumentos a lista, e quantos valores serão escolhidos
sorteados = random.sample(lista, 3)
print(f'Números sorteado na lista: {sorteados}')

# embaralhar lista
lista_embaralhada = random.shuffle(lista)

print(f'Lista inicial: {lista}')
lista_embaralhada = random.shuffle(lista)
print(f'Lista embaralhada: {lista}')
