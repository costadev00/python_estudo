# 1) Faça um programa que leia dois números e calcule:
# a)
# b)
# c)
# d)
# e)
# f)
# g)
# A soma.
# A subtração.
# A multiplicação.
# A divisão.
# A exponenciação.
# O módulo.
# O resto.
import math

n1 = input()
n2 = input()
n1 = int(n1)
n2 = int(n2)
soma = n1 + n2
print(f"Soma = {soma}")
subt = n1 - n2
print(f"Subtracao = {subt}")
multi = n1 * n2
print(f"Multiplicacao = {multi}")
divs = n1 / n2
print(type(divs))
print(f"Divisao = {divs}")
expo = math.pow(n1, n2)
print(f"{n1} elevado a {n2} = {expo}")
rest = n1 % n2
print(f"Resto da divisao entre {n1} {n2} = {rest}")

