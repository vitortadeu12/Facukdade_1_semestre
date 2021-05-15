def minutos(horas):
     return horas * 60
def relogio(horas):
    total = horas * 3600
    return total            # ou return horas * 3600
horas = int(input('Digite as horas:'))
print(f'O valor de {horas} em segundos é {relogio(horas)} e em minutos é {minutos(horas)}')