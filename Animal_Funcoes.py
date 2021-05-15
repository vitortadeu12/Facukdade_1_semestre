def mostrar_anamial(a, b, c):
    if a == 'VERTEBRADO':
        if b == 'AVE':
            if c == 'CARNIVORO':
                return ('aguia')  # Nesse exemplo pode ser tanto print como o return
            else:
                c == 'ONIVORO'
                return ('pomba')
        if b == 'MAMIFERO':
            if c == 'ONIVORO':
                return ('homem')
            else:
                c == 'HERBIVORO'
                return ('vaca')
    else:
        a == 'INVERTEBRADO'
        if b == 'INSETO':
            if c == 'HEMATOFAGO':
                return ('pulga')
            else:
                c == 'HERBIVORO'
                return ('lagarta')
        if b == 'ANELIDIO':
            if c == 'HEMATOFAGO':
                return ('sanguessuga')
            else:
                c == 'ONIVORO'
                return ('minhoca')

a = str(input()).upper()
b = str(input()).upper()
c = str(input()).upper()

animais = mostrar_anamial(a, b, c)
print(animais)