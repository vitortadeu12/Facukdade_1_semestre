def posicao_semana(dia):
    if dia == "domingo":
        return 1
    elif dia == "segunda":
        return 2
    elif dia == "terca":
        return 3
    elif dia == "quarta":
        return 4
    elif dia == "quinta":
        return 5
    elif dia == "sexta":
        return 6
    else:
        return 7
def dia_extendo(dia):
    if dia == 1:
        return "domingo"
    elif dia == 2:
        return "segunda"
    elif dia == 3:
        return "terca"
    elif dia == 4:
        return "quarta"
    elif dia == 5:
        return "quinta"
    elif dia == 6:
        return "sexta"
    else:
        return "sabado"

compra = input()
prazo = int(input())

if prazo == 0:
    print("Chega hoje:")
else:
    entrega = posicao_semana(compra) + prazo
    if entrega >= 7:
        entrega -= 7
        print(f'sera entregue {entrega}')