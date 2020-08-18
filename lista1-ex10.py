# Faça um programa que leia a quantidade de dias, horas, minutos e segundos.
# Calcule o total em segundos.

dias = int(input())
horas = int(input())
minutos = int(input())
segundos = int(input())

dias = dias * 86400
horas = segundos * 3600
minutos = segundos * 60
segundos = segundos + dias + horas + minutos
print(segundos)
