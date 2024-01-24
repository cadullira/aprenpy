# Crie uma função chamada verificar_par que receba um número como parâmetro e imprima se o número é par ou ímpar.

def verificar_par(num):
    par_impar = None
    if(num % 2 == 0):
        par_impar = 'par'
    else:
        par_impar = 'ímpar'
    return par_impar