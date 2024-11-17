# Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except: ValueError
print("Por favor, digite um número válido para a temperatura.")