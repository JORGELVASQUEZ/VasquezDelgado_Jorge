#programa que oida un numero entero positivo y muestre su raiz cuadrada, raiz cubica 
#potencia al cuadrado y potencia al cubo
import math

numero = int(input("ingresa un numero entero positivo: "))
raizcuadrada = math.sqrt(numero)
raizcubica = numero ** (1/3)
potenciacuadrado = pow(numero, 2)#numero ** 2
potenciacubica = pow(numero, 3)#numero ** 3

print(f'la raiz cuadrda de {numero} es: {raizcuadrada}.')
print(f'la raiz cubica de {numero} es: {raizcubica}.')
print(f'la potencia al cuadrado de {numero} es: {potenciacuadrado},')
print(f'la potencia al cubo de {numero} es: {potenciacubica}.')

