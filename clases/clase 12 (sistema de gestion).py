#sistema de gestion de estudiantes

#funcion para mostras las opciones del menu
def mostrar_menu():
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

#funcion para buscar un estudiante por nombre
def buscar_estudiante(lista_estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_buscar.lower():
            print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
            return
    print("Estudiante no encontrado.")

#funcion para eliminar un estudiante
def eliminar_estudiante(lista_estudiantes):
    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_eliminar.lower():
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} dado de baja exitosamente.")
            return
    print("Estudiante no encontrado.")

#funcion principal del sistema
def _main_():
    lista_estudiantes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == '3':
            buscar_estudiante(lista_estudiantes)
        elif opcion == '4':
            eliminar_estudiante(lista_estudiantes)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    _main_()