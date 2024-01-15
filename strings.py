# uma string é imutável, porém podemos alterar o seu valor

# nome = 'Eduardo'
# letra = nome[4]
# print(letra)
# print(nome[5])
# print(len(nome))

frase = 'A vida é uma jornada, não um destino. Aproveite o caminho'

#print(type(frase))

palavras = frase.split() # Cada palavra vai se transformar em um item para uma lista
#print(palavras) # palavras é uma lista criada a partir do fatiamento da string frase
#print(len(palavras))
#print(type(palavras))

# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)

# slices em uma string, no caso na string frase
# print(frase[3:19])
# print(frase[:21])
# print(frase[20:])
# print(frase[-10:-1])

# email = input('Digite seu melhor email: ')
# arroba = email.find('@') # a função find devolve a posição da lista que determinada pesquisa foi encontrada

# if arroba == -1:
#     print('Email inválido') # arroba == -1 é porque não foi encontrado o @ no email digitado, se foi encontrado alguma coisa com o método find. arroba valerá diferente de -1
# else:
#     print('Email válido')                    
# #print(arroba)

# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario, dominio)
# print(arroba) # o find só mostrará o primeiro resultado da pesquisa
# print(email.find('a'))

produtos = 'carbonato de sódio e óxido de zinco'

# print('sódio' in produtos)
# print('magnésio' in produtos)
# print('magnésio' not in produtos)

# print(produtos.find('dio'))
# print(produtos.find('ste')) # não achou o valor retorna a posição -1

# print(produtos.upper()) # tudo maiúscula
# print(produtos.lower()) # tudo minúscula
# print(produtos.capitalize()) # apenas a primeira letra ficará maiúscula
# print(produtos.title()) # a letra de cada palavras maiúscula

# print(produtos.replace('algodão', 'magnésio')) # o método replace substitui, se existir, uma palavra ou termo por outro. Primeiro argumento do método a palavra ou termo que desejo substituir, o termo que será colocado no seu lugar

# frase = '   Ômega 3 é bom para a saúde!   '
# frase_strip = frase.strip() # o método strip limpa o espaços em branco
# print(f'{frase}, total de caracteres da frase: {len(frase)}')
# print(frase.lstrip(), len(frase.lstrip())) # limpa os espaços em branco a esquerda
# print(frase.rstrip(), len(frase.rstrip())) # limpa os espaços em branco a direita
# print(f'{frase_strip}, total de caracteres da frase: {len(frase_strip)}')

# string alinhamento de texto com rjust, center, ljust

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20)) # default/padrão left justify
# print(fruta.ljust(20, '-'))
# print(fruta.center(20, '-'))
# print(fruta.rjust(20, '-'))

# p = 'Tientrega'
# # a função verifica se determinda palavra começa (startswitch), termina (endswitch) com caractere passado como argumento, retorna boolean

# print(p.startswith('T'))
# print(p.startswith('c'))
# print(p.endswith('ega'))

# Docstrings

doc = """
Docstrings é uma espécie de documentação
que podemos inserir dentro de um módulo, função ou
classe no python, entre outros locais.
        Respeita deslocamento de texto e é  multilinhas
    ------
        Não usar como comentário normal
"""

print(doc)