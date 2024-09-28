# Crie um programa usando matemática e f-Strings que nos diga quantos dias, semanas, meses nos restam se vivermos até os 90 anos.

# a mensagem final deve ser

# Você tem x dias, y semanas e z meses restantes.

age = input("Digite sua idade: ")
age = int(age)
# ANO
ano = (90 - age)
# MESES
meses = (ano * 12)
#SEMANAS
semana = (ano * 52)
# DIAS
dias = (ano * 365.2)

print(f"SUA IDADE É: {age} | VOCÊ TEM {ano} ANOS, {meses} MESES, {semana} SEMANAS e {round(dias)} DIAS")

# age = int(age)
# calcMorte = 90 - age
# dias = calcMorte * 365.3
# print(f"dias {dias}")
