planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Vênus', 'Lua', 'Sirius', 'Marte']
print(astros, end=' ')
astro_set = set(astros)
print(astro_set) # com o uso de set (conjunto), os elementos não se repetem)

astros1 = {'Lua', 'Vênus', 'Lua', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Lua', 'Sirius', 'Marte', 'Cometa de Halley'}

# print(astros1 != astros2) # vê se conjuntos são diferentes, retorna um boolean

# print(astros1 | astros2) # faz a união entre dois conjuntos
# print(astros2.union(astros1)) # faz mesma coisa de forma diferente

# print(astros1 & astros2) # faz a interseção entre dois conjuntos
# print(astros2.intersection(astros1)) # ou seja elementos comun entre os conjuntos

# print(astros1 ^ astros2) # faz a diferença simétrica entre dois conjuntos
# print(astros2.symmetric_difference(astros1)) 

astros1.add('Urano') # adiciona elemento no set/conjunto
print(astros1)

#astros1.remove('Sol') # erro de chave o elemento não estiver presente no conjunto, o contrário remove o elemento
astros1.remove('Lua')
print(astros1)

astros1.discard('Sol') # com o método discard, diferente do remove, caso o elemento informado não faça parte do conjunto, nenhum erro é dado
print(astros1)

astros1.pop() # exclui um elemento aleatório do conjunto
print(astros1)

astros1.clear() # limpa o conjunto
print(astros1)

conjunto_de_palavras_proibidas = {"spam", "spam", "eggs"}
mensagem = "spam and eggs"
if "spam" in conjunto_de_palavras_proibidas:
    print("A mensagem contém palavras proibidas.")
