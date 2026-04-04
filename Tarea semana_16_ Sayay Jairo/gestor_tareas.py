"""
Gestor de Tareas - Aplicación GUI con Tkinter
Autor: Jairo - Banco Pichincha
Descripción: Aplicación de gestión de tareas con interfaz gráfica,
             atajos de teclado y feedback visual.
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ──────────────────────────────────────────────
# PALETA DE COLORES Y CONSTANTES
# ──────────────────────────────────────────────
BG_DARK      = "#0f1117"
BG_PANEL     = "#1a1d27"
BG_CARD      = "#22263a"
BG_ENTRY     = "#2c3150"
ACCENT_BLUE  = "#4f8ef7"
ACCENT_GREEN = "#3ecf8e"
ACCENT_RED   = "#f76c6c"
ACCENT_GOLD  = "#f5c518"
TEXT_MAIN    = "#e8eaf0"
TEXT_MUTED   = "#7b82a0"
TEXT_DONE    = "#4a5270"
BORDER       = "#2e3350"

FONT_TITLE   = ("Courier New", 22, "bold")
FONT_SUB     = ("Courier New", 10)
FONT_BTN     = ("Courier New", 10, "bold")
FONT_TASK    = ("Courier New", 12)
FONT_TAG     = ("Courier New", 9)
FONT_ENTRY   = ("Courier New", 13)
FONT_HINT    = ("Courier New", 9)


# ──────────────────────────────────────────────
# CLASE PRINCIPAL
# ──────────────────────────────────────────────
class GestorTareas:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.tareas: list[dict] = []   # {"texto": str, "completada": bool, "hora": str}
        self._configurar_ventana()
        self._construir_ui()
        self._registrar_atajos()
        self._actualizar_contador()

    # ── Configuración de la ventana ────────────
    def _configurar_ventana(self):
        self.root.title("✦ Gestor de Tareas")
        self.root.geometry("680x700")
        self.root.minsize(560, 500)
        self.root.configure(bg=BG_DARK)
        self.root.resizable(True, True)
        # Centrar en pantalla
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  - 680) // 2
        y = (self.root.winfo_screenheight() - 700) // 2
        self.root.geometry(f"+{x}+{y}")

    # ── Construcción de la interfaz ────────────
    def _construir_ui(self):
        # ---- Encabezado ----
        header = tk.Frame(self.root, bg=BG_DARK, pady=20)
        header.pack(fill="x", padx=30)

        tk.Label(header, text="✦ GESTOR DE TAREAS",
                 font=FONT_TITLE, bg=BG_DARK, fg=TEXT_MAIN).pack(anchor="w")
        tk.Label(header, text="Organiza. Completa. Elimina.",
                 font=FONT_SUB, bg=BG_DARK, fg=TEXT_MUTED).pack(anchor="w", pady=(2, 0))

        # Separador decorativo
        sep = tk.Frame(self.root, bg=ACCENT_BLUE, height=2)
        sep.pack(fill="x", padx=30)

        # ---- Panel de entrada ----
        panel_entrada = tk.Frame(self.root, bg=BG_PANEL, pady=18)
        panel_entrada.pack(fill="x", padx=30, pady=(18, 0))

        tk.Label(panel_entrada, text="NUEVA TAREA", font=FONT_TAG,
                 bg=BG_PANEL, fg=ACCENT_BLUE).pack(anchor="w", padx=20)

        fila_entrada = tk.Frame(panel_entrada, bg=BG_PANEL)
        fila_entrada.pack(fill="x", padx=20, pady=(6, 0))

        self.entrada = tk.Entry(
            fila_entrada, font=FONT_ENTRY,
            bg=BG_ENTRY, fg=TEXT_MAIN,
            insertbackground=ACCENT_BLUE,
            relief="flat", bd=0,
            highlightthickness=2,
            highlightbackground=BORDER,
            highlightcolor=ACCENT_BLUE
        )
        self.entrada.pack(side="left", fill="x", expand=True,
                          ipady=10, ipadx=12)

        btn_add = self._boton(
            fila_entrada, "＋ AÑADIR", self.agregar_tarea,
            color=ACCENT_BLUE, padx=16
        )
        btn_add.pack(side="left", padx=(10, 0))

        tk.Label(panel_entrada, text="↵ Enter para añadir",
                 font=FONT_HINT, bg=BG_PANEL, fg=TEXT_MUTED).pack(anchor="w", padx=20, pady=(4, 0))

        # ---- Barra de acciones ----
        barra = tk.Frame(self.root, bg=BG_DARK, pady=12)
        barra.pack(fill="x", padx=30)

        self.lbl_contador = tk.Label(barra, text="", font=FONT_HINT,
                                     bg=BG_DARK, fg=TEXT_MUTED)
        self.lbl_contador.pack(side="left")

        btn_del  = self._boton(barra, "⊗ ELIMINAR",  self.eliminar_tarea,  color=ACCENT_RED,   padx=12)
        btn_comp = self._boton(barra, "✓ COMPLETAR", self.completar_tarea, color=ACCENT_GREEN, padx=12)
        btn_del.pack(side="right", padx=(6, 0))
        btn_comp.pack(side="right")

        # ---- Lista de tareas ----
        marco_lista = tk.Frame(self.root, bg=BG_DARK)
        marco_lista.pack(fill="both", expand=True, padx=30, pady=(0, 6))

        tk.Label(marco_lista, text="TAREAS PENDIENTES / COMPLETADAS",
                 font=FONT_TAG, bg=BG_DARK, fg=TEXT_MUTED).pack(anchor="w", pady=(0, 6))

        contenedor = tk.Frame(marco_lista, bg=BG_PANEL,
                              highlightthickness=1, highlightbackground=BORDER)
        contenedor.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(contenedor, bg=BG_PANEL, troughcolor=BG_PANEL,
                              relief="flat", bd=0)
        scroll.pack(side="right", fill="y")

        self.lista = tk.Listbox(
            contenedor,
            yscrollcommand=scroll.set,
            font=FONT_TASK,
            bg=BG_PANEL, fg=TEXT_MAIN,
            selectbackground=ACCENT_BLUE,
            selectforeground=BG_DARK,
            activestyle="none",
            relief="flat", bd=0,
            highlightthickness=0,
            selectmode="single",
            cursor="hand2"
        )
        self.lista.pack(fill="both", expand=True, padx=4, pady=4)
        scroll.config(command=self.lista.yview)

        # ---- Barra de atajos ----
        pie = tk.Frame(self.root, bg=BG_DARK, pady=10)
        pie.pack(fill="x", padx=30)

        atajos_txt = (
            "  ↵ Añadir   ·   C  Completar   ·   "
            "Del / D  Eliminar   ·   Esc  Salir  "
        )
        tk.Label(pie, text=atajos_txt, font=FONT_HINT,
                 bg=BG_DARK, fg=TEXT_MUTED).pack(side="left")

    # ── Botón reutilizable ─────────────────────
    def _boton(self, parent, texto, comando, color=ACCENT_BLUE, padx=14):
        btn = tk.Button(
            parent, text=texto, command=comando,
            font=FONT_BTN, bg=color, fg=BG_DARK,
            relief="flat", bd=0, cursor="hand2",
            padx=padx, pady=8,
            activebackground=color, activeforeground=BG_DARK
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=self._aclarar(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        return btn

    @staticmethod
    def _aclarar(hex_color: str) -> str:
        """Aclara un color hexadecimal un 20 % para el hover."""
        r = min(255, int(hex_color[1:3], 16) + 40)
        g = min(255, int(hex_color[3:5], 16) + 40)
        b = min(255, int(hex_color[5:7], 16) + 40)
        return f"#{r:02x}{g:02x}{b:02x}"

    # ── Registro de atajos ─────────────────────
    def _registrar_atajos(self):
        self.root.bind("<Return>",  lambda e: self.agregar_tarea())
        self.root.bind("<c>",       lambda e: self.completar_tarea())
        self.root.bind("<C>",       lambda e: self.completar_tarea())
        self.root.bind("<Delete>",  lambda e: self.eliminar_tarea())
        self.root.bind("<d>",       lambda e: self.eliminar_tarea())
        self.root.bind("<D>",       lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>",  lambda e: self.salir())

    # ── Lógica de la aplicación ────────────────
    def agregar_tarea(self):
        texto = self.entrada.get().strip()
        if not texto:
            self._flash_entry()
            return
        hora = datetime.now().strftime("%H:%M")
        self.tareas.append({"texto": texto, "completada": False, "hora": hora})
        self._refrescar_lista()
        self.entrada.delete(0, tk.END)
        self._actualizar_contador()
        # Seleccionar la última tarea añadida
        idx = len(self.tareas) - 1
        self.lista.selection_clear(0, tk.END)
        self.lista.selection_set(idx)
        self.lista.see(idx)

    def completar_tarea(self):
        idx = self._indice_seleccionado()
        if idx is None:
            return
        self.tareas[idx]["completada"] = not self.tareas[idx]["completada"]
        self._refrescar_lista()
        self.lista.selection_set(idx)
        self._actualizar_contador()

    def eliminar_tarea(self):
        idx = self._indice_seleccionado()
        if idx is None:
            return
        tarea = self.tareas[idx]["texto"]
        if messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Eliminar la tarea?\n\n«{tarea}»",
            parent=self.root
        ):
            self.tareas.pop(idx)
            self._refrescar_lista()
            # Mantener selección cercana
            nuevo_idx = min(idx, len(self.tareas) - 1)
            if nuevo_idx >= 0:
                self.lista.selection_set(nuevo_idx)
            self._actualizar_contador()

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?",
                                  parent=self.root):
            self.root.destroy()

    # ── Helpers internos ───────────────────────
    def _indice_seleccionado(self) -> int | None:
        sel = self.lista.curselection()
        if not sel:
            messagebox.showinfo("Sin selección",
                                "Selecciona una tarea de la lista primero.",
                                parent=self.root)
            return None
        return sel[0]

    def _refrescar_lista(self):
        self.lista.delete(0, tk.END)
        for t in self.tareas:
            if t["completada"]:
                etiqueta = f"  ✓  {t['texto']}  [{t['hora']}]"
                self.lista.insert(tk.END, etiqueta)
                idx = self.lista.size() - 1
                self.lista.itemconfig(idx, fg=TEXT_DONE,
                                      selectforeground=TEXT_DONE)
            else:
                etiqueta = f"  ○  {t['texto']}  [{t['hora']}]"
                self.lista.insert(tk.END, etiqueta)
                idx = self.lista.size() - 1
                self.lista.itemconfig(idx, fg=TEXT_MAIN,
                                      selectforeground=BG_DARK)

    def _actualizar_contador(self):
        total     = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t["completada"])
        pendientes  = total - completadas
        self.lbl_contador.config(
            text=f"Total: {total}  ·  Pendientes: {pendientes}  ·  Completadas: {completadas}"
        )

    def _flash_entry(self):
        """Parpadea el borde del Entry si se intenta añadir vacío."""
        self.entrada.config(highlightbackground=ACCENT_RED, highlightcolor=ACCENT_RED)
        self.root.after(600, lambda: self.entrada.config(
            highlightbackground=BORDER, highlightcolor=ACCENT_BLUE))
        self.entrada.focus_set()


# ──────────────────────────────────────────────
# PUNTO DE ENTRADA
# ──────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
