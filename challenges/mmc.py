"""
Criado por: @gabrielabezerra
Resolvido por: @jessyka

Crie um programa que calcula o MMC de dois números naturais.


Exemplo:
$ mmc.py 10 22
MMC = 110


"""

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2

for i in range(maior):
    aux = num1 * i
    if (aux % num2) == 0:
        mmc = aux

print(mmc)
