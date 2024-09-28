# 15. Mr. Datan gostaria de sacar uma quantia X de sua conta, porém o caixa está com defeito, e só esta aceitando Mr. Datan sacar se o numero X for múltiplo de 5, suponha que a conta de Mr . Datan tem dinheiro suficiente para efetuar essa transação, (incluindo a taxa do banco que é de 0.50 R$ pra cada transação ) vamos pedir para o usuário digitar o valor dessa conta em uma outra variável que vamos chamar de valorConta. Calcule a conta de Mr. Datan após sacar o dinheiro: trabalhe com as seguintes condições:
# O valor sacado deve ser maior que 20 e menor ou igual a 2000
# O valor da conta não pode ser negativo e deve ser maior ou igual a 2000.
valorConta = float(input("Digite o valor que você tem na conta = "))
sacarDinheiro = float(input("Digite o valor que deseja sacar (OBS: Apenas múltiplos de 5: ) = "))
taxa = 0.50

if valorConta <= 2000 and valorConta > 0:
    if valorConta >= sacarDinheiro:
        sacarDinheiro = float(input("Digite o valor que deseja sacar (OBS: Apenas múltiplos de 5: ) = "))
        if sacarDinheiro >= 20 and sacarDinheiro <= 2000:
            if sacarDinheiro % 5 == 0:
                valorConta = (valorConta - sacarDinheiro)*taxa
                print(f"Você sacou {sacarDinheiro}R$! O valor atual da sua conta é {valorConta}")
            else:
                print(f"O saque de {sacarDinheiro}R$ foi recusado! O caixa está com problema, aceitamos apenas valores múltiplos de 5!")
        else:
            print("Não aceitamos valores maior que 2000R$ ou menores que 20R$")
       
    else:
        print("Vish fih, dá certo não. Só se fizer empréstimo!")

else:
    print(f"Você declarou {valorConta}R$! O limite da sua conta é de 2000R$")