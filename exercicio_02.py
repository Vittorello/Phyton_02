# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

valor_01 = float(input("Digite um valor: "))
valor_02 = float(input("Digite outro valor: "))

resto = valor_01 % valor_02

sobra = int(resto * 5)

print(sobra)