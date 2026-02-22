# ============================================================
# producto.py - Clase Producto
# Representa un producto individual en el inventario
# Sin cambios estructurales, se mantiene igual que la versión anterior
# ============================================================

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con sus datos básicos.
        id       : número único para identificar el producto
        nombre   : nombre del producto (ej: "Manzanas")
        cantidad : unidades disponibles en stock
        precio   : precio unitario del producto
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # ── Getters ──────────────────────────────────────────────
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # ── Setters ──────────────────────────────────────────────
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # ── Representación en texto ───────────────────────────────
    def __str__(self):
        """Representación legible del producto para mostrar en consola."""
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}")

    def a_linea_csv(self):
        """
        Convierte el producto a una línea CSV para guardar en el archivo.
        Formato: id,nombre,cantidad,precio
        """
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def desde_linea_csv(linea):
        """
        Crea un Producto a partir de una línea CSV leída del archivo.
        Retorna un objeto Producto o lanza ValueError si la línea es inválida.
        """
        partes = linea.strip().split(",")
        if len(partes) != 4:
            raise ValueError(f"Línea con formato incorrecto: '{linea.strip()}'")
        id_prod  = int(partes[0])
        nombre   = partes[1]
        cantidad = int(partes[2])
        precio   = float(partes[3])
        return Producto(id_prod, nombre, cantidad, precio)
