#1. Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando. Imprime en consola un coteo de números pares y de números impares.
print("Ejercicio 1")
numero = int(input("Ingresa un número: "))
contador_pares = 0
contador_impares = 0
for i in range(1, numero + 1):
    print(i)
    if i % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")

print("________________________________________________")
#2. Haz un programa que pida al usuario ingresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicando que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que le faltan para llegar poder votar.
print("Ejercicio 2")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(f"{nombre}, tienes la edad sufiente para votar.")
else:
    años_faltantes = 18 - edad
    print(f"{nombre}, no tienes la edad suficiente para votar. Te faltan {años_faltantes} años.")
print("________________________________________________")

#3. Haz un programa en Python que pida al usuario ingresar un número, y muestre su tabla de multiplicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc).
print("Ejercicio 3")
numero_usuario = int(input("Introduce un numero: "))
print(f"Multiplicaciones del {numero_usuario} por numeros pares del 1 al 20: ")
print("________________________________")
for i in range(0, 21, 2):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')
print("________________________________")

#4. Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo, pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes), de los 5 números ingresados, muestra cuántos fueron mayores que 10.
print("Ejercicio 4")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
num4 = float(input("Ingresa el cuarto número: "))
num5 = float(input("Ingresa el quinto número: "))
contador_mayoresde10 = 0
if num1 > 10:
    contador_mayoresde10 += 1
if num2 > 10:
    contador_mayoresde10 += 1
if num3 > 10:
    contador_mayoresde10 += 1
if num4 > 10:
    contador_mayoresde10 += 1
if num5 > 10:
    contador_mayoresde10 += 1
print(f"Numeros mayores a 10: {contador_mayoresde10}")
print("________________________________________________")
#5. Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma.
print("Ejercicio 5")
suma_pares = 0
for i in range(0, 101, 2):
    suma_pares += i
print(f"La suma de los numeros pares del 1 al 100 es: {suma_pares}")
print("________________________________________________")
#6. Haz un programa que genera la tabla de multiplicar de un número ingresado. Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50, cuántos menores que 50 y cuántos iguales a 50.
print("Ejercicio 6")
num = int(input("Ingrese un numero para generar su tabla de multiplicar: "))
contador_mayores50 = 0
contador_menores50 = 0
contador_iguales50 = 0
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    if resultado > 50:
        contador_mayores50 += 1
    elif resultado < 50:
        contador_menores50 += 1
    else:
        contador_iguales50 += 1
print(f"Numeros mayores a 50: {contador_mayores50}")
print(f"Numeros menores a 50: {contador_menores50}")
print(f"numeros iguales a 50: {contador_iguales50}")
print("________________________________________________")
print(" : )")
