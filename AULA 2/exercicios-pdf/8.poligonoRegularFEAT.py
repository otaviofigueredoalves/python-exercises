#8. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso. 
# − Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO. 
# − Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

import math

lados = int(input("Digite o número de lados de um polígono: [3] [4] ou [5] = "))

if lados >= 3 and lados <=5:
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
elif lados < 3:
    print("NÃO É UM POLÍGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")

    