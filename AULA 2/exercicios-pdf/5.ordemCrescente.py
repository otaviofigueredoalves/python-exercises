# Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

value1 = int(input("Digite o primeiro valor: "))
value2 = int(input("Digite o segundo valor: ")) 
value3 = int(input("Digite o terceiro valor: ")) 
auxiliar = value1


if (value1 != value2) and (value1 != value3) and (value2 != value3):

    if value2 < value1:
        auxiliar = value2
        value2 = value1
        value1 = auxiliar

    if value3 < value1:
        auxiliar = value3
        value3 = value1
        value1 = auxiliar

    if value3 < value2:
        auxiliar = value2
        value2 = value3
        value3 = auxiliar

    
    print(f"{value1} -> {value2} -> {value3}")

else:
    print("USE VALORES DIFERENTES!")






