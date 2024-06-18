notas = []
soma = 0
numNotas = int(input("Quantas notas você vai inserir? "))

for i in range(numNotas):
    nota = float(input("Digite a nota: "))

    notas.append(nota)
    soma += nota

for i in range(numNotas):
    print(f"Nota {i + 1}: {notas[i]}")

media = soma / numNotas

print(f"A média das notas é {media}")