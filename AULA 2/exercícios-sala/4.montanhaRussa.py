print("SEJA BEM-VINDO A MONTANHA RUSSA IGD")
altura = int(input("Digite sua altura em cm: "))
count = 0
if altura > 120:
    altura = altura / 100
    print(f"Sua altura é {altura} metros, você pode entrar na montanha russa")
    
    idade = int(input("Digite sua idade: "))
    if idade <= 12:
        count+=5
        print(f"Você irá pagar na entrada:{count}")
    elif idade <= 18:
        count+=15
        print(f"Você irá pagar na entrada {count}")
    elif idade > 60: 
        print("Você não paga naaaada!")

    pacote = print(input("Você vai querer o pacote? [1] SIM | [2] NÃO : "))

    if pacote == 1:
        count += idade
    else:
        count = count
   
    print(f"Você pagará {count} no total")

else:
    altura = altura / 100
    print(f"Sua altura é {altura}, você não pode entrar na montanha russa")



