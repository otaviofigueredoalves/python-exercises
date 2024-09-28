#9. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
maior = num1

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 < num2:
        maior = num2
    if num1 < num3:
        maior = num3
    if num2 < num3:
        maior = num3
    print(f"O maior valor é {maior}")
else:
    print("NÃO USE VALORES IGUAIS!")
        