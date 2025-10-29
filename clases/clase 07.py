#Ejercicio 03: Haz un programa en python que pida un numero entero y muestre cuantos numeros pareas hay desde 1 hasta ese numero (incluyendolo si es par)

# conteo_pares = 0
# #solicitar al usuario que ingrese un numero entero
# numero = int(input("Ingrese un número entero: "))

# for i in range(1, numero + 1):
#     if i % 2 == 0:
#         conteo_pares += 1
#     print(i)

# print(f"Hay {conteo_pares} números pares desde 1 hasta {numero}.")

#Ejercicio 4: Haz un programa en python que pida un numero y calcule el factorial de ese numeero utilizando un ciclo for

# numero = int(input("Ingrese un número para calcular su factorial: "))
# factorial = 1
# for i in range(1, numero + 1):
#     factorial *= i
# print(f"El factorial de {numero} es {factorial}.")

#Blucle While
# while condicion:
#    bloque de codigo

#Ejercicio 1:Haz un programa que pida al usuario ingresar una contraseña hasta que ingrese la correcta, y que tenga maximo 5 intentos.

contrasena_correcta = "Credinalga"
intentos = 0
max_intentos = 5
contrasena = input("Ingrese la contraseña: ")
while (intentos < max_intentos) and (contrasena != contrasena_correcta):
    print("Contraseña incorrecta. Intente de nuevo.")
    intentos += 1
    contrasena = input("Ingrese la contraseña: ")

if intentos == max_intentos:
    print("Ha excedido el número máximo de intentos., acceso denegado.")
else:
    print(f"Contraseña correcta, acceso concedido. Intentos realizados {intentos}.")