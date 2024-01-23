#Modularização, Reúso de código, Legibilidade
# sem parâmetro
def mensagem():
    print('Tientre.ga')
    print('Entendendo, produzindo, entregando')

# com parâmetro
def soma(a, b):
    print(a+b)

# retorno da função
def multi(v1, v2):
    return v1 * v2

def div(k, j):
    if j != 0:
        return k/j
    else:
        return 'Impossível dividir número por zero'
def quadrado(val):
    quadrados = []
    for i in val:
        quadrados.append(i ** 2)
    return quadrados

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

    numeros = [2, 5, 8, 10]

    numeros_ao_quadrado = quadrado(numeros)

    for i in numeros_ao_quadrado:
        print(i)