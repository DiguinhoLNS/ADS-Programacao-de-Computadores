nomes = []

for i in range(5):
    nome = input("Digite o nome: ")

    nomes.append(nome)

digito = int(input("Digite um número de 0 a 4 que deseja buscar: "))

print(f"{nomes[digito]}")