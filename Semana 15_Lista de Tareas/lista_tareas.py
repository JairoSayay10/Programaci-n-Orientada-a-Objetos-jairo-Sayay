# =============================================================
# APLICACIÓN: Lista de Tareas con Tkinter
# AUTOR: Jairo Estiven Sayay Alvarez
# DESCRIPCIÓN: Aplicación GUI para gestionar tareas del día a día.
#              Permite añadir, completar y eliminar tareas.
# =============================================================

import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------------
# CLASE PRINCIPAL DE LA APLICACIÓN
# Agrupamos toda la lógica y la interfaz dentro de una clase
# para mantener el código organizado (programación orientada a objetos).
# ---------------------------------------------------------------
class ListaDeTareas:

    def __init__(self, ventana_raiz):
        """
        Constructor: se ejecuta al crear la aplicación.
        Recibe la ventana principal de Tkinter y configura todo.
        """
        self.ventana = ventana_raiz
        self.ventana.title("📝 Mi Lista de Tareas")
        self.ventana.geometry("500x550")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#f0f4f8")

        # Guardamos las tareas en una lista de Python.
        # Cada tarea es un diccionario con 'texto' y 'completada'.
        self.tareas = []

        # Llamamos al método que construye la interfaz visual
        self._construir_interfaz()

    # -----------------------------------------------------------
    # CONSTRUCCIÓN DE LA INTERFAZ GRÁFICA
    # -----------------------------------------------------------
    def _construir_interfaz(self):
        """
        Crea y organiza todos los widgets (elementos visuales)
        de la ventana: etiquetas, campo de texto, botones y lista.
        """

        # --- TÍTULO ---
        etiqueta_titulo = tk.Label(
            self.ventana,
            text="📝 Lista de Tareas",
            font=("Helvetica", 20, "bold"),
            bg="#f0f4f8",
            fg="#2d3748"
        )
        etiqueta_titulo.pack(pady=(20, 10))

        # --- SECCIÓN DE ENTRADA ---
        # Frame (contenedor) que agrupa el campo de texto y el botón "Añadir"
        frame_entrada = tk.Frame(self.ventana, bg="#f0f4f8")
        frame_entrada.pack(padx=20, pady=5, fill="x")

        # Campo de texto donde el usuario escribe la nueva tarea
        self.campo_tarea = tk.Entry(
            frame_entrada,
            font=("Helvetica", 13),
            relief="flat",
            bg="#ffffff",
            fg="#2d3748",
            insertbackground="#4a90d9",  # Color del cursor de escritura
        )
        self.campo_tarea.pack(side="left", expand=True, fill="x",
                              ipady=8, padx=(0, 8))

        # Evento: presionar Enter en el campo de texto también añade la tarea.
        # '<Return>' es el nombre del evento de la tecla Enter en Tkinter.
        self.campo_tarea.bind("<Return>", self._evento_anadir_con_enter)

        # Botón para añadir tarea
        boton_anadir = tk.Button(
            frame_entrada,
            text="Añadir",
            font=("Helvetica", 12, "bold"),
            bg="#4a90d9",
            fg="white",
            relief="flat",
            padx=16,
            pady=8,
            cursor="hand2",  # Cambia el cursor al pasar por encima
            command=self.anadir_tarea  # Evento: clic en el botón
        )
        boton_anadir.pack(side="right")

        # --- LISTA DE TAREAS ---
        # Frame contenedor para la lista y su barra de desplazamiento
        frame_lista = tk.Frame(self.ventana, bg="#f0f4f8")
        frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

        # Barra de desplazamiento vertical (scrollbar)
        scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Listbox: el componente que muestra la lista de tareas
        self.lista_widget = tk.Listbox(
            frame_lista,
            font=("Helvetica", 13),
            bg="#ffffff",
            fg="#2d3748",
            selectbackground="#4a90d9",
            selectforeground="white",
            relief="flat",
            activestyle="none",       # Quita el subrayado al pasar el cursor
            yscrollcommand=scrollbar.set  # Conecta la barra de desplazamiento
        )
        self.lista_widget.pack(side="left", fill="both", expand=True)

        # Vinculamos la scrollbar con la lista
        scrollbar.config(command=self.lista_widget.yview)

        # Evento: doble clic sobre un elemento de la lista para completarlo
        self.lista_widget.bind("<Double-Button-1>", self._evento_doble_clic)

        # --- BOTONES DE ACCIÓN ---
        frame_botones = tk.Frame(self.ventana, bg="#f0f4f8")
        frame_botones.pack(padx=20, pady=10, fill="x")

        # Botón "Marcar como Completada"
        boton_completar = tk.Button(
            frame_botones,
            text="✔ Marcar Completada",
            font=("Helvetica", 11),
            bg="#48bb78",  # Verde
            fg="white",
            relief="flat",
            padx=12,
            pady=8,
            cursor="hand2",
            command=self.marcar_completada  # Evento: clic
        )
        boton_completar.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Botón "Eliminar Tarea"
        boton_eliminar = tk.Button(
            frame_botones,
            text="🗑 Eliminar Tarea",
            font=("Helvetica", 11),
            bg="#fc8181",  # Rojo suave
            fg="white",
            relief="flat",
            padx=12,
            pady=8,
            cursor="hand2",
            command=self.eliminar_tarea  # Evento: clic
        )
        boton_eliminar.pack(side="right", expand=True, fill="x", padx=(5, 0))

        # --- CONTADOR DE TAREAS ---
        self.etiqueta_contador = tk.Label(
            self.ventana,
            text="Total: 0 tarea(s) | Pendientes: 0",
            font=("Helvetica", 10),
            bg="#f0f4f8",
            fg="#718096"
        )
        self.etiqueta_contador.pack(pady=(0, 15))

        # Ponemos el foco en el campo de entrada al iniciar
        self.campo_tarea.focus()

    # -----------------------------------------------------------
    # LÓGICA DE LA APLICACIÓN
    # -----------------------------------------------------------

    def anadir_tarea(self):
        """
        Lee el texto del campo de entrada y añade la tarea a la lista.
        Si el campo está vacío, muestra una advertencia.
        """
        # Obtenemos el texto y quitamos espacios al inicio/final
        texto = self.campo_tarea.get().strip()

        if texto == "":
            # Si no hay texto, avisamos al usuario
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea antes de añadir.")
            return

        # Guardamos la tarea en nuestra lista interna como diccionario
        nueva_tarea = {"texto": texto, "completada": False}
        self.tareas.append(nueva_tarea)

        # Añadimos la tarea al widget visual (Listbox)
        self.lista_widget.insert(tk.END, f"  ○  {texto}")

        # Limpiamos el campo de entrada para la siguiente tarea
        self.campo_tarea.delete(0, tk.END)

        # Actualizamos el contador
        self._actualizar_contador()

    def marcar_completada(self):
        """
        Cambia el estado de la tarea seleccionada a 'completada'.
        Modifica su apariencia visual con color gris y tachado (✔).
        """
        # Obtenemos el índice del elemento seleccionado en la lista
        seleccion = self.lista_widget.curselection()

        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla como completada.")
            return

        indice = seleccion[0]  # El índice del primer elemento seleccionado

        # Verificamos si ya estaba completada para no repetir la acción
        if self.tareas[indice]["completada"]:
            messagebox.showinfo("Ya completada", "Esta tarea ya fue marcada como completada.")
            return

        # Actualizamos el estado en nuestra lista interna
        self.tareas[indice]["completada"] = True

        # Actualizamos el texto visual: añadimos ✔ y tachamos con guiones
        texto_original = self.tareas[indice]["texto"]
        texto_tachado = "  ✔  " + texto_original  # Prefijo de completado

        # Reemplazamos el elemento en el Listbox
        self.lista_widget.delete(indice)
        self.lista_widget.insert(indice, texto_tachado)

        # Cambiamos el color del texto a gris para indicar que está hecho
        self.lista_widget.itemconfig(indice, fg="#a0aec0")

        # Actualizamos el contador
        self._actualizar_contador()

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista visual y de la lista interna.
        Pide confirmación antes de eliminar.
        """
        seleccion = self.lista_widget.curselection()

        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")
            return

        indice = seleccion[0]
        texto_tarea = self.tareas[indice]["texto"]

        # Pedimos confirmación al usuario antes de eliminar
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que quieres eliminar la tarea:\n\n'{texto_tarea}'?"
        )

        if confirmar:
            # Eliminamos de la lista interna y del widget visual
            self.tareas.pop(indice)
            self.lista_widget.delete(indice)
            self._actualizar_contador()

    # -----------------------------------------------------------
    # MANEJADORES DE EVENTOS ADICIONALES
    # -----------------------------------------------------------

    def _evento_anadir_con_enter(self, evento):
        """
        Manejador del evento 'presionar Enter' en el campo de texto.
        El parámetro 'evento' es enviado automáticamente por Tkinter
        pero no lo necesitamos usar aquí, solo llamamos a anadir_tarea().
        """
        self.anadir_tarea()

    def _evento_doble_clic(self, evento):
        """
        Manejador del evento 'doble clic' en la lista.
        Marca la tarea seleccionada como completada sin usar el botón.
        El parámetro 'evento' contiene info del clic (posición, widget, etc.)
        """
        self.marcar_completada()

    # -----------------------------------------------------------
    # MÉTODO AUXILIAR
    # -----------------------------------------------------------

    def _actualizar_contador(self):
        """
        Recalcula y actualiza la etiqueta que muestra el número
        de tareas totales y cuántas están pendientes.
        """
        total = len(self.tareas)
        pendientes = sum(1 for t in self.tareas if not t["completada"])
        self.etiqueta_contador.config(
            text=f"Total: {total} tarea(s)  |  Pendientes: {pendientes}"
        )


# =============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# Esta sección se ejecuta solo cuando corremos este archivo
# directamente (no cuando se importa como módulo).
# =============================================================
if __name__ == "__main__":
    # Creamos la ventana principal de Tkinter
    ventana_principal = tk.Tk()

    # Creamos una instancia de nuestra aplicación, pasándole la ventana
    app = ListaDeTareas(ventana_principal)

    # Iniciamos el bucle principal de eventos de Tkinter.
    # Esta línea mantiene la ventana abierta y escuchando eventos
    # (clics, teclas, etc.) hasta que el usuario la cierra.
    ventana_principal.mainloop()
