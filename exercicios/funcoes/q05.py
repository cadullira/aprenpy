# Implemente uma função chamada contador_vogais que receba uma string como parâmetro e retorne o número de vogais na string.

def contador_vogais(palavra):
    contador_vogais = 0
    vogais = 'AaEeIiOoUu'
    for e_vogal in palavra:
        if e_vogal in vogais:
            contador_vogais += 1
    return contador_vogais
        