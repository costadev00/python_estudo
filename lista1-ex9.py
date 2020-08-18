# 9) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
# valor do salário e a porcentagem de aumento. Mostre o valor do aumento e do
# novo salário.

salario = float(input("Digite o salario:\n"))
porcentagem = int(input("Digite a porcentagem a ser aumentada \n"))
porcentagem = (porcentagem * salario) / 100
salario = salario + porcentagem
print(salario)
