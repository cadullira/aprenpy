# estrutura de dados imutável
# após criada não pode ser modifcada

tupla = (2, 4, 6, 9)
print(tupla)
print(tupla[1])
#tupla[2] = 4 # erro ao tentar modificar o valor de um índice de uma tupla

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t_numeros = (6,4,9,1,4,6,6,12,3,8)

print(f'{len(halogenios), halogenios[2], halogenios[-2]}')
print(elementos)
print(t_numeros.count(4))
print(elementos[1:5])
print(elementos[-5:])
print('Fe' in elementos)
print('Rn' in elementos)
print(sum(t_numeros))

# Não pode fazer com tupla: .sort, .append(), .reverse(), .pop() isso acontece por ser uma estrutura imutável

#print(sorted(elementos)) # sorted não altera a lista apenas exibi a lista de maneira ordenada
#print(elementos.sort()) # já sort ele pega a lista e a modifica 

for elemento in elementos:
    print(elemento)

# cria lista a partir de uma tupla
grupo17 = list(halogenios)
print(grupo17)
print(type(grupo17))

# tupla a partir de uma lista
grupo1 = ['Li', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(type(alcalinos))

