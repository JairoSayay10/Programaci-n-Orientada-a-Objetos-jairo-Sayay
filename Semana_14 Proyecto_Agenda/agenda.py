import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # El componente que instalamos para la fecha

class AplicacionAgenda:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda Personal - UEA")
        self.ventana.geometry("650x500")

        # --- 1. ORGANIZACIÓN POR FRAMES (CONTENEDORES) ---
        # Frame Superior: Entrada de datos
        self.frame_datos = tk.LabelFrame(self.ventana, text="Registrar Nuevo Evento", padx=10, pady=10)
        self.frame_datos.pack(padx=20, pady=10, fill="x")

        # Frame Central: Lista de eventos (TreeView)
        self.frame_lista = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

        # Frame Inferior: Botones de control
        self.frame_controles = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_controles.pack(fill="x")

        # Llamada a los métodos para dibujar la interfaz
        self.crear_interfaz_entrada()
        self.crear_tabla()
        self.crear_botones()

    def crear_interfaz_entrada(self):
        """Crea los campos para que el usuario escriba"""
        # Etiqueta y Selector de Fecha (DatePicker)
        tk.Label(self.frame_datos, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.txt_fecha = DateEntry(self.frame_datos, width=12, background='darkblue', 
                                   foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.txt_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y Campo de Hora
        tk.Label(self.frame_datos, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.txt_hora = tk.Entry(self.frame_datos)
        self.txt_hora.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y Campo de Descripción
        tk.Label(self.frame_datos, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.txt_desc = tk.Entry(self.frame_datos, width=50)
        self.txt_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    def crear_tabla(self):
        """Configura el Treeview para mostrar los eventos guardados"""
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings")
        
        # Encabezados de la tabla
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción del Evento")
        
        # Configurar anchos
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=350)

        # Agregar barra de desplazamiento (Scrollbar)
        scroll = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def crear_botones(self):
        """Crea los botones de acción con colores para mejor diseño"""
        btn_agregar = tk.Button(self.frame_controles, text="Agregar Evento", 
                                 command=self.accion_agregar, bg="#28a745", fg="white", width=15)
        btn_agregar.pack(side="left", padx=10, expand=True)

        btn_eliminar = tk.Button(self.frame_controles, text="Eliminar Seleccionado", 
                                  command=self.accion_eliminar, bg="#dc3545", fg="white", width=20)
        btn_eliminar.pack(side="left", padx=10, expand=True)

        btn_salir = tk.Button(self.frame_controles, text="Salir", 
                               command=self.ventana.quit, bg="#6c757d", fg="white", width=10)
        btn_salir.pack(side="left", padx=10, expand=True)

    # --- LÓGICA DE LA APLICACIÓN ---

    def accion_agregar(self):
        """Toma los datos de los campos y los sube a la tabla"""
        fecha = self.txt_fecha.get()
        hora = self.txt_hora.get()
        desc = self.txt_desc.get()

        if hora.strip() == "" or desc.strip() == "":
            messagebox.showwarning("Campos vacíos", "Por favor, completa la hora y la descripción.")
            return

        # Insertar datos en la tabla (TreeView)
        self.tree.insert("", "end", values=(fecha, hora, desc))
        
        # Limpiar campos después de agregar
        self.txt_hora.delete(0, tk.END)
        self.txt_desc.delete(0, tk.END)

    def accion_eliminar(self):
        """Elimina la fila seleccionada con confirmación"""
        seleccion = self.tree.selection() # Obtiene lo que el usuario marcó
        
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un evento de la lista para eliminarlo.")
            return

        # Diálogo de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este evento?")
        if respuesta:
            for fila in seleccion:
                self.tree.delete(fila)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionAgenda(root)
    root.mainloop()