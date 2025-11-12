#metodos de utilidad
lista_frutas = ["manzana", "banana", "cereza","durazo", "naranja"]
print(lista_frutas)

lista_frutas.append("kiwi") #agrega un elemento al final de la lista
print(lista_frutas)

lista_frutas.pop() #elimina el ultimo elemento de la lista
print(lista_frutas)

lista_frutas.pop(2) #elimina el elemento en la posicion 2 (tercer elemento)
print(lista_frutas)

lista_frutas.remove("banana") #elimina el elemento con el valor "banana"
print(lista_frutas)

lista_frutas.insert(2, "uva") #inserta el elemento "uva" en la posicion 2
print(lista_frutas)

lista_frutas.clear() #elimina todos los elementos de la lista
print(lista_frutas)

lista_frutas = [] #reasignamos la lista para seguir trabajando

lista_frutas = ["manzana", "banana", "cereza","durazo", "naranja"]

lista_frutas.index("cereza") #devuelve el indice del elemento con el valor "cereza"
print(lista_frutas.index("cereza"))

lista_frutas.count("banana") #cuenta cuantas veces aparece el elemento con el valor "banana"
print(lista_frutas.count("banana"))

lista_frutas.sort() #ordena la lista en orden alfabetico
print(lista_frutas)

lista_frutas.reverse() #invierte el orden de los elementos en la lista
print(lista_frutas)

lista_frutas.len() #devuelve la cantidad de elementos en la lista
print(len(lista_frutas))

lista = [5, 2, 9, 1, 5, 6]#devuelve la suma de todos los elementos en la lista
print(sum(lista)) 

#Ejercicio 1: Pide 5 numeros, guardalos en una lista y muestra el promedio y el mayor de esos numeros
print("Ejercicio 1")
lista_numeros = []  #declaramos una lista vacia para guardar los numeros
for i in range(5):
    numero = float(input("Ingrese un numero: "))
    lista_numeros.append(numero)#agregamos el numero ingresado a la lista

promedio = sum(lista_numeros) / len(lista_numeros) #calculamos el promedio
mayor = max(lista_numeros) #obtenemos el mayor numero de la lista
print(f"El promedio de los numeros ingresados es: {promedio}")
print(f"El numero mayor ingresado es: {mayor}")
#Ejercicio 2: Pide numeros hasta que el usuario escriba 0: guardalos en una lista y muestra la lista ordenada ascendentemente
print("Ejercicio 2")
lista_numeros = []  #declaramos una lista vacia para guardar los numeros
while True:
    numero = float(input("Ingrese un numero (0 para terminar): "))
    if numero == 0:
        break #salimos del bucle si el numero es 0
    lista_numeros.append(numero) #agregamos el numero ingresado a la lista
lista_numeros.sort() #ordenamos la lista en orden ascendente
print("Lista ordenada ascendentemente:", lista_numeros)

