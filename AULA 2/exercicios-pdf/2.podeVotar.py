# Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

yearBirthday = int(input("Digite o seu ano de nascimento: "))
yearCurrently = int(input("Digite o seu ano atual: "))

validate = yearCurrently - yearBirthday

if validate >= 16:
    print(f"Você tem {validate} anos, pode votar")
else:
    print(f"Você tem {validate} anos, NÃO pode votar")