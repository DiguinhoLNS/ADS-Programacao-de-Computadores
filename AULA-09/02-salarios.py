meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

totalSalario = 0

salarios = []

for i in range(12):
    salario = float(input(f'Digite o salário do mês de {meses[i]}: '))

    salarios.append(salario)
    totalSalario += salario

decimoTerceiro = totalSalario / 12
ferias = decimoTerceiro * (1/3)

print(f"O total de salários recebidos no ano foi de R${totalSalario:.2f}")
print(f"O valor do décimo terceiro é de R${decimoTerceiro:.2f}")
print(f"1/3 de férias: R${ferias:.2f}")