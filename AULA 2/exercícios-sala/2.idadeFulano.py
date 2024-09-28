#Imprimir na tela se pelo menos uma pessoa é maior ou menor de idade
pessoa1 = int(input("Digite a idade da pessoa1: "))
pessoa2 = int(input("Digie a idade da pessoa2: "))

if pessoa1 >= 18 or pessoa2 >= 18:
    print("Uma delas é maior de idade ")

else:
    print("Uma delas ou as duas não são maiores de idade")