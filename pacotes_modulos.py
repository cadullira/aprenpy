# pacotes um conjunto de códigos prontos são baixados, tem alguma funcinalidade específica e são somente usados por mim
# https://pypi.org endereço onde ficam armazenados os pacotes
# pacote podem possuir dependências de outros pacotes
# módulos são criados por mim, posso fazer coisas personalizáveis com minhas próprias funções

# para usar o uso comando import nome_do_modulo
#import math
# importa somente algumas funções de um pacote
#from math import sqrt, sin
#dando um apelido (aliases) para um módulo
#import math as m
import mod_func as mf

if __name__ == '__main__':
    mf.mensagem()

    num = int(input('Digite um número inteiro positivo: q'))

    print('\nCalcular fatorial do número: ')
    fat = mf.fatorial(num)
    print(f'O fatorial é: {fat}')

    print('\nCalcular a sequência de fibonacci do número: ')
    fib = mf.fibo(num)
    print(f'O fatorial é: {fib}')




#print(m.sqrt(81))

#usando algo do módulo importado
#print(sqrt(9))

# python --version                     -> versão do python
# pip --version                        -> versão do gerenciador de pacote (pip)
# python -m pip list                   -> lista os pacotes instalado na minha máquina
# python -m pip install nome_do_pacote -> instala um pacote
# python -m pip show nome_do_pacote    -> mostra detalhes de determinado pacote
# python -m pip uninstall nome_do_pacote  -> desinstala um pacote
