#7. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
# − Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área 
# − Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
# − Se o número de lados for igual a 5 escrever PENTÁGONO.
import math

lados = int(input("Digite o número de lados de um polígono: [3] [4] ou [5] = "))

if lados == 3 or lados == 4 or lados == 5:
    if lados == 3:
        lado = int(input("Digite o valor do lado em cm = "))
        area = (lado ** 2 * math.sqrt(3))/4
        print(f"É um TRIÂNGULO com {area:.2f}cm²")
    elif lados == 4:
        lado = int(input("Digite o valor do lado em cm = "))
        area = lado ** 2
        print(f"É um QUADRADO com {area:.2f}cm²")
    else:
        print(f"É um PENTÁGONO")

else:
    print("VALOR INVÁLIDO")
    