# while

# num = 1

# while(num <= 10):
#     print(f'O número vale {num}')
#     num += 1

# nome = None

# while True:
#     print('Digite seu nome, ou x para sair ')
#     nome = input()
#     if nome == 'x' or nome == 'X':
#         break;
#     print(f'Bem-vindo, {nome}')
# print('Até logo!')

# for

# lista = [2, 6, 9, 4, 0, 12, 3, 7]
# palavra = 'Brasil'

# for item in lista:
#     print(item)

# for letra in palavra:
#     print(letra)

# for numero in range(1, 11): # range inicia no 1 e vai até o valor final -1
#     print(numero)

# range(valor_inicial, valor_final, incremento)
# for numero in range(10):
#     print(numero)

# for x in range(2, 20, 2):
#     print(x)
# # faz o range inverso, com decremento
# for x in range(20, 2, -2):
#     print(x)

# pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
# for pedra in pedras:
#     if pedra == 'Quartzo':
#         continue # não executa a instrução testada, no caso pedra quando testada == 'Quartzo', a intrução não é executada, e passa para a seguinte
#     print(pedra)

# REPETIÇÕES ENCADEADAS

# for contador_externo in range(1,6):
#     print(f'\nRodada: {contador_externo}')
#     for contador_interno in range(5, 0, -1):
#         print(f'valor: {contador_interno}')

# import random
# for A in range(1, 6):
#     print(f'\nAposta {A}:')
#     for B in range(6):
#         numero = random.randint(1, 61)        
#         print(numero)

