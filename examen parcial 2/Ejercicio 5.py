#Haz un programa que pide al usuario solicitar 5 calificaciones, solo acepta numeros del 1 al 10 (si se permite decimales). Almacena estas 5 calificaciones en un arreglo, y posteriormente calcula el promedio de las calificaciones, muestra solamente 2 decimales si el alumno tiene una calificacion promedio mayor que 6, imprime un mensaje de "aprobado", si tiene una calificacion menor que 6 imprime "reprobado", y si tiene una calificacion de 10 imprime "Exelente"
calificaciones = []
while len(calificaciones) < 5:
    califcacion = float(input("Ingresa una calificación (1-10): "))
    if 1 <= califcacion <= 10:
        calificaciones.append(califcacion)
    else:
        print("Calificación inválida. Por favor ingresa un número entre 1 y 10.")
promedio = sum(calificaciones) / len(calificaciones)
if promedio == 10:
    print(f"Exelente {promedio}")
elif promedio >= 6:
    print(f"Aprobado, El promedio es: {promedio:.2f}")
else:
    print(f"Reprobado, el promedio es: {promedio:.2f}")

