soma = 0
n1 = int(input())
n2 = int(input())
if n1 < n2:
    for impar in range(n1 + 1, n2):
        if not impar % 2 == 0:
            soma += impar
            print(impar)
if n2 < n1:
    for impar in range(n2 + 1, n1):
        if not impar % 2 == 0:
            soma += impar
            print(impar)
print(f'O valor da soma é {soma}')


# ver a explicação do professor sobre esse exercicio
