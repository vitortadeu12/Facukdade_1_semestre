a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangulo = (a * c) / 2
circulo = 3.14159 * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b
print('TRIANGULO: {:.3F}'.format(triangulo))
print('CIRCULO: {:.3F}'.format(circulo))
print('TRAPEZIO: {:.3F}'.format(trapezio))
print('QUADRADO: {:.3F}'.format(quadrado))
print('RETANGULO: {:.3F}'.format(retangulo))

'''print(f'TRIANGULO: {triangulo:.3F}\n CIRCULO: {circulo:.3F}\n TRAPEZIO: {trapezio:.3F}\n ') #print na mesma linha'''
'''Precisamos converter o numero em string e depois trasposfar eme float'''
# No exercicio de area do triangulo iremos usar dessa forma