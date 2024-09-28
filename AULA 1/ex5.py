# Deve informar-lhes a interpretação do seu IMC com base no valor do IMC.



# Menores de 18,5 anos estão abaixo do peso

# Acima de 18,5, mas abaixo de 25, eles têm peso normal

# Acima de 25, mas abaixo de 30, ele esta ligeiramente acima do peso

# Acima de 30, mas abaixo de 35, ele está obeso


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura * altura)


# if imc < 18.5:
#     print(f"Seu peso é: {peso} | Sua altura é: {altura} | Seu IMC é: {round(imc,2)} | Você está abaixo do peso!")
# elif 18.5 <= imc < 25:
#     print(f"Seu peso é: {peso} | Sua altura é: {altura} | Seu IMC é: {round(imc,2)} | Você está com peso normal!")
# elif 25 > imc < 30:
#     print(f"Seu peso é: {peso} | Sua altura é: {altura} | Seu IMC é: {round(imc,2)} | Você está acima do peso!")
# elif 30 > imc < 35:
#     print(f"Seu peso é: {peso} | Sua altura é: {altura} | Seu IMC é: {round(imc,2)} | Você está obeso, Big Smoke!")
# else:
#     print("VALOR INVÁLIDO, TENTE NOVAMENTE")
imcBaixoP = imc < 18.5,
imcNormalP = 18.5 <= imc < 25,
imcAcimaP = 25 > imc < 30,
imcObesoP = 30 > imc < 35,


imcTrue =  input(f"Seu IMC é: {round(imc,2)} | Em qual você se encaixa? [BAIXO PESO (IMC < 18.5)] | [PESO NORMAL(IMC < 18.5 E IMC < 25) | ACIMA DO PESO(IMC > 25 IMC < 30)] | VOCÊ ESTÁ OBESO!(IMC > 25 IMC < 30)]")
print(f"Seu peso é: {peso} | Sua altura é: {altura} | Seu IMC é: {round(imc,2)} | {imcTrue}")



