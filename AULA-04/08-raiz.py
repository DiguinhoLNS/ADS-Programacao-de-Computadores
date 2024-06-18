import math

valor = int(input("Digite um número: "))

if valor > 0:
    raiz = math.sqrt(valor)
    
    print(f"A raiz quadrada de {valor} é {raiz}")
else:
    print("ão é possível calcular raís quadrada de números negativos")