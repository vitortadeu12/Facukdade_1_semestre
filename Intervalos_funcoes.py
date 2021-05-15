def retona_intervalo(n):
    if 0 <= n <= 25:
        return 'Intervalo [0,25]'
    if 25 < n <= 50:
        return 'Intervalo (25,50]'
    if 50 < n <= 75:
        return 'Intervalo (50,75]'
    if 75 < n <= 100:
        return 'Intervalo (75,100]'
    if x > 100 or n < 0:
        return 'Fora de intervalo'

x = float(input())
print(retona_intervalo(x))


'''def exibe_intervalo(n):
    if 0 <= n <= 25:
        print('Intervalo [0,25]')
    if 25 < n <= 50:
        print('Intervalo (25,50]')
    if 50 < n <= 75:
        print('Intervalo (50,75]')
    if 75 < n <= 100:
        print('Intervalo (75,100]')
    if x > 100 or n < 0:
        print('Fora de intervalo')

x = float(input())
exibe_intervalo(x)'''