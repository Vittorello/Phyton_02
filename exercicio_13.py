# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Digite uma frase: "))

print(f"A sua fra sem espaços é: {frase.strip()}")