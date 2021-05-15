a = str(input()).upper()
b = str(input()).upper()
c = str(input()).upper()
if a == 'VERTEBRADO':
    if b == 'AVE':
        if c == 'CARNIVORO':
            print('aguia')
        else:
            c == 'ONIVORO'
            print('pomba')
    if b == 'MAMIFERO':
        if c == 'ONIVORO':
            print('homem')
        else:
            c == 'HERBIVORO'
            print('vaca')
else:
    a == 'INVERTEBRADO'
    if b == 'INSETO':
        if c == 'HEMATOFAGO':
            print('pulga')
        else:
            c == 'HERBIVORO'
            print('lagarta')
    if b == 'ANELIDIO':
        if c == 'HEMATOFAGO':
            print('sanguessuga')
        else:
            c == 'ONIVORO'
            print('minhoca')

# Outra forma de fazer
'''x = input()
y = input()
z = input()
if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    a = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    a = 'pomba'
if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    a = 'homem'
if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    a = 'vaca'
if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    a = 'pulga'
if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    a = 'lagarta'
if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    a = 'sanguessuga'
if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    a = 'minhoca'
print(a)'''