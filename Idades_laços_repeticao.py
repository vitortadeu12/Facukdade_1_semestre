soma = 0
quantiade = 1
n = int(input())
while n >= 0:
    quantiade += 1
    soma += n
    n = int(input())
media = soma / (quantiade - 1)
print(f'{media:.2f}')



#usamos o quantiade para ele contar quantos numeros foram digitados pelo n
#fizemos -1, pois queremos só os numeros positivos
#para apagar o primeiro numeo que digitamos, é necessario colocar outro
# input para digitar um novo numero