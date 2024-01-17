elemento = {
    'nome' : 'Lítio',
    'grupo' : 'Metais alcalinos',
    'densidade' : 0.534 
}

print(elemento['nome']) #mostra o valor da chave nome
print(elemento['grupo'])
print(elemento['densidade'])
print(f'O dicionário tem {len(elemento)} elementos')

#atualiza uma entrada
elemento['grupo'] = 'Alcalinos'
#mostra todas as chaves (keys) e valores (values)
print(elemento)

#adiciona uma entrada
elemento['periodo'] = 1
print(elemento)

#exclui um item de um dicionário
#del elemento['periodo']
#print(elemento)

#limpa todos os itens de um dicionário 
#elemento.clear()
#print(elemento)

#exclui o dicionário
#del elemento
#print(elemento)

#vai printar uma lista de tuplas
print(elemento.items())

#percorrendo um dicionário

# em cada iteração printa i => tupla (uma por linha)
# for i in elemento.items():
#     print(i)

# em cada iteração é printado uma key (chave)
# for i in elemento.keys():
#     print(i)

# em cada iteração é printado um value (valor)
# for i in elemento.values():
#     print(i)

# faz uma espécie de extrair a chave e o valor da tupla
for i, j in elemento.items():
    print(f'{i} : {j}')



