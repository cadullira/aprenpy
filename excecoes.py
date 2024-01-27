# um objeto que representa um erro quando ocorrer algum erro no código
# try...except

# Exception - Classe base para todas as exceções
# ArithimeticError - Classe base para todos os erros que ocorrem em cálculos numéricos
# OverflowError - Um cálculo excedeu o limite máximo de um tipo numérico
# ZeroDivisionError - Lançada quando uma divisão ou módulo por zero é executada em tipos númericos
# ImportError - Lançada quando uma declaração import falha
# NameError - Um identificador (nome) não foi encontrado no namespace local ou global
# IOError - Ocorre quando uma operação de E/S, como ler ou escrever em um arquivo, falha.
# IdentationError - A indentação não foi aplicada corretamente
# RecursionError - O interpretador detectou que a profundidade máxima de recursão foi excedida.
# TypeError - Lançada quando uma função ou operação é inválida para o tipo de dados especificado

#=========================================================================

#explicação 1 - o que é uma exceção

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# try: # dentro do try vai o código que pode ocorre um erro
#     r = round(n1/n2, 2) 
# #except: # erro genérico
# except ZeroDivisionError: # dentro except genérico ou específico vai a mensagem caso ocorra o erro
#     print(f'Não é possível dividir por zero!!!')
# else: # caso não o erro o else irá ser executado
#     print(f'Resultado: {r}')

#=========================================================================

#explicação 2 - enfileirando exceções, mais de um tipo de exceção em um try, usando também o finally que vai ser executado independente de qualquer resultado

# def div(j, k):
#     return round(j/k, 2)

# if __name__ == '__main__':
#     while True:
#         try:
#             n1 = int(input('Digite um número: '))
#             n2 = int(input('Digite outro número: '))
#             break
#         except ValueError:
#             print('Ocorreu um erro ao ler o valor. Tente novamente')
#     try:
#         r = div(n1, n2)
#     except ZeroDivisionError:
#         print(f'Não é possível dividir por zero!!!')
#     except:
#         print('Ocorreu um erro desconhecido')
#     else:
#         print(f'Resultado: {r}')
#     finally: # com o finally esse bloco sempre será executado
#         print('\nfim do cálculo')


#=========================================================================

from math import sqrt

#explicação 4 - criando nossas próprias exceções

class NumeroNegativoError(Exception):
    pass # o pass dá a possibilidade rodar um código sem seja implementado
         # existe a class NumeroNegativoError só não faz nada

#=========================================================================

#explicação 3 - forçando que seja lançado uma exceção mesmo que o python não identifique esse erro, com raise


if __name__ == '__main__':
    try:
        num = int(input('Digite um número: '))
        if num < 0:
            #raise ArithmeticError 
            raise NumeroNegativoError
            # no código acima pede que seja fornecido um número inteiro, porém só quero receber um número inteiro positivo, dessa forma forço para que seja chamado uma exceção quando a condição não seja satisfeita
            # anteriormente estava sendo usada um erro do python, agora o raise chama o próprio erro personalizado NumeroNegativoError
    except NumeroNegativoError:
        print('Foi fornecido um número negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print('Fim do cálculo')

