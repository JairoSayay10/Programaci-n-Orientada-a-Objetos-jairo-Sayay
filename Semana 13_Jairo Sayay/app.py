# ============================================================
# Aplicación GUI - Lista de Tareas
# Librería: Tkinter 
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox


def agregar_item():
    """
    Lee el texto del campo de entrada y lo agrega a la tabla.
    Valida que el campo no esté vacío antes de agregar cualquier tarea.
    """
    nombre = entry_nombre.get().strip()
    descripcion = entry_descripcion.get().strip()

    # Validación: ambos campos deben tener contenido
    if not nombre or not descripcion:
        messagebox.showwarning("Campo vacío", "Por favor completa todos los campos vacios.")
        return

    # Insertar nueva fila en la tabla con los datos ingresados
    tabla.insert("", "end", values=(nombre, descripcion))

    # Limpiar los campos de texto después de agregar
    entry_nombre.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)
    entry_nombre.focus()  # Mover el foco al primer campo


def limpiar_seleccion():
    """
    Elimina únicamente el elemento que se selecciona en la tabla.
    Muestra advertencia si no hay ningún elemento seleccionado.
    """
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Sin selección", "Selecciona un elemento de la lista.")
        return
    # Eliminar cada elemento seleccionado
    for item in seleccion:
        tabla.delete(item)


def limpiar_todo():
    """
    Elimina todos los elementos de la tabla después de confirmar con el usuario.
    """
    if not tabla.get_children():
        messagebox.showinfo("Lista vacía", "No hay elementos para limpiar.")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar todos los elementos?")
    if confirmar:
        for item in tabla.get_children():
            tabla.delete(item)


# ============================================================
# VENTANA PRINCIPAL
# ============================================================
ventana = tk.Tk()
ventana.title("Gestión de Tareas - App GUI- Desarrollado por Jairo Sayay")
ventana.geometry("600x480")
ventana.resizable(False, False)
ventana.configure(bg="#95b6ac")

# ============================================================
# TÍTULO DE LA APLICACIÓN
# ============================================================
lbl_titulo = tk.Label(
    ventana,
    text="📋 Lista de Tareas",
    font=("Georgia", 18, "bold"),
    bg="#f0f4f8",
    fg="#2d3748"
)
lbl_titulo.pack(pady=(16, 4))

lbl_subtitulo = tk.Label(
    ventana,
    text="Agrega y administra tus tareas fácilmente",
    font=("Georgia", 10),
    bg="#f0f4f8",
    fg="#718096"
)
lbl_subtitulo.pack(pady=(0, 12))

# ============================================================
# FRAME DE ENTRADA DE DATOS
# ============================================================
frame_entrada = tk.LabelFrame(
    ventana,
    text=" Nueva Tarea ",
    font=("Arial", 10, "bold"),
    bg="#f0f4f8",
    fg="#4a5568",
    padx=12,
    pady=10
)
frame_entrada.pack(fill="x", padx=20, pady=4)

# Etiqueta y campo: Nombre de la tarea
lbl_nombre = tk.Label(frame_entrada, text="Nombre:", font=("Arial", 10), bg="#f0f4f8", fg="#2d3748")
lbl_nombre.grid(row=0, column=0, sticky="w", pady=4)

entry_nombre = tk.Entry(frame_entrada, width=30, font=("Arial", 10))
entry_nombre.grid(row=0, column=1, padx=8, pady=4, sticky="ew")

# Etiqueta y campo: Descripción
lbl_descripcion = tk.Label(frame_entrada, text="Descripción:", font=("Arial", 10), bg="#f0f4f8", fg="#2d3748")
lbl_descripcion.grid(row=1, column=0, sticky="w", pady=4)

entry_descripcion = tk.Entry(frame_entrada, width=30, font=("Arial", 10))
entry_descripcion.grid(row=1, column=1, padx=8, pady=4, sticky="ew")

frame_entrada.columnconfigure(1, weight=1)

# ============================================================
# FRAME DE BOTONES
# ============================================================
frame_botones = tk.Frame(ventana, bg="#f0f4f8")
frame_botones.pack(pady=10)

# Botón Agregar
btn_agregar = tk.Button(
    frame_botones,
    text="➕  Agregar",
    command=agregar_item,
    font=("Arial", 10, "bold"),
    bg="#3182ce",
    fg="white",
    activebackground="#2b6cb0",
    activeforeground="white",
    relief="flat",
    padx=16,
    pady=6,
    cursor="hand2"
)
btn_agregar.grid(row=0, column=0, padx=6)

# Botón Limpiar selección
btn_limpiar_sel = tk.Button(
    frame_botones,
    text="🗑  Limpiar selección",
    command=limpiar_seleccion,
    font=("Arial", 10),
    bg="#e53e3e",
    fg="white",
    activebackground="#c53030",
    activeforeground="white",
    relief="flat",
    padx=16,
    pady=6,
    cursor="hand2"
)
btn_limpiar_sel.grid(row=0, column=1, padx=6)

# Botón Limpiar todo
btn_limpiar_todo = tk.Button(
    frame_botones,
    text="🧹  Limpiar todo",
    command=limpiar_todo,
    font=("Arial", 10),
    bg="#718096",
    fg="white",
    activebackground="#4a5568",
    activeforeground="white",
    relief="flat",
    padx=16,
    pady=6,
    cursor="hand2"
)
btn_limpiar_todo.grid(row=0, column=2, padx=6)

# ============================================================
# TABLA DE DATOS (Treeview)
# ============================================================
frame_tabla = tk.LabelFrame(
    ventana,
    text=" Tareas Registradas ",
    font=("Arial", 10, "bold"),
    bg="#f0f4f8",
    fg="#4a5568",
    padx=12,
    pady=8
)
frame_tabla.pack(fill="both", expand=True, padx=20, pady=(4, 16))

# Configurar columnas de la tabla
columnas = ("Nombre", "Descripción")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
tabla.heading("Nombre", text="Nombre de la Tarea")
tabla.heading("Descripción", text="Descripción")
tabla.column("Nombre", width=180, anchor="w")
tabla.column("Descripción", width=340, anchor="w")

# Barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Estilo de la tabla
estilo = ttk.Style()
estilo.configure("Treeview", font=("Arial", 10), rowheight=26)
estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))

# ============================================================
# INICIAR LA APLICACIÓN
# ============================================================
entry_nombre.focus()       # Foco inicial en el primer campo
ventana.mainloop()         # Bucle principal de eventos
