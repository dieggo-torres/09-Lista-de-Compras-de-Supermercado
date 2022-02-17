# Lista vazia
compras = []

while True:
    produto = input("Produto: ")
    if produto == "":
        break
    else:
        qtde = input("Qtde: ")
        compras.append([produto, qtde])

print("-" * 25)
print("{:^12}|{:^12}".format("PRODUTO", "QTDE"))
print("-" * 25)

for compra in compras:
    produto, qtde = compra
    print("{:<12}|{:>12}".format(produto, qtde))

print("-" * 25)
