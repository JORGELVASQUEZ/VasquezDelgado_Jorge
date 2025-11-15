#sistema de gestion de estudiantes

#funcion para mostras las opciones del menu
print("Sistema de gestion de estudiantes")
print("1. Agregar estudiante")
print("2. Mostrar lista completa de estudiantes")
print("3. Buscar estudiante por nombre")
print("4. Eliminar estudiante")
print("5. Salir")

#funcion para agregar un estudiante
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})
    print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

    #funcion para mostrar la lista completa de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista.")
        return
    print("Lista completa de estudiantes:")
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")

    mostrar_estudiantes(lista_estudiantes)