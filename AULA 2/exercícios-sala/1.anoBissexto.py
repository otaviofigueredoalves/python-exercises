#Para ser bissexto, o ano deve ser: Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero; Não pode ser divisível por 100.
print("VERIFICADOR DE ANO BISSEXTO!")
ano = int(input("Digite o ano que deseja verificar: "))

if (ano % 4) == 0 and (ano / 100) != 0 or (ano % 4) == 0 and (ano / 100) != 0 (ano % 400) == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")