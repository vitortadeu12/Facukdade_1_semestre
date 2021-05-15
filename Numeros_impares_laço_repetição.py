'''Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.'''
x = int(input())
for impar in range(0, x + 1):
    if impar % 2 != 0:
        print(impar)

