def compra(preco, qtd, desconto):
    total = preco * qtd
    final = total - (total * desconto / 100)
    return final
preco = float(input('Preço:'))
qtd = int(input('Quantiade:'))
desconto = float(input('Desconto:'))
final = compra(preco, qtd, desconto)
print(f'O valor final é R${final:.2f}')