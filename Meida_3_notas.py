n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
if media >= 7.0:
    print(f'Media: {media :.1f}\nAluno aprovado.')
elif media <= 6.9 and media >= 5.0:                                            #ou 6.9 <= media >=5.0
    print('', end='')                                 # comando end='' ele não pula a linha
    n5 = float(input())
    exame = (n5 + media) / 2
    if exame >= 5.0:
        print(f'Media: {media :.1f}\nAluno em exame.')
        print(f'Nota do exame {n5:.1f}')
        print(f'Aluno Aprovado.')
        print(f'Media final: {exame:.1f}')
    else:
        exame < 4.9
        print(f'Media: {media :.1f}\nAluno em exame.')
        print(f'Nota do exame {n5:.1f}')
        print(f'Aluno Reprovado.')
        print(f'Media final: {exame:.1f}')
else:
    media <= 5.0
    print(f'Media: {media :.1f}\nAluno reprovado.')

    '''n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())'''