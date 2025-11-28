#!/usr/bin/env python3
"""
Gestor de Alumnos

Características:
- Guarda los registros en JSON en el archivo 'alumnos.json' dentro de la carpeta del script.
- Campos: id (int), matricula (string), nombre (string), carrera (string), promedio (float: 0 < promedio < 10)
- Menú: agregar, consultar, editar, eliminar, salir

Uso: ejecutar este archivo con Python 3.
"""

import json
import os
import sys


DATA_FILENAME = os.path.join(os.path.dirname(__file__), "alumnos.json")


def cargar_datos():
    """Carga la lista de alumnos desde el archivo JSON. Devuelve lista vacía si no existe."""
    if not os.path.exists(DATA_FILENAME):
        return []
    try:
        with open(DATA_FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        print("Advertencia: no se pudo leer el archivo de datos. Se iniciará con lista vacía.")
        return []


def guardar_datos(alumnos):
    """Guarda la lista de alumnos en el archivo JSON."""
    try:
        with open(DATA_FILENAME, "w", encoding="utf-8") as f:
            json.dump(alumnos, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar los datos: {e}")


def input_no_vacio(prompt):
    """Pide entrada al usuario y obliga que no sea vacía."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("El campo no puede estar vacío. Intente nuevamente.")


def input_int(prompt):
    while True:
        valor = input(prompt).strip()
        try:
            return int(valor)
        except ValueError:
            print("Por favor ingrese un número entero válido.")


def input_float_rango(prompt, min_val=0.0, max_val=10.0):
    """Pide un float dentro de (min_val, max_val) exclusivo del 0 y 10 si se requiere."""
    while True:
        valor = input(prompt).strip()
        try:
            f = float(valor)
            # Aceptar valores mayores que min_val y menores o iguales a max_val
            if f > min_val and f <= max_val:
                return f
            print(f"El valor debe ser mayor que {min_val} y menor o igual que {max_val}.")
        except ValueError:
            print("Por favor ingrese un número válido (p. ej. 7.5).")


def existe_id(alumnos, id_buscar):
    return any(a.get("id") == id_buscar for a in alumnos)


def existe_matricula(alumnos, matricula_buscar):
    return any(a.get("matricula").lower() == matricula_buscar.lower() for a in alumnos)


def agregar_registro(alumnos):
    print("\n--- Agregar nuevo alumno ---")
    # ID único
    while True:
        try:
            id_nuevo = int(input_no_vacio("ID (número entero): "))
        except ValueError:
            print("ID inválido. Debe ser un entero.")
            continue
        if existe_id(alumnos, id_nuevo):
            print("Ya existe un registro con ese ID. Ingrese otro.")
        else:
            break

    # Matrícula única
    while True:
        matricula = input_no_vacio("Matrícula: ")
        if existe_matricula(alumnos, matricula):
            print("Ya existe un alumno con esa matrícula. Verifique.")
        else:
            break

    nombre = input_no_vacio("Nombre completo: ")
    carrera = input_no_vacio("Carrera: ")
    promedio = input_float_rango("Promedio (0 < promedio < 10): ")

    nuevo = {
        "id": id_nuevo,
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera,
        "promedio": round(promedio, 2)
    }
    alumnos.append(nuevo)
    guardar_datos(alumnos)
    print("Registro agregado correctamente.\n")


def mostrar_registros(alumnos):
    print("\n--- Lista de Alumnos ---")
    if not alumnos:
        print("No hay registros guardados.")
        return
    # Mostrar en formato tabular simple
    header = f"{'ID':<5} {'MATRICULA':<15} {'NOMBRE':<30} {'CARRERA':<20} {'PROMEDIO':<8}"
    print(header)
    print("-" * len(header))
    for a in alumnos:
        print(f"{a.get('id', ''):<5} {a.get('matricula',''):<15} {a.get('nombre',''):<30} {a.get('carrera',''):<20} {a.get('promedio',''):<8}")
    print()


def buscar_registro(alumnos):
    print('\n--- Buscar registro por ID o nombre ---')
    clave = input_no_vacio("Ingrese ID (enteros) o parte del nombre: ")
    resultados = []
    # intento por ID
    try:
        id_b = int(clave)
        resultados = [a for a in alumnos if a.get('id') == id_b]
    except ValueError:
        q = clave.lower()
        resultados = [a for a in alumnos if q in a.get('nombre','').lower()]

    if not resultados:
        print("No se encontraron registros.")
        return
    print("Resultados:")
    for a in resultados:
        print(json.dumps(a, ensure_ascii=False, indent=2))


def editar_registro(alumnos):
    print('\n--- Editar registro ---')
    if not alumnos:
        print("No hay registros para editar.")
        return
    mostrar_registros(alumnos)
    try:
        id_editar = int(input_no_vacio("Ingrese el ID del registro a editar: "))
    except ValueError:
        print("ID inválido.")
        return
    for a in alumnos:
        if a.get('id') == id_editar:
            print("Ingrese nuevos valores (dejar vacío para mantener el valor actual).")
            nueva_matricula = input(f"Matrícula [{a.get('matricula')}]: ").strip()
            if nueva_matricula:
                if nueva_matricula.lower() != a.get('matricula').lower() and existe_matricula(alumnos, nueva_matricula):
                    print("La matrícula ya existe en otro registro. No se actualizó la matrícula.")
                else:
                    a['matricula'] = nueva_matricula

            nuevo_nombre = input(f"Nombre [{a.get('nombre')}]: ").strip()
            if nuevo_nombre:
                a['nombre'] = nuevo_nombre

            nueva_carrera = input(f"Carrera [{a.get('carrera')}]: ").strip()
            if nueva_carrera:
                a['carrera'] = nueva_carrera

            # Promedio: validar rango o dejar
            prom_str = input(f"Promedio [{a.get('promedio')}]: ").strip()
            if prom_str:
                try:
                    prom_f = float(prom_str)
                    # Aceptar prom_f > 0 y <= 10
                    if prom_f > 0 and prom_f <= 10:
                        a['promedio'] = round(prom_f, 2)
                    else:
                        print("Promedio fuera de rango (debe ser > 0 y <= 10). No se actualizó el promedio.")
                except ValueError:
                    print("Promedio inválido. No se actualizó el promedio.")

            guardar_datos(alumnos)
            print("Registro actualizado correctamente.")
            return
    print("No se encontró ningún registro con ese ID.")


def eliminar_registro(alumnos):
    print('\n--- Eliminar registro ---')
    if not alumnos:
        print("No hay registros para eliminar.")
        return
    mostrar_registros(alumnos)
    try:
        id_elim = int(input_no_vacio("Ingrese el ID del registro a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, a in enumerate(alumnos):
        if a.get('id') == id_elim:
            confirm = input(f"¿Está seguro de eliminar al alumno '{a.get('nombre')}'? (S/N): ").strip().lower()
            if confirm == 's' or confirm == 'si':
                alumnos.pop(i)
                guardar_datos(alumnos)
                print("Registro eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return
    print("No se encontró ningún registro con ese ID.")


def menu_principal():
    alumnos = cargar_datos()
    while True:
        print("\n================ Gestor de Alumnos ================")
        print("1. Agregar registro")
        print("2. Consultar registros")
        print("3. Buscar registro")
        print("4. Editar registro")
        print("5. Eliminar registro")
        print("6. Salir")
        try:
            opcion = int(input("Seleccione una opción (1-6): ").strip())
        except ValueError:
            print("Opción inválida. Ingrese un número entre 1 y 6.")
            continue

        if opcion == 1:
            agregar_registro(alumnos)
        elif opcion == 2:
            mostrar_registros(alumnos)
        elif opcion == 3:
            buscar_registro(alumnos)
        elif opcion == 4:
            editar_registro(alumnos)
        elif opcion == 5:
            eliminar_registro(alumnos)
        elif opcion == 6:
            print("Saliendo... Guardando datos y cerrando.")
            guardar_datos(alumnos)
            break
        else:
            print("Opción fuera de rango. Intente nuevamente.")


if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        print('\nInterrupción por teclado. Saliendo...')
        sys.exit(0)
