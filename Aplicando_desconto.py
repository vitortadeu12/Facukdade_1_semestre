'''Maria, além de comerciante, é também uma excelente negociante! Por isso, sempre consegue descontos em suas compras.
Ao visitar uma loja, Maria recebeu a seguinte proposta de um vendedor: "Se comprar minha mercadoria concederei um desconto fixo de 10% e mais 1% a cada unidade comprada".
Infelizmente, Maria está cansada de tanto trabalhar e não quer fazer os cálculos sozinha para descobrir qual será o valor da compra antes e depois do desconto,
por isso pediu sua ajuda.
Você criará um programa que receberá como entradas um número real, indicando o preço da mercadoria comprada por Maria, e um número inteiro,
indicando a quantidade de mercadoria comprada, e exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.'''

n = float(input())
n1 = int(input())
aplicado = n1 / 100
total = n * n1
desconto = ((aplicado + 0.10) * total)
final = total - desconto
print(f'{total:.2f}')
print(f'{final:.2f}')
