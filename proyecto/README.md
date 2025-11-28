# Gestor de Alumnos

Pequeño gestor de alumnos en Python que permite agregar, consultar, editar y eliminar registros.

Archivos:
- `gestor_alumnos.py`: script principal.
- `alumnos.json`: archivo creado automáticamente al guardar registros.

Requisitos:
- Python 3.x

Cómo ejecutar (desde la carpeta `proyecto`):

```powershell
python .\gestor_alumnos.py
```

El menú es interactivo y se repite hasta que se selecciona "Salir".

Validaciones importantes:
- `id` debe ser un entero y único.
- `matrícula` debe ser única.
- `promedio` acepta solo valores mayores a 0 y menores a 10.
 - `promedio` acepta solo valores mayores a 0 y menores o iguales a 10.

Los datos se guardan automáticamente en `alumnos.json` cada vez que se agrega, edita o elimina un registro.