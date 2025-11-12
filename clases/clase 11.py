# #Ejercicio 3: Pide 6 nombres y muestra la lista numerada (1.nombre1, 2.nombre2, etc)
# lista_nombres = []  #declaramos una lista vacia para guardar los nombres
# for i in range(6):
#     nombre = input("Introduce un nombre: ")
#     lista_nombres.append(nombre)  #agregamos el nombre ingresado a la lista

# lista_nombres.sort()  #ordenamos la lista alfabeticamente

# for i, nombre in enumerate(lista_nombres, start=1):
#     print(f"{i}. {nombre}")  #mostramos la lista numerada

# #Ejercicio 4: Pide 8 numeroa, eliminma las repeticiones y muestra la lista sin duplicados ordenados de mayor a menor
# lista_numeros = []  #declaramos una lista vacia para guardar los numeros

# for i in range(8):
#     numero = int(input("Ingrese un numero: "))
#     lista_numeros.append(numero)  #agregamos el numero ingresado a la lista

# lista_numeros_ordenada = list(set(lista_numeros))  #eliminamos duplicados convirtiendo la lista en un conjunto y luego de vuelta a lista
# lista_numeros_ordenada.sort()
# print(lista_numeros_ordenada)

# #Ejercicio 5: Pide 10 calificaciones entre 0 y 10. Si alguna es menor a 6, añade al conteo de reprobados. al final muestra cuantas aprobaron y cuantas reprobaron.
# lista_aprobados = []  
# lista_reprobados = []

# for i in range(10):
#     calificacion = float(input("introduce una calificacion entre 0 y 10: "))
#     while calificacion < 0 or calificacion > 10:
#         calificacion = float(input("Calificacion invalida. Introduce una calificacion entre 0 y 10: "))
#     if calificacion <= 6:
#         lista_reprobados.append(calificacion)
#     else:
#         lista_aprobados.append(calificacion)
# print(f"Cantidad de aprobados: {len(lista_aprobados)}")
# print(f"Cantidad de reprobados: {len(lista_reprobados)}")

# #Diccionarios
# diccionario = {
#     "nombre": "jorge",
#     "apellido" : "Vasquez",
#     "edad": 19,
#     "carrera": "programacion y webmaster",
#     "isestudiante":  True
# }

# print(diccionario.keys())  #muestra las claves del diccionario
# print(diccionario.values())  #muestra los valores del diccionario
# print(diccionario.items())  #muestra los pares clave-valor del diccionario
# print(diccionario["isestudiante"])  #muestra el valor de la clave "isestudiante"
# diccionario.pop("edad")  #elimina la clave "edad" y su valor
# print(diccionario)
# print(len(diccionario))  #muestra la cantidad de elementos en el diccionario
# diccionario["edad"] = 20  #agrega la clave "edad" con su valor 20
# print(diccionario)

# #Recorrido de diccionarios
# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}")

# # #Ejercicio 1: Crea un diccionario vacio. Pide nombres y calificaciones de 5 alumnos y guardalos en el diccionario. luego muestra su promedio
# diccionario_alumnos = {}
# for i in range(5):
#     nombre = input("introduce el nombre del alumno: ")
#     calificacion = float(input("introduce la calificacion del alumno: "))
#     while(calificacion < 0 or calificacion > 10):
#         calificacion = float(input(f"Calificacion invalida. Introduce la calificacion de {nombre} entre 0 y 10: "))
#     diccionario_alumnos[nombre] = calificacion

# print(diccionario_alumnos)

# for clave, valor in diccionario_alumnos.items():
#     print(f"{clave}: {valor}")

# suma_calificaciones = sum(diccionario_alumnos.values())
# promedio = suma_calificaciones / len(diccionario_alumnos)
# print(f"El promedio de las calificaciones es: {promedio}")

# #Ejercicio 2: Crea un diccionario con 5 productos y precios. pide un producto y muestra su precio.
# diccionario_productos = {
#     "cloro": 20,
#     "detergente": 35,
#     "jabón": 15,
#     "papel sanitario": 40,
#     "limpiador multiusos": 60
# }

# producto_buscado = input("introsduce el nombre del producto: ")
# if producto_buscado in diccionario_productos:
#     print(f"El precio de {producto_buscado} es: ${diccionario_productos[producto_buscado]}.")
# else:
#     print("El producto no se encuentra en el diccionario.")

#Ejercicio 3: Crea un diccionario con 5 paises y sus capitales. pide un pais y muestra su capital.
pais_buscado = input("introduce el nombre de un pais: ")
diccionario_paises = {
    "mexico": "ciudad de mexico",
    "brasil": "bracilia",
    "uruguay": "montevideo",
    "argentina": "buenos aires",
    "Estados unidos": "washington d.c."
}
while pais_buscado in diccionario_paises:
    if pais_buscado in diccionario_paises:
        print(f"la capital del pais {pais_buscado} es: {diccionario_paises[pais_buscado]}")
    else: