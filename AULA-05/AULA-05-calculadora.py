valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = valor1 + valor2
elif operacao == "-":
    resultado = valor1 - valor2
elif operacao == "*":
    resultado = valor1 * valor2
elif operacao == "/":
    resultado = valor1 / valor2

print(f"O resultado da operação é {resultado}")