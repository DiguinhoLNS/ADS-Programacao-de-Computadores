tipoDiaria = input("Digite o tipo de diária (S, D ou T): ")
qtdDias = int(input("Digite a quantidade de dias: "))
mensagem = ""

if tipoDiaria != "S" and tipoDiaria != "D" and tipoDiaria != "T":
    print("Tipo de diária inválido")
else:
    if tipoDiaria == "S":
        valorDiaria = 255.50
    elif tipoDiaria == "D":
        valorDiaria = 305.50
    else:
        valorDiaria = 360.50

    valorTotal = qtdDias * valorDiaria
    
    print(f"O valor total de {qtdDias} diárias é de R$ {valorTotal}")