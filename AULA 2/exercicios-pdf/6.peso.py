#Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes 
# Fórmulas:
# - para homens: (72.7 * Altura) – 58
# - para mulheres: (62.1 * Altura) – 44.7

gender = int(input("Informe seu sexo: [1]Feminino | [2] Masculino = "))
height = float(input("Informe sua altura em metros. (Ex: 1.62) = "))

if gender == 1 or gender == 2 or height <= 0:
    if gender == 1:
        gender = 'Mulher'
        weight = (72.7 * height) - 58
    else:
        gender = 'Macho'
        weight = (62.1 * height) - 44.7

    print(f"Você é {gender}. Seu peso é {weight:.2f}kg")
else:
    print("DIGITE UM VALOR VÁLIDO!")