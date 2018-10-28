"""
Criado por: @gabrielabezerra
Resolvido por: @jessyka

Crie um programa que receve um número como entrada e verifica se ele é par ou impar.


Exemplo:

$ verificapar.py 20
par

$ verificapar.py 21
impar

"""
n = int(input("Digite um numero:"))

if n%2 == 0:
   print('Numero e par.')
else:
   print('Numero e impar.')
     
