valorCompra = float(input("Digite o valor da compra"))
qtdParcelas = int(input("Digite a quantidade de parcelas"))

procentagemCompra = (valorCompra / 100) 
juros = 0.0

if(qtdParcelas == 2):
    juros = procentagemCompra * 3
elif(qtdParcelas == 4):
    juros = procentagemCompra * 7
elif(qtdParcelas == 6):
    juros = procentagemCompra * 9
elif(qtdParcelas == 8):
    juros = procentagemCompra * 12

valorTotal = valorCompra + juros

