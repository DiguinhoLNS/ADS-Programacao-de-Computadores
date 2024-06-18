print("Responda com 1 para sim e 0 para não!!!")

jobSegunda = bool(int(input("Você trabalhou na segunda-feira? ")))
jobQuarta = bool(int(input("Você trabalhou na quarta-feira? ")))
jobSexta = bool(int(input("Você trabalhou na sexta-feira? ")))
mensagem = ''

if jobSegunda and jobQuarta and jobSexta:
    mensagem = "Tv de 55 polegadas 4K"

elif jobSegunda and jobQuarta:
    mensagem = "Tv de 32 polegadas"

elif jobSegunda:
    mensagem = "Tv de tubo"

else:
    mensagem = "Nada"

print(f"Você consegue comprar, {mensagem}!")