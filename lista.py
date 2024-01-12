# lista = ['valor1', 'valor2', 'valor3']

# notas = [10, 8, 9, 8.5, 9]
# print(notas)

# # definindo uma lista
# n1 = [4, 8, 3, 2, 2, 3]
# n2 = [10, 10, 9, 1, 4]
# #somando 2 listas
# valores = n1 + n2
# #mostrando a lista concatenada
# print(valores)
# #ver qual o tipo de valores list
# print(type(valores))
# #alterar o valor de determinado índice da lista
# valores[6] = 4
# valores[7] = 8
# print(f'{valores[6], valores[7], len(valores)}')
# #posições invertidas
# #mostra o último elemento da lista, o penúltimo, e antepenúltimo e assim sucessivamente
# print(valores[-1], valores[-2], valores[-3])
# #slices
# #vai pegar intervalos de elementos de uma lista
# print(valores[0:3])
# print(valores[:2])
# print(valores[3:])
# print(valores[-7:])
# print(valores[-4:-1])

# print(len(valores)) # tamanho da lista
# print(sorted(valores)) # ordena a lista em ordem crescente
# print(sorted(valores, reverse=True)) # ordena a lista de forma reversa
# print(sum(valores)) # soma os elementos da lista
# print(min(valores)) # menor número da lista
# print(max(valores)) # maior número da lista

# valores.append(19) # adiciona valor no final da lista
# print(valores) 
# valores.pop() # exclui o último valor da lista
# print(valores)
# valores.pop(4) # exclui elemento informado como argumento da função
# print(valores)
# valores.insert(3, 28) # primeiro argumento a posição que será inserido, o segundo argumento o valor a ser inserido
# print(valores)

# print(12 in valores)
# print(0 in valores)
# print(2 in valores)

# # Iterar uma lista 

# planetas = ['Vênus', 'Saturno', 'Urano', 'Netuno'] #list() forma alternativa de declarar uma lista vazia
# print(planetas)
# planetas.append('Mercúrio') # com o método append só podemos adicionar um argumento por vez
# print(planetas)

# for planeta in planetas:
#     print(planeta)

# Exercício

bebidas_favoritas = []

for i in range(5):
    #bebidas_favoritas.append(input(f'Digite a {i+1}ª bebida: '))
    print(f'Digite a {i+1}ª bebida: ')
    bebida = input()
    bebidas_favoritas.append(bebida)
print('\n\n')

#bebidas_favoritas.sort() #a lista tem uma função que se ordena
#print(bebidas_favoritas)

print('Bebidas Favoritas: ')
print('\n')

for bebida in sorted(bebidas_favoritas):
    print(bebida)




