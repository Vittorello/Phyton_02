# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

media_valor_01 = float(input("Digite um valor: "))
media_valor_02 = float(input("Digite outro valor: "))
media_constante = 2

soma = media_valor_01 + media_valor_02

media = soma // media_constante

print(f"A média é {media}")