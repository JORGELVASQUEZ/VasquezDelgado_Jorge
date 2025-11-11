palabra = "plabra ejemplo"

for letra in palabra:
    print(letra)

#Ejercicio 1: Haz un programa que pida nombre y apellido. muestra en pantalla en formato apellido, nombre con cada palabra iniciando con mayuscula
print("Ejercicio 1")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = apellido + ", " + nombre
print(f"{apellido.capitalize()}, {nombre.capitalize()}") #Aqui usamos cadenas formateadas para mostrar el resultado, tod  el trato en mayuscula se hace esta linea
print(nombre_completo.title())#aqui usamos title oara convertir la primera letra de cada palabra en mayuscula, trbajamos con la variable creada anteriormente

#Ejercico 2: pidee una frase y una letra. muestra cuantas veces aparece esa letra en la frase sin distinguir entre mayusculas y minusculas
print("Ejercicio 2")
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra que desee buscar: ")
frase_formateada = frase.strip().lower() #elimina espacios en blanco al inicio y al final y convierte la frase a minusculas
letra_formateada = letra.strip().lower() #elimina espacios en blanco al inicio y al final y convierte la letra a minusculas
conteo_letra = frase_formateada.count(letra_formateada) #cuenta cuantas veces aparece la letra en la frase
print(f"La letra '{letra}' aparece {conteo_letra} veces en la frase: '{frase}'.")

#Ejercicio 3: Pide una frase y reemplaza todas las vocales 'a' por '@' y muestra el resultado
print("Ejercicio 3")
frase = input("Escribe una frase: ")
frase_formateada = frase.strip().lower() #elimina espacios en blanco al inicio y al final y convierte la frase a minusculas
frase_modificada = frase_formateada.replace("a", "@") #remplaza todas las 'a' por '@'
print("Frase modificada:", frase_modificada)

#Ejercicio 4: Pide un texto y eextrae los primeros 10 caracteres. Si el texto tiene menos de 10 caracteres, muestra el texto completo
print("Ejercicio 4")
texto = input("Ingrese un texto: ")
if len(texto) <= 10:
    print("Texto completo:", texto)
else:
    primeros_10 = texto[:10] #extrae los primeros 10 caracteres
    print("Primeros 10 caracteres:", primeros_10)

#############################################################
#                     LISTAS EN PYTHON                      #
#############################################################

#las listas son coleecciones ordenadas, mutables y  inexadas
lista1 = [10, 30, 20, 50, 5, 15]
lista2 = ["manzana", "banana", "fresa", "pera", "naranja", 4, 6.6, True]  #Lista con diferentes tipos de datos
print(lista1)
print(lista2)

#Recorrido de listas

for elemento in lista1:
    print(elemento)

for elemento in lista2:
    print(elemento)

#Llenado de listas vacias
lista3 = [] #lista vacia
#Llenar la lista con datos ingresados por el usuario
for i in range(11):
    numero = int(input("Ingrese un numero entero: "))
    lista3.append(numero) #El append agrega el numero ingresado al final de la lista
print("Lista llena:", lista3)
print(len(lista3)) #muestra la cantidad de elementos en la lista
print(sum(lista3)) #muestra la suma de todos los elementos en la lista