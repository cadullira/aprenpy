# simples, composto, encadeado

nota1, nota2, media = 0.0, 0.0, 0.0

nota1 = float(input('Informe sua 1ª nota: '))
nota2 = float(input('Informe sua 2ª nota: '))

media = (nota1 + nota2) / 2
#se o programa tiver somente o if, será uma condicional simples
#se o programa tiver o if e else, será uma condicional composto
#se o programa tiver o encadeamento de if mais elifs e o else, será uma condicional encadeada
if(media >= 7):
    print('Aluno aprovado!')
    print('Parabéns')
elif(media > 4):
    print('Aluno de recuperação')
else:
    print('Aluno reprovado')

print('A média da nota do aluno: {}'.format(media))