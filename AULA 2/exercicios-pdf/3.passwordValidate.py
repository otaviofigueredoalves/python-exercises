# Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
#ACESSO PERMITIDO caso a senha seja válida.
#ACESSO NEGADO caso a senha seja inválida.

print("CADASTRO DO USUÁRIO")
user = input("Digite seu nome: ")
password = int(input("Digite sua senha: "))


print("LOGIN")

userLogin = input("Insira seu nome: ")
passwordLogin = int(input("Insira sua senha: "))
if(userLogin == user and passwordLogin == password):
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")