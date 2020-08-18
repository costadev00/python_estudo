#  8) Modificando o exercício anterior, faça um programa que converta a temperatura
#  digitada em Fahrenheit para Celsius.

graus = float(input("Digite uma temperatura em Fahrenheit"))

celsius = (32 * graus - 32) * (5 / 9)
print(f"A temperatura em celsius: {celsius}")
