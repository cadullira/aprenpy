# #Modularização, Reúso de código, Legibilidade
# # sem parâmetro
# def mensagem():
#     print('Tientre.ga')
#     print('Entendendo, produzindo, entregando')

# # com parâmetro
# def soma(a, b):
#     print(a+b)

# # retorno da função
# def multi(v1, v2):
#     return v1 * v2

# def div(k, j):
#     if j != 0:
#         return k/j
#     else:
#         return 'Impossível dividir número por zero'
# def quadrado(val):
#     quadrados = []
#     for i in val:
#         quadrados.append(i ** 2)
#     return quadrados

# parâmetros obrigatórios, opcionais, valor padrão
def contar(num, caractere = '+'):
    # num = 11, caractere = '+'
    # num, caractere = '+'
    for i in range(1, num):
        print(caractere)

def soma_multi(a, b, c=0):
    if c==0:
        return a*b
    else:
        return a+b+c

if __name__ == '__main__':

    # a = 10
    # b = 8

    # mensagem()
    # soma(a, b)
    # resultado_multi = multi(a, b)
    # print(resultado_multi)

    # dividendo = int(input('Informe o dividendo: '))
    # divisor = int(input('Informe o divisor: '))

    # r_div = div(dividendo, divisor)
    # print(r_div)

    # numeros = [2, 5, 8, 10]

    # numeros_ao_quadrado = quadrado(numeros)

    # for i in numeros_ao_quadrado:
    #     print(i)
    # contar() # deixei vazio porém existe um valor padrão estabelecido na declaração da função
    # contar(4, 'x') # aqui é passado um valor que é obrigatório, o num, caractere opcional pois já possui um valor default
    x = 10
    y = 3
    z = 4
    resultado = soma_multi(x, y, z)
    print(resultado)