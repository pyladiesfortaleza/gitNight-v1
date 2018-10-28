"""
Criado por: @gabrielabezerra
Resolvido por:
Resolvido por: Jessyka

Crie um programa que recebe a base e a altura de um triangulo, e retorna a sua área.

@ -11,3 +11,10 @@ $ areatriangulo.py 6 5
Area = 15

"""

altura = int(input('Digite o valor da altura: '))
base = int(input('Digite o valor da base: '))

area = (altura*base)/2
	    
print('A area do triangulo e %0.2f' %area) 
