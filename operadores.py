# ARITMÉTICOS

# +  -> adição
# -  -> subtração
# *  -> multiplicação
# /  -> divisão
# // -> divisão inteira
# %  -> resto da divisão
# ** -> potenciação

#x = y = z = 0
# x = 7
# y = 9
# z = x + y
# print('A soma dos valores: ', z)

# x = int(input('Digite um número: '))
# y = int(input('Digite outro número: '))
# z = x + y
# print('A soma dos valores: ', z)

# RELACIONAIS

# == -> igual
# != -> diferente
# >  -> maior
# >= -> maior igual
# <  -> menor
# <= -> menor igual

#x = y = z = False
# n1 = n2 = 0

# n1 = int (input('Digite o 1º valor: '))
# n2 = int(input('Digite o 2º valor: '))

# x = n1 == n2
# print(f'{n1} é igual a {n2}? {x}')

# y = n1 > n2
# print(f'{n1} é maior que a {n2}? {y}')

# z = n1 != n2
# print(f'{n1} diferente de {n2}? {z}')

# LÓGICOS

# e   -> and 
# ou  -> or
# não -> not

# os resultados obtidos a partir do uso dos operadores lógicos sempre será um boolean, true ou false

# exemplo 1 - Verifica se uma pessoa pode particpar de determinada competição esportiva, para isso deverá ter ao menos 18 anos E altura superior a 1.70

# idade = altura = 0

# idade = 19
# altura = 1.74

# resultado = (idade >= 18) and (altura > 1.70)
# print('Pode participar do evento esportivo? '+ str(resultado)) # essa conversão de converter resultado que é um bool para str, se dá pelo uso do + para concatenar

# exemplo 2 - Verifica se um alarme está disparado, para isso a entrada esteja com seu valor igual a A

# porta = 'f'
# janela = 'f'

# disparado = porta == 'a' or janela == 'a'

# print ('O alarme está disparado =>', disparado)

# exemplo 3 - Verifica se uma pessoa pode realizar uma compra, essa só será efetuada com tem_dinheiro = 'True'

# tem_dinheiro = False
# #recebi uma grana
# tem_dinheiro = not False

# print('Posso comprar? ' + str(tem_dinheiro))
