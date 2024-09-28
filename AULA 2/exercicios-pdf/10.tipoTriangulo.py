#10. Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que: 
# − Triângulo Equilátero: possui os 3 lados iguais.
# − Triângulo Isóscele: possui 2 lados iguais.
# − Triângulo Escaleno: possui 3 lados diferentes.

lado1 = int(input("Digite o valor do primeiro lado: "))
lado2 = int(input("Digite o valor do segundo lado: "))
lado3 = int(input("Digite o valor do terceiro lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("É UM TRIÂNGULO EQUILÁTERO!")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É UM TRIÂNGULO ISÓSCELES!")
    else:
        print("É UM TRIÂNGULO ESCALENO!")
else:
    print("NÃO USE VALORES NEGATIVOS!")
