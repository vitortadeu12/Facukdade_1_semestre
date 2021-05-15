def multiplos(a, b):
    return a % b == 0 or b % a == 0  #uma das formas de fazer, jeito da faculdade

a, b = input().split()
a = int(a)
b = int(b)
if multiplos(a, b):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')


'''def multiplos(a, b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False'''
#outra forma de fazer