#!/usr/bin/env python3
"""
Interfaz gráfica para el Gestor de Alumnos usando Tkinter.

Este script reutiliza las funciones de persistencia y validación definidas
en `gestor_alumnos.py`.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter.ttk as ttk
import sys
import os

# Asegurarse de que el módulo gestor_alumnos pueda importarse cuando se ejecuta
# desde la carpeta proyecto
SCRIPT_DIR = os.path.dirname(__file__)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from gestor_alumnos import (
    cargar_datos,
    guardar_datos,
    existe_id,
    existe_matricula,
)


class GestorAlumnosGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Alumnos - GUI")
        self.geometry("800x400")
        self.resizable(True, True)

        # Datos
        self.alumnos = []

        # UI
        self.create_widgets()
        self.cargar()

    def create_widgets(self):
        # Frame superior: botones
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.X, padx=8, pady=6)

        btn_agregar = tk.Button(top_frame, text="Agregar", command=self.abrir_agregar)
        btn_agregar.pack(side=tk.LEFT, padx=4)

        btn_editar = tk.Button(top_frame, text="Editar", command=self.abrir_editar)
        btn_editar.pack(side=tk.LEFT, padx=4)

        btn_eliminar = tk.Button(top_frame, text="Eliminar", command=self.eliminar)
        btn_eliminar.pack(side=tk.LEFT, padx=4)

        btn_buscar = tk.Button(top_frame, text="Buscar", command=self.buscar)
        btn_buscar.pack(side=tk.LEFT, padx=4)

        btn_refrescar = tk.Button(top_frame, text="Refrescar", command=self.cargar)
        btn_refrescar.pack(side=tk.LEFT, padx=4)

        # Frame central: Treeview con registros
        cols = ("id", "matricula", "nombre", "carrera", "promedio")
        self.tree = ttk.Treeview(self, columns=cols, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("carrera", text="Carrera")
        self.tree.heading("promedio", text="Promedio")

        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("matricula", width=120)
        self.tree.column("nombre", width=260)
        self.tree.column("carrera", width=160)
        self.tree.column("promedio", width=80, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        # Doble click para editar
        self.tree.bind('<Double-1>', lambda e: self.abrir_editar())

    def cargar(self):
        self.alumnos = cargar_datos()
        self.refrescar_lista()

    def refrescar_lista(self):
        # limpiar
        for r in self.tree.get_children():
            self.tree.delete(r)
        # insertar
        for a in self.alumnos:
            self.tree.insert('', tk.END, values=(
                a.get('id'),
                a.get('matricula'),
                a.get('nombre'),
                a.get('carrera'),
                a.get('promedio')
            ))

    def abrir_agregar(self):
        FormAlumno(self, modo='agregar')

    def abrir_editar(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Editar", "Seleccione un registro para editar.")
            return
        item = self.tree.item(sel[0])
        id_sel = item['values'][0]
        FormAlumno(self, modo='editar', id_registro=id_sel)

    def buscar(self):
        q = simpledialog.askstring("Buscar", "Ingrese ID o parte del nombre:")
        if q is None or q.strip() == '':
            return
        q = q.strip()
        resultados = []
        try:
            id_b = int(q)
            resultados = [a for a in self.alumnos if a.get('id') == id_b]
        except ValueError:
            ql = q.lower()
            resultados = [a for a in self.alumnos if ql in a.get('nombre','').lower()]

        if not resultados:
            messagebox.showinfo("Buscar", "No se encontraron registros.")
            return
        # mostrar primera coincidencia seleccionada
        first = resultados[0]
        # encontrar en tree y seleccionar
        for iid in self.tree.get_children():
            vals = self.tree.item(iid)['values']
            if vals and vals[0] == first.get('id'):
                self.tree.selection_set(iid)
                self.tree.see(iid)
                break

    def eliminar(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Eliminar", "Seleccione un registro para eliminar.")
            return
        item = self.tree.item(sel[0])
        id_sel = item['values'][0]
        alumno = next((a for a in self.alumnos if a.get('id') == id_sel), None)
        if not alumno:
            messagebox.showerror("Eliminar", "Registro no encontrado.")
            return
        if messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar a '{alumno.get('nombre')}'?"):
            self.alumnos = [a for a in self.alumnos if a.get('id') != id_sel]
            guardar_datos(self.alumnos)
            self.refrescar_lista()
            messagebox.showinfo("Eliminar", "Registro eliminado correctamente.")


class FormAlumno(tk.Toplevel):
    def __init__(self, master: GestorAlumnosGUI, modo='agregar', id_registro=None):
        super().__init__(master)
        self.master = master
        self.modo = modo
        self.id_registro = id_registro
        self.title("Agregar alumno" if modo=='agregar' else "Editar alumno")
        self.resizable(False, False)
        self.create_widgets()

        if modo == 'editar' and id_registro is not None:
            self.cargar_datos_existentes()

    def create_widgets(self):
        pad = 6
        lbl_id = tk.Label(self, text="ID:")
        lbl_id.grid(row=0, column=0, sticky=tk.W, padx=pad, pady=pad)
        self.ent_id = tk.Entry(self)
        self.ent_id.grid(row=0, column=1, padx=pad, pady=pad)

        lbl_mat = tk.Label(self, text="Matrícula:")
        lbl_mat.grid(row=1, column=0, sticky=tk.W, padx=pad, pady=pad)
        self.ent_mat = tk.Entry(self)
        self.ent_mat.grid(row=1, column=1, padx=pad, pady=pad)

        lbl_nom = tk.Label(self, text="Nombre:")
        lbl_nom.grid(row=2, column=0, sticky=tk.W, padx=pad, pady=pad)
        self.ent_nom = tk.Entry(self, width=40)
        self.ent_nom.grid(row=2, column=1, padx=pad, pady=pad)

        lbl_car = tk.Label(self, text="Carrera:")
        lbl_car.grid(row=3, column=0, sticky=tk.W, padx=pad, pady=pad)
        self.ent_car = tk.Entry(self)
        self.ent_car.grid(row=3, column=1, padx=pad, pady=pad)

        lbl_prom = tk.Label(self, text="Promedio:")
        lbl_prom.grid(row=4, column=0, sticky=tk.W, padx=pad, pady=pad)
        self.ent_prom = tk.Entry(self)
        self.ent_prom.grid(row=4, column=1, padx=pad, pady=pad)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=(0,8))

        btn_save = tk.Button(btn_frame, text="Guardar", command=self.guardar)
        btn_save.pack(side=tk.LEFT, padx=6)

        btn_cancel = tk.Button(btn_frame, text="Cancelar", command=self.destroy)
        btn_cancel.pack(side=tk.LEFT, padx=6)

    def cargar_datos_existentes(self):
        alumno = next((a for a in self.master.alumnos if a.get('id') == self.id_registro), None)
        if not alumno:
            messagebox.showerror("Editar", "Registro no encontrado.")
            self.destroy()
            return
        self.ent_id.insert(0, str(alumno.get('id')))
        # ID no editable en edición
        self.ent_id.config(state='disabled')
        self.ent_mat.insert(0, alumno.get('matricula'))
        self.ent_nom.insert(0, alumno.get('nombre'))
        self.ent_car.insert(0, alumno.get('carrera'))
        self.ent_prom.insert(0, str(alumno.get('promedio')))

    def guardar(self):
        # Validaciones: no vacíos, id int, promedio float rango, unicidad
        try:
            if self.modo == 'agregar':
                id_val = int(self.ent_id.get().strip())
            else:
                id_val = int(self.ent_id.get().strip()) if self.ent_id.get().strip() else None
        except ValueError:
            messagebox.showerror("Validación", "ID inválido. Debe ser un número entero.")
            return

        matricula = self.ent_mat.get().strip()
        nombre = self.ent_nom.get().strip()
        carrera = self.ent_car.get().strip()
        prom_str = self.ent_prom.get().strip()

        if not matricula or not nombre or not carrera or (self.modo=='agregar' and id_val is None) or not prom_str:
            messagebox.showerror("Validación", "Todos los campos son obligatorios.")
            return

        try:
            prom_val = float(prom_str)
            # Aceptar valores mayores que 0 y menores o iguales a 10
            if not (prom_val > 0 and prom_val <= 10):
                messagebox.showerror("Validación", "Promedio fuera de rango. Debe ser > 0 y <= 10.")
                return
        except ValueError:
            messagebox.showerror("Validación", "Promedio inválido.")
            return

        # Verificar unicidad
        alumnos = self.master.alumnos
        if self.modo == 'agregar':
            if existe_id(alumnos, id_val):
                messagebox.showerror("Validación", "Ya existe un registro con ese ID.")
                return
            if existe_matricula(alumnos, matricula):
                messagebox.showerror("Validación", "Ya existe un registro con esa matrícula.")
                return
            nuevo = {
                'id': id_val,
                'matricula': matricula,
                'nombre': nombre,
                'carrera': carrera,
                'promedio': round(prom_val, 2)
            }
            alumnos.append(nuevo)
            guardar_datos(alumnos)
            self.master.refrescar_lista()
            messagebox.showinfo("Agregar", "Registro agregado correctamente.")
            self.destroy()
        else:
            # editar -- id no cambia
            id_actual = id_val
            alumno = next((a for a in alumnos if a.get('id') == id_actual), None)
            if not alumno:
                messagebox.showerror("Editar", "Registro no encontrado.")
                return
            # comprobar matrícula única (excepto el mismo registro)
            if matricula.lower() != alumno.get('matricula','').lower() and existe_matricula(alumnos, matricula):
                messagebox.showerror("Validación", "La matrícula ya existe en otro registro.")
                return
            alumno['matricula'] = matricula
            alumno['nombre'] = nombre
            alumno['carrera'] = carrera
            alumno['promedio'] = round(prom_val, 2)
            guardar_datos(alumnos)
            self.master.refrescar_lista()
            messagebox.showinfo("Editar", "Registro actualizado correctamente.")
            self.destroy()


def main():
    app = GestorAlumnosGUI()
    app.mainloop()


if __name__ == '__main__':
    main()
