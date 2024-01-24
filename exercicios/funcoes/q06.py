# Crie uma função chamada inverter_string que aceite uma string como parâmetro e retorne a string invertida. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".
def inverter_string(palavra):
    invertida = ""

    for i in palavra:
        invertida = i + invertida
     
    return invertida