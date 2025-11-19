#Pide una palabra y remplaza todas las vocales por el simbolo *
palabra = input("Ingresa una palabra:")
palabra_minusculas = palabra.lower()
palabra_modificada = palabra_minusculas.replace("a" , "*").replace("e" , "*").replace("i" , "*").replace("o" , "*").replace("u" , "*")
print("La palabra sin vocales es: ", palabra_modificada)
