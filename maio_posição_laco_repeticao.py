from random import randrange
numeros = []
for c in range(0, 101):
    n = randrange(0, 1000)
    numeros.append(n)
print(max(numeros))
print(numeros.index(max(numeros)))

'''O método index() encontro o índice de um item de uma determinada lista, 
passado o item desejado como argumento que neste caso foi o menor valor da lista retornado pelo método min().'''

# Outra forma de fazer tendo que digitar os 100 numeros:
n = []
i = 0
while i < 100:
    numero = int(input())
    n.append(numero)
    i += 1
print(max(n))
print(n.index(max(n))+1)
