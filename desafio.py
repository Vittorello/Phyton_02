# Cálculo de Bônus com Entrada do Usuário
try:
    nome_usr = input("Digite seu nome: ")

    if len(nome_usr) == 0:
        raise ValueError("O nome não pode estar vazio. ")

    elif any(char.isdigit() for char in nome_usr):
        raise ValueError("O nome não deve conter números. ")

    else:
        print("Nome válido: ",nome_usr)

except ValueError as e:
    print(e)
    exit()

try:
    salario_usr = int(input("Digite o valor do seu salário: "))

    if salario_usr < 0:
        raise ValueError("Digite um valor positivo para o salário. ")
    
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

try:
    bonus_usr = float(input("Digite o valor do seu bônus: "))

    if bonus_usr < 0:
        print("Digite um valor positivo para o bônus. ")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

constante_bonus = int(1000)

calculo_bonus = int(constante_bonus + salario_usr * bonus_usr)

print(f"Olá {nome_usr} o seu bônus foi de {calculo_bonus}")