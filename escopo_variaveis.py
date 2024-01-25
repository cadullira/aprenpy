# variável global, local

var_global = 'Aprender Python'
def escreve_texto():
    global var_global
    var_global = 'Aprender Java' # mesmo tendo o mesmo nome da variável de fora essa var_global só terá esse valor dentro da função, para conseguir reatribuir um valor para a mesma, e que esse valor possa está disponível fora da função dizemos para a variável que ela é global antes da sua declaração

    var_local = 'Carlos'
    print(f'Variável global: {var_global}')
    print(f'Variável local: {var_local}')

if __name__ == '__main__':
    print('Executar a função excreve_texto()')
    escreve_texto()

    print('Tentar executar as variáveis diretamente:')
    print(f'Variável global: {var_global}')
    #print(f'Variável local: {var_local}') # dá um erro pois a variável local não está disponível fora da função