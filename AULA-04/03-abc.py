valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))

if (valorB < valorA and valorB < valorC):
    print(f"{valorB} é menor que {valorA} e {valorC}!")
else:
    print("O valor de B não é o menor número digitado!")