notas = []
soma = 0

while True:
    nota = float(input("Digite uma nota, ou 0 pra sair: "))

    if(nota == 0):
        break

    notas.append(nota)
    soma += nota

media = soma / len(notas)

print(f"A média das notas é {media}")