# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada

import math

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = float(math.pi * raio_do_circulo ** 2)

print(f"Esse é a área do circulo: {area_do_circulo:.2f}")