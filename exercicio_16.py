# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

idade = int(input("Qual é a sua idade? "))
if idade >= 18 and idade <=65:
    print("Você é obrigado a votar!")
else:
    print("Você não é obrigado a votar!")


valor_1 = False
valor_2 = True

print (valor_1 and valor_2)