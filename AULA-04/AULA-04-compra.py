valorCompra = float(input("Digite o valor da compra: "))

if valorCompra > 200:
    desconto = (valorCompra / 100) * 20
    novoValorCompra = valorCompra - desconto

    print(f"Você ganhou um desconto de R$ {desconto} e o novo valor da compra é R$ {novoValorCompra}")
else:
    print(f"O valor da compra é R$ {valorCompra}")