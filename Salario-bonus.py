nome = str(input("Nome: ")) #Aqui o input já é um str então no caso não seria necessario
a = float(input())
b = float(input())
TOTAL = (b * 0.15) + a
print('TOTAL = R$ {:.2f}'.format(TOTAL))