#Haz un programa que pida una frase y cuenta cuantas lestras tiene la frase sin contar espacios.
frase = input("Ingresa una frase: ")
frase_sin_espacios = frase.replace(" " , "")
cantidas_letras = len(frase_sin_espacios)
print("La cantidas de letras en la frase es: ", cantidas_letras)
