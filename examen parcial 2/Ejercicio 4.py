#Haz un programa que pida una palabra, y cuenta cuantas vocales tiene la palabra ingresada
palabra = input("Ingresa una palabra: ")
vocales = "aeiou"
contador_vocales = 0
palabra_minusculas = palabra.lower()
for letra in palabra_minusculas:
    if letra in vocales:
        contador_vocales += 1
print("La cantidad de vocales que tiene la palabra es: ", contador_vocales)
