# PIZZA P = 35, PIZZA M = 40, PIZZA G = 45 | ADICIONAL P: 3, ADICIONAL M e G: 5 | BORDA: 3

tamanhoPizza = input("Escolha o tamanho da pizza [P] [M] [G]")
preco = 0
adicional = 0
borda = 3

if tamanhoPizza == "P":
    preco = 35
    adicional = int(input("Você vai querer adicional? [1] SIM , [2] NÃO: "))
    if adicional == 1:
        adicional = 3
        preco += adicional
    else:
        print("Sem adicional")

elif tamanhoPizza == "M":
    preco = 40
    adicional = int(input("Você vai querer adicional? [1] SIM , [2] NÃO: "))
    if adicional == 1:
        adicional = 5
        preco += adicional
    else:
        print("Sem adicional")

elif tamanhoPizza == "G":
    preco = 45
    adicional = int(input("Você vai querer adicional? [1] SIM , [2] NÃO: "))
    if adicional == 1:
        adicional = 5
        preco += adicional
    else:
        print("Sem adicional")

borda = int(input("Vai querer borda recheada [1] SIM, [2] NÃO: "))
if borda == 1:
    preco += borda
else:
    print("Sem borda recheada")

print(f"Sua pizza é tamanho {tamanhoPizza}, você pagará {preco}R$ no total")