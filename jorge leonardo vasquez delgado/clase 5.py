#sintaxis condicionales 

#if condicion:
# intrucciones si la condicion es verdadera
#elif otra condicion:
#instrucciones si la otra condicion es verdadera
#else:
#instrucciones si ninguna condicion es verdadera

#ejercicio 1: programa que pida un numero y muestre si es positivio, negativo o cero
print("Ejercicio 1")
numero = float(input("ingrese un numero: "))

if numero > 0:
    print("Bloque if ejecutado.")
    print("El numero es positivo.")
elif numero < 0:
    print("Bloque elif ejecutado.")
    print("El numero es negativo.")
else:
    print("El bloque else ejecutado.")
    print("El es cero.")
print(" :)")

print("________________________________________")


#ejercicio 2: programa que pida 2 numeros y muestre cual es mayor o si son iguales.

print("ejercicio 2")
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

if num1 > num2:
    print("el primer numero es mayor.")
elif num1 < num2:
    print("el segundo numero es mayor")
else:
    print("ambos numeros son iguales")
print(" :)")

print("_______________________________________")

#ejercicio 3: haz un programa que pida una calificacion del 0 al 10 y muestre si esta aprobado o reprobado. toma en cuenta una calificacion mayor o igual a 6 como aprobatoria 

print("Ejercicio 3")
nombreAlumno = input("ingresa el nombre del alumno: ")
calificacion = float(input("ingresa la calificacion del alunmo (0-10): "))

if calificacion >= 6:
    print(f"El alumno {nombreAlumno} esta aprovado.")
else:
    print(f"El alumno {nombreAlumno} esta reprodado.")

print("______________________________________")

#ejercicio 4: haz un programa que pida la edad de una persona y muestre si puede votar (mayor o igual a 18 años) o no 

print("Ejercicio 4")

nombre = input("ingresa el nombre de la persona: ")
edadpersona = int(input("ingrese su edad: "))

if edadpersona >= 18:
    print(f"{nombre} tiene {edadpersona} años y puede votar.")
else:
    print(f"{nombre} tiene {edadpersona} años y no puede votar.")

print("______________________________________")