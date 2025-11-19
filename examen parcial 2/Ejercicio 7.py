#Haz un programa que pida un numero y determina si es par o impar.
numero = int(input("Ingresa un numero entero: "))
if numero == 0:
    numero = int(input("Ingresa un numero entero (no 0): "))
if numero < 0:
        numero = int(input("Ingresa un numero entero (positivo): "))

if numero % 2 == 0:
        print("El numero", numero, "es par.")
else:
        print("El numero", numero, "es impar.")