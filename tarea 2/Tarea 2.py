  # Ejercicio 1: Haz un programa en python que pida tres calificaciones y calcule su promedio con dos decimales (investiga lla fincion round) en phyton)
print("Ejercico 1")

calificacion1 = float(input("ingresa la primera calificación: "))
calificacion2 = float(input("ingresa la segunda calificación: "))
calificacion3 = float(input("ingresa la tercera calificación: "))
promedio = (calificacion1 + calificacion2 + calificacion3) /3

round = (promedio, 2)

print(f"el promedio es, {promedio}")

print("__________________________________________________")

#Ejercicio 2: Haz un programa en Python que calcule el área de un círculo a partir de su radio.
print("Ejercicio 2")
import math

radio = float(input("Ingresa el radio de tu circulo: "))

potencia = math.pow (radio, 2)

area = (potencia * 3.1416)

print(f"El area del circulo es: {area}")

print("___________________________________________________")

#Ejercicio 3: Haz un programa en Python que calcule el perímetro de una circunferencia con base en su radio.
print("Ejercicio 3")
 
radio = float(input("Ingresa el radio de tu circunferencia: "))

perimetro = ((radio * 2) * 3.1416)

print(f"El perimetro de tu circunferencia es: {perimetro}")

print("_____________________________________________________")

#Ejercicio 4: Haz un programa en Python que convierta una cantidad de minutos a horas.
print("Ejercico 4")

minutos = int(input("Ingresa los minutos: "))

horas = (minutos / 60)

print(f"Las horas totales son: {horas}")

print("___________________________________________________")

#ejercicio 5: Haz un programa en Python que pida un precio y muestre el total con IVA del 16%.
print("Ejercicio 5")

precio = float(input("Ingresa el precio: "))

iva = (precio * .16)
precioiva = (precio + iva)

print(f"El precio con iva es: {precioiva}")
print("___________________________________________________")

#Ejercicio 6: Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico).
print("Ejercicio 6")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 < num2 < num3

print(f"¿Se cumple la expresión A < B < C? {resultado}")

print("______________________________________________________")

#Ejercicio 7: Haz un programa en Python que pida un número y muestre si está entre 10 y 20 (solo mostrando True o False).
print("Ejercicio 7")

num = float(input("Ingresa un numero: "))

numero = num>=10 and num<=20
print(f"¿El numero esta entre 10 y 20? {numero}")

print("_________________________________________________________")

#Ejercicio 8: Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False).
print("Ejercicio 8")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿Los tres numeros son iguales? {resultado}")

print("__________________________________________________________________")

#Ejercicio 9: Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False).
print("Ejercicio 9")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿Los tres numeros son iguales? {resultado}")

print("__________________________________________________________________")

#Ejercicio 10: Haz un programa en Python que pida el radio y la altura de un cilindro y muestre su volumen.
print("Ejercicio 10")

radio = float(input("Ingresa el radio de tu cilindro: "))
altura = float(input("Ingresa la altura de tu cilindro: "))

radiocuadrado = math.pow (radio, 2)
areabase = (radiocuadrado * 3.1416)
volumen = (areabase * altura)

print(f"El volumen del cilindro es: {volumen}")

print("________________________________________________________________")

print(" : ) ")