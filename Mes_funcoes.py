def mes_do_ano (mes):
    if mes == 1:
        return ('January')
    if mes == 2:
        return ('February')
    if mes == 3:
        return ('March')
    if mes == 4:
        return ('April')
    if mes == 5:
        return ('May')
    if mes == 6:
        return ('June')
    if mes == 7:
        return ('July')
    if mes == 8:
        return ('August')
    if mes == 9:
        return ('September')
    if mes == 10:
        return ('October')
    if mes == 11:
        return ('November')
    if mes == 12:
        return ('December')



mes = int(input())
imprime_mes = mes_do_ano(mes)
print(imprime_mes)
print(mes_do_ano(mes))#POde ser assim tbm 