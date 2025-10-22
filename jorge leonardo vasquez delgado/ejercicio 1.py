#ejercicio 1 haz un programa que solicite al usuario ingresar 5 calificaciones y calcula el promedio

#solicita a usuario que ingrese 5 calificaciones

calificacion1 = float(input("ingresa la calificacion 1: "))
calificacion2 = float(input("ingresa la calificacion 2: "))
calificacion3 = float(input("ingresa la calificacion 3: "))
calificacion4 = float(input("ingresa la calificacion 4: "))
calificacion5 = float(input("ingresa la calificacion 5: "))

#calcula el promedio
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

#mostrar el promedio 
print ("el promedio es: ", promedio)
