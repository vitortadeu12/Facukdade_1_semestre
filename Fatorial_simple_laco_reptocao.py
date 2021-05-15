soma = 1
n = int(input())
while n > 0:
    soma *= n
    n -= 1
print(soma)


# no n -=1 ele pega o valor de n e vai decompando até chegar no 0 que é quando acaba
# o laço de repetição