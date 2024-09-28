# Utilizando um pouco dos conhecimentos que vimos até agora com os
# comandos Print e Input, vamos fazer um programa que conte a quantidade
# de letras do nome de uma pessoa, e para isso será necessário utilizar um
# pouco do Google para pesquisar qual comando é responsável por contar a
# quantidade de letras.

usuario = input("Digite seu nome: ") #pede o nome ao usuário
lettersCount = len(usuario.replace(" ", "")) #substitui o espaço em branco por uma string vazia (então, em vez de 'Otavio F)[8 letras], vai retornar 'OtavioF'[7 letras]
print(f"{usuario}, o seu nome tem: {(lettersCount)}") #imprime o nome do usuário e a quantidade de caracteres do seu nome