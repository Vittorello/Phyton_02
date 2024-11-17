# Classificador de Números
try:
    numero = int(input("Digite um numero: "))
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Número par")
    elif numero % 2 != 0:
        print("Número ímpar")
except ValueError:
    print("Digite um número válido.")