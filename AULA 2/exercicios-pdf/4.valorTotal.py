#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

appleNum = int(input("Digite o número de maçãs que deseja comprar: "))
valorTotal = 0

if (appleNum < 12) and (appleNum > 0):
    valorTotal = appleNum * 0.30
else:
    valorTotal = appleNum * 0.25

print(f"Você comprou {appleNum} por R${(valorTotal):.2f}")