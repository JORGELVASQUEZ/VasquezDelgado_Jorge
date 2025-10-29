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

#Ejercicio 2: Haz un programa que pida al usuario ingresar numeros positivos  y que se detenga cuando ingrese un numero negativo.
numero = float(input("Ingrese un número positivo (o un número negativo para salir): "))

while numero >= 0:
    numero = float(input("Ingrese un número positivo (o un número negativo para salir): "))
print("Número negativo ingresado. Programa terminado.")

#Ejercicio 3: Haz un programa que sume todos los numeros que ingrese el usuario hasta que ingrese un 0.

suma = 0
numero = float(input("Ingrese un número para sumar (o 0 para terminar): "))

while numero != 0:
    suma += numero
    numero = float(input("Ingrese un número para sumar (o 0 para terminar): "))
print(f"La suma total de los números ingresados es: {suma}.")

# ! simbolo de diferente
