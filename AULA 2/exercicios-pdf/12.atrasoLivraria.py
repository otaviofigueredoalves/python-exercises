#12. Escreva um programa onde o usuário de uma livraria passou alguns dias em atraso, pergunte quantos dias ele está em atraso e o multe de acordo com as regras a seguir:
# - Até 5 dias ele deverá pagar 2 reais por dia atrasado.
# - Entre 6 e 10 dias ele deverá pagar 3 reais por dia atrasado.
# - Entre 11 e 15 dias ele deverá pagar 4 reais por dia atrasado.
# - E após 15 dias ele deverá pagar 6 reais por dias atrasado.


print("Eita que o Raimundo Nonato vai me dar um carão")
diasAtraso = int(input("Seu figuereeeedo, atrasou quantos dias? : "))
multa = 0

if diasAtraso < 0:
    print("FIGUEREEEEEDO, INFORME UM DIA VÁLIDO!")

elif diasAtraso == 0:
    print("Parabéns Figueredo, entregou no dia! Não paga multa!")

else:
    if(diasAtraso >= 15):
        multa = 6
    elif(diasAtraso >= 11):
        multa = 4
    elif(diasAtraso >= 6):
        multa = 2
    print(f"Atrasou, Figueredo. Sua multa é de {multa}R$")
    
