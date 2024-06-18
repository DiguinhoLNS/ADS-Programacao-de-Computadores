notas = [6, 7, 6.5, 4.8, 8]
soma = 0

for i in notas:
    soma += i

media = soma / len(notas)

print(f'A média do aluno foi de {media:.2f}')