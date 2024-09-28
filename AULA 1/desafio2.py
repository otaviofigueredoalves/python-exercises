# Crie um programa onde Calcule o valor total de uma conta, pergunte
# a porcentagem da gorjeta, decida entre 10, 12 ou 15 porcento, pergunte
# quantas pessoas irão dividir a conta e dê o resultado individual de cada
# pessoa que irá pagar a conta.

valorConta = float(input("Digite o valor da conta: "))
gorjeta = int(input("Digite quanto quer dar de gorjeta [10%] | [12%] | [15%]: "))
pessoasQtd = int(input("Digite a quantidade de pessoas que irão dividir: "))



gorjeta = ((valorConta) * (gorjeta))/100 #irá pegar o valor total atual, múltiplicar pelo percentual de gorjeta inserida pelo usuário e dividirá por 100(x% de valorConta)
valorTotal = valorConta + gorjeta #valor total atual será valorConta + Gorjeta
valorPessoa = valorTotal/(pessoasQtd) #valor total dividido pela quantidade de cabeças (se for esperto, recomendo pagar só o que comeu e ir embora)

print(f"VALOR TOTAL A PAGAR: R$ {round(valorTotal,2)} | GORJETA: {round(gorjeta,2)}R$ | Como somos {pessoasQtd} pessoas, vamos dividir para cada um pagar R${round(valorPessoa,2)}") #o método round() arredonda para 2 casas decimais. Ou seja, limitará resultados iguais ou acima de 2 casas decimais