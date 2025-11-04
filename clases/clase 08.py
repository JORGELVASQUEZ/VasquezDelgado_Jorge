#cadenas
cadena = "texto o oraciones"
cadena2 = 'texto o oraciones'
cadena3 = "                   texto o oraciones                   "
cadena4 ="cadena 4"
cadena5 = "cadena 5"
#las cadenas son inmutables (pregunta de examen)

print(len(cadena))  #len() sirve para saber la longitud de la cadena
print(cadena.upper()) #convierte la cadena a mayusculas
print(cadena.lower()) #convierte la cadena a minusculas
print(cadena.capitalize()) #convierte la primera letra en mayuscula
print(cadena.title()) #convierte la primera letra de cada palabra en mayuscula
print(cadena3.strip()) #elimina espacios en blanco al inicio y al final

cadenanueva = cadena4 + cadena5
print(cadenanueva) #concatena dos cadenas, + " " + para agregar un espacio en blanco para separar las cadenas (print(cadena4 + " " + cadena5))

cadenamultiplicada = cadena4 * 5
print(cadenamultiplicada) #multiplica la cadena las veces que se indique

print(cadena.replace("t", "q")) #remplasa los caracteres puestos antes de la coma por los que estan puestos despues de la coma

cadena6 = "Hola, ¿cómo estás?, ¿estás bien?"
indice = cadena6.find("a") #imprime el indice de la primera aparicion del caracter o palabra que se busca
print(indice)# imprime la posicion del primer caracter "a"

indiceultimo = cadena6.rfind("n") #imprime el indice de la ultima aparicion del caracter o palabra que se busca
print(indiceultimo) #imprime la posicion del ultimo caracter "n"

cadena7 = "anita lava la tina"
conteo = cadena7.count("a") #cuenta cuantas veces aparece el caracter o palabra que se busca
print(conteo) #imprime el numero de veces que aparece el caracter "a"

print(cadena7.startswith("anita")) #devuelve True si la cadena empieza con el caracter o palabra que se busca, de lo contrario devuelve False
print(cadena7.endswith("tina")) #devuelve True si la cadena termina con el caracter o palabra que se busca, de lo contrario devuelve False
print(cadena7.split(" ")) #divide la cadena en una lista de subcadenas usando el caracter o palabra que se indica como separador
print(cadena7.isalpha()) #devuelve True si todos los caracteres de la cadena son letras del alfabeto, de lo contrario devuelve False
print(cadena7.isdigit()) #devuelve True si todos los caracteres de la cadena son dígitos, de lo contrario devuelve False
print(cadena7.isspace()) #devuelve True si todos los caracteres de la cadena son espacios en blanco, de lo contrario devuelve False
print(cadena7.index("lava")) #devuelve el índice de la primera aparición del caracter o palabra que se busca, si no se encuentra lanza un error
print(cadena7.count("la")) #cuenta cuantas veces aparece el caracter o palabra que se busca

#sintaxis de slicing cadena(inicio:fin:paso
cadena8 = "hola a todos"
print(cadena8[0:4]) #imprime desde el indice 0 hasta el 3 (el 4 no se incluye) sirve para partir una cadena
print(cadena8[:4]) #imprime desde el inicio hasta el indice 3
print(cadena8[4:9]) #imprime desde el indice 4 hasta el 9
print(cadena8[5:]) #imprime desde el indice 5 hasta el final
print(cadena8[-2:]) #imprime los dos ultimos caracteres de la cadena
print(cadena8[::2]) #imprime la cadena de 2 en 2 (cada dos caracteres)
print(cadena8[::-1]) #imprime la cadena al reves

#ejercicios

#1: pide una frase y mestra la misma frase sin espacios al inicio y al final con todas las letras en minusculas.
print("Ejercicio 1")
frase = input("Ingrese una frase: ")
fraselimpia = frase.strip().lower()
print(fraselimpia)

#2: pide una palabra y comprueba si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
print("Ejercicio 2")
palabra = input("Ingrese una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
