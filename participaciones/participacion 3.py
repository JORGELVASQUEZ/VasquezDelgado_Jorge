#1.- Pide nombres hasta que el usuario escriba la palabra "Fin". Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.
print("Ejercicio 1")
nombres = []
while True:
    nombre = input("Ingrese un nombre (escriba 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)
print(f"cantidad de nombres ingresados: {len(nombres)}")

print("___________________________________________________________")

#2.- Pide números hasta que el usuario escriba 0. Guarda los pares en una lista y los impares en otra. Al final, muestra cuantos números hay en cada lista. Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.
print("Ejercicio 2")
numeros_pares = []
numeros_impares = []
while True:
    numero = float(input("Ingrese un numero (0 para terminar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
print(f"los numeros pares son: {len(numeros_pares)}")
print(numeros_pares)
print(f"los numeros impares son: {len(numeros_impares)}")
print(numeros_impares)

print("______________________________________________________________")

#3.- Haz un programa que pida "Nombre" y "Calificación". Almacena todos estos datos en un diccionario. Posteriormente muestra: Promedio general, cantidad de aprobados y cantidad de reprobados.
print("Ejercicio 3")
diccionario_alumnos = {}
reprobados = 0
aprobados = 0

while True:
     nombre = input("introduce el nombre del alumno(fin para terminar): ")
     if nombre.lower() =="fin":
        break
     calificacion = float(input("introduce la calificacion del alumno: "))
     while(calificacion < 0 or calificacion > 10):
         calificacion = float(input(f"Calificacion invalida. Introduce la calificacion de {nombre} entre 0 y 10: "))
     diccionario_alumnos[nombre] = calificacion
     print (diccionario_alumnos)   
     for clave, valor in diccionario_alumnos.items():
        suma_calificaciones = sum(diccionario_alumnos.values())
        promedio = suma_calificaciones / len(diccionario_alumnos)
     if calificacion <= 6:
        reprobados += 1
     else:
         aprobados += 1
     print(f"El promedio de las calificaciones es: {promedio}")
     print(f"la cantidad de aprovados son: {aprobados}")
     print(f"la cantidad de reprobados son: {reprobados}")

print("_______________________________________________________________")

#4.- Pide una frase y cuenta cuántas vocales usa (a, e, i, o, u).
print("Ejercicio 4")
frase = input("Escribe una frase: ")
frase = frase.lower()
a = e = i = o = u = 0
for letra in frase:
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1
total = a + e + i + o + u
print("Total de vocales:", total)
print("A:", a)
print("E:", e)
print("I:", i)
print("O:", o)
print("U:", u)

print("____________________________________________________________________")
#5.- Haz un programa que pida un número, y crea una nueva lista sin duplicados.
print("Ejercicio 5")
lista_numeros = []

while True:
 finalizar = input("Escribe fin para salir o next para continuar: ")
 if finalizar.lower() =="fin":
    break
 numero = float(input("Ingrese un numero: "))

 lista_numeros.append(numero)
 lista_numeros_ordenada = list(set(lista_numeros))
 lista_numeros_ordenada.sort()
 print(lista_numeros_ordenada)

print("_______________________________________________________________")

#6.- Haz un programa que pida "Nombre" y "Calificaciones". Posteriormente calcula el promedio general, calificación mayor, calificación menor y muestra el nombre del mejor alumno. Agrega 5 nombres y calificaciones.
print("Ejercicio 6")

nombres = []
calificaciones = []
for i in range(5):
    nombre = input(f"Nombre del alumno {i+1}: ")
    calificacion = float(input(f"Calificación de {nombre}: ")) 
    nombres.append(nombre)
    calificaciones.append(calificacion)
promedio = sum(calificaciones) / len(calificaciones)
mayor = max(calificaciones)
menor = min(calificaciones)
mejor_alumno = nombres[calificaciones.index(mayor)]
print("Promedio general:", promedio)
print("Calificación más alta:", mayor)
print("Calificación más baja:", menor)
print("Mejor alumno:", mejor_alumno)
