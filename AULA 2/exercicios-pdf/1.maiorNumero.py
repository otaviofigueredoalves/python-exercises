# 1. Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
maiorN = ""

if valor1 > valor2:
    maiorN = valor1
else:
    maiorN = valor2

print(f"O maior número é: {maiorN}")