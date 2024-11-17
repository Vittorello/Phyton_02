# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    div_valor_01 = int(input("Digite um valor: "))
    div_valor_02 = int(input("Digite outro valor: "))
    valor_total_div = div_valor_01 // div_valor_02
    print("O valor da divisão é", valor_total_div)

except:
    print("Não é possivel dividir por zero")