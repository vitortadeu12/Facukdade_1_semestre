x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'{distancia:.4f}')

'''Precisamos converter o numero em string e depois trasposfar eme float'''
# No exercicio de area do triangulo iremos usar dessa forma