import q01, q02, q03, q04, q05, q06

if __name__ == '__main__':
    ## chamada q01
    # nome_informado = input('Qual o seu nome: ')
    # msg = q01.saudacao(nome_informado)
    # print(f'Olá, {msg}!')

    ## chamada q02
    # valor1 = int(input('Informe um número: '))
    # valor2 = int(input('Informe outro número: '))
    # resultado_soma = q02.soma_quadrados(valor1, valor2)
    # print(f'Número informados: ({valor1, valor2}) e a soma desses dois valores ao quadrado: ({resultado_soma})')

    # chamada q03
    # numero = int(input('Qual número para verificar se é par ou ímpar: '))
    # resultado_paridade = q03.verificar_par(numero)
    # print(f'{numero} é {resultado_paridade}')

    # chamada q04
    # n1 = float(input('Informe a 1ª nota: '))
    # n2 = float(input('Informe a 2ª nota: '))
    # n3 = float(input('Informe a 3ª nota: '))

    # media = q04.calcula_media(n1, n2, n3)
    # print(f'Notas informadas: [{n1, n2, n3}], média obtida [{round(media, 1)}]')

    # chamada q05
    # palavra = input('Informe a palavra para contarmos as vogais: ')
    # total_vogais = q05.contador_vogais(palavra)

    # print(f'Quantidade de vogais na palavra {palavra}: {total_vogais}')

    # chamada q06
    palavra = input('Digite uma palavra para invertermos: ')
    p_invertida = q06.inverter_string(palavra)
    print(f'{palavra} => {p_invertida}')