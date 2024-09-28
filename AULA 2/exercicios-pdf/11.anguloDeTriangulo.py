#11.Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo , Retângulo ou Obtusângulo . Sendo que:
# − Triângulo Retângulo: possui um ângulo reto. (igual a 90o)
# − Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90o)
# − Triângulo Acutângulo: possui três ângulos agudos. (menor que 90o)

angulo1 = int(input("Digite o valor do primeiro angulo: "))
angulo2 = int(input("Digite o valor do segundo angulo: "))
angulo3 = int(input("Digite o valor do terceiro angulo: "))

if (angulo1 + angulo2 + angulo3) != 180:
    print("NÃO É UM TRIÂNGULO")
elif (angulo1 + angulo2) == 90 or (angulo1 + angulo3) == 90 or (angulo2 + angulo3) == 90:
    print("O triângulo é RETÂNGULO!")
elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("O triângulo é ACUTÂNGULO!")
else:
    print("O triângulo é OBTUSÂNGULO")


#VALORES PARA TESTAR: 
# (130;30;20)
# (30;70;80)
# (90;40;50)
# (90;20;30)