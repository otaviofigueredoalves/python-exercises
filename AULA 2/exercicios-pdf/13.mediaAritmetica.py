#13 . Ler o valores de 4 notas escolares bimestrais de um aluno , representada pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD1) desse aluno e apresentar a mensagem "Aprovado " se a media obtida for maior ou igual a 7; Caso o contrario , o programa deve solicitar a quinta nota (Nota de Exame, representada pela variável NE) do aluno e calcular uma nova média aritmética variável (MD2) entre a nota de exame e a primeira média aritmética . se o valor da nota média for maior ou igual a 5, apresentar a mensagem "aprovado em exame" caso o contrario, apresentar a mensagem "Reprovado". Informar também após a apresentação das mensagens o valor da média obtida pelo aluno.

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))

if (n1 >= 0 or n2 >= 0 or n3 >= 0 or n4 >= 0) and (n1 <= 10 and n2 <= 10 and n3 <= 10 and n4 <= 10):
    md1 = (n1+n2+n3+n4)/4

    if md1 < 7:
        print("RECUPERAÇÃO")
        ne = int(input("Digite a nota da recuperação: "))
        md2 = (md1 + ne)/2

        if md2 >= 5:
            print(f"Aprovado em exame, sua média foi {md2}")
        else:
            print(f"Reprovado, sua média foi {md2}")
    else:
        print(f"Aprovado, sua média foi {md1}")

else:
    print("NOTA INVÁLIDA!")


