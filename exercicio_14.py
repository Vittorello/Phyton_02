# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato DD/MM/AAAA: ")
data_dia_mes_ano = data.split("/")

print(f"O dia é: {data_dia_mes_ano[0]}")
print(f"O mês é: {data_dia_mes_ano[1]}")
print(f"O ano é: {data_dia_mes_ano[2]}")