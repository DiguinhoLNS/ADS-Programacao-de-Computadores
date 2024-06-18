comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

perimetro = (comprimento + largura) * 2
area = comprimento * largura

print(f"\nO retângulo que tem, {comprimento} de comprimento e {largura} de largura possui:")
print("Perímetro:", perimetro)
print("Área:", area)