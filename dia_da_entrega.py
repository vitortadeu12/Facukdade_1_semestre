z = input()
dia = int(input())
if z == "domingo":
    z = 0
if z == "segunda":
    z = 1
if z == "terca":
    z = 2
if z == "quarta":
    z = 3
if z == "quinta":
    z = 4
if z == "sexta":
    z = 5
if z == "sabado":
    z = 6
if dia == 0:
    print('chega hoje!')
else:
    entrega = (dia % 7) + z
    if entrega > 6:
        entrega = (dia % 7 + z) - 7
    if entrega == 0:
        entrega = "domingo"
    if entrega == 1:
        entrega = "segunda"
    if entrega == 2:
        entrega = "terca"
    if entrega == 3:
        entrega = "quarta"
    if entrega == 4:
        entrega = "quinta"
    if entrega == 5:
        entrega = "sexta"
    if entrega == 6:
        entrega = "sabado"
    print(f'sera entregue {entrega}')