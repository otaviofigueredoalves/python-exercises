#14. Pedir ao usuário para atribuir valores a 5 variáveis (A,B,C,D e E) e apresentar o maior e menor dos números informados.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))

maior = max(a,b,c,d,e)
menor = min(a,b,c,d,e)
#NÃO CONSEGUI FAZER SEM UTILIZAR ESSAS FUNÇÕES

print(f"O maior valor é {maior} e o menor valor é {menor}")
