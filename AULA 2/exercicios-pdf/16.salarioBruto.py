#1. Escreva um programa Python que pede para o usuário informar o valor do seu Salário Bruto. Sabendo-se que o desconto do imposto de renda e do INSS variam de acordo com a faixa salarial, subtraindo também 3% do imposto sindical que o usuário devera optar se deseja ou não, calcule e mostre o total do salário liquido a receber.
#2. Atenção: Salário Bruto é o salário sem quaisquer descontos, enquanto Salário Líquido é o salário final, já com todos os descontos aplicados. Trabalhe com as seguintes tabelas.

#INSS
#Até 1.412,00 -> 7,50% x
#De 1412,01 até 2.666,68 -> 9% x
#De 2666,69 até 4.000,03 -> 12% x
#De 4.000,04 até 7.786,02 -> 14% x

#IOR
#Até 2.112,00 -> 0% x
#De 2.112,01 até 2.826,65 -> 7,50% x
#De 2.826,66 até 3.751,05 -> 15% x
#De 3.751,06 até 4.664,68 -> 22,50% x
#Acima de 4.664,68 -> 27,50% x 

salarioBruto = float(input("Digite o valor do seu salário bruto: "))

if salarioBruto < 600 and salarioBruto > 0: 
    print(f"{salarioBruto}R$ não é salário de gente, denuncia essa empresa!")
elif salarioBruto == 0:
    print("Procura um emprego, rapaz!")
elif salarioBruto > 0:

    impostoSindical = 3/100
    pagarImposto = ''
    ior = 0

    if salarioBruto > 7768.02:
        inss = 20/100
        ior = 27.50/100

    if salarioBruto > 4000.04 and salarioBruto <= 7768.02:
        inss = 14/100
        if salarioBruto > 4664.68:
            ior = 27.50/100

    elif salarioBruto >= 2666.09 and salarioBruto <= 4664.68:
        if salarioBruto >= 3751.06:
            ior = 22.50/100
        if salarioBruto <= 4000.03:
            inss = 12/100

    elif salarioBruto >= 1412.01 and salarioBruto <= 3751.05:
        if salarioBruto >= 2826.66:
            ior = 15/100
        if salarioBruto <= 2666.08:
            inss = 9/100
    elif salarioBruto <= 2826.65 and salarioBruto >= 600:
        inss = 7.50/100
        if salarioBruto >= 2112.00:
            ior = 0
    else: 
        inss = 0
        ior = 0

    if salarioBruto >= 600:
        pagarImposto = input("Você deseja pagar imposto sindical?: [SIM] ; [NAO] = ").lower()

    if pagarImposto != 'sim':
        impostoSindical = 0
        taxa = ior + inss 
    else:
        taxa = ior + inss + impostoSindical
        
    salarioLiquido = salarioBruto - (salarioBruto * taxa)

    print(f"Seu salário bruto é de {salarioBruto:.2f}R$. Por conta da taxa de {(taxa*100):.2f}%, sendo o IOR: {(ior*100):.2f}% | INSS: {(inss*100):.2f}% |IMPOSTO SINDICAL: {(impostoSindical*100)}%. Seu salário líquido é de: {(salarioLiquido):.2f}R$")
else:
    print("Ocorreu um problema!")