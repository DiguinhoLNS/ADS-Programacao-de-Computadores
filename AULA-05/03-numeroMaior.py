valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print("O maior valor é o primeiro: %d" % valor1)
elif valor2 > valor1 and valor2 > valor3:
    print("O maior valor é o segundo: %d" % valor2)
else:
    print("O maior valor é o terceiro: %d" % valor3)