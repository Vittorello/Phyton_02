# Calculadora Simples
try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operador = input("Digite um operador (+,-,*,/: )")
    if operador == '+':
        resultado = numero_1 + numero_2
    elif operador == '-':
        resultado = numero_1 - numero_2
    elif operador == '*':
        resultado = numero_1 * numero_2
    elif operador == '/' and numero_2 != 0:
        resultado = numero_1 / numero_2
    else: print("Operador inválido ou divisão por zero.")
    print("Resultado:",resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")