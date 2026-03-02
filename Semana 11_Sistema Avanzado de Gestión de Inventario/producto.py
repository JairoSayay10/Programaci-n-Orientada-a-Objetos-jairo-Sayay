# ============================================================
# producto.py - Clase Producto
# Representa un artículo del inventario de la tienda
# NUEVO: se añade categoría al producto (almacenada como tupla)
# ============================================================

# Categorías válidas para los productos (uso de TUPLA porque no cambian)
CATEGORIAS_VALIDAS = ("alimentos", "bebidas", "limpieza", "higiene", "otros")


class Producto:
    def __init__(self, id, nombre, cantidad, precio, categoria="otros"):
        """
        Crea un nuevo producto con sus datos principales.

        Parámetros:
        - id        : número entero único para identificar el producto
        - nombre    : nombre del producto (ej: "Manzanas")
        - cantidad  : cuántas unidades hay en stock
        - precio    : precio por unidad
        - categoria : tipo de producto (por defecto "otros")
        """
        self.id        = id
        self.nombre    = nombre
        self.cantidad  = cantidad
        self.precio    = precio
        # Si la categoría no es válida, se asigna "otros" automáticamente
        self.categoria = categoria if categoria in CATEGORIAS_VALIDAS else "otros"

    # ── Getters (métodos para obtener los valores) ────────────
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def get_categoria(self):
        return self.categoria

    # ── Setters (métodos para cambiar los valores) ────────────
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def set_categoria(self, categoria):
        # Solo se acepta si la categoría es una de las válidas
        if categoria in CATEGORIAS_VALIDAS:
            self.categoria = categoria
        else:
            print(f"⚠️  Categoría inválida. Se mantendrá '{self.categoria}'.")

    # ── Cómo se ve el producto en consola ────────────────────
    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Cantidad: {self.cantidad} | Precio: ${self.precio:.2f} | "
                f"Categoría: {self.categoria}")

    # ── Métodos para guardar y cargar desde archivo ───────────
    def a_linea_csv(self):
        """Convierte el producto a texto CSV para guardarlo en el archivo."""
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio},{self.categoria}\n"

    @staticmethod
    def desde_linea_csv(linea):
        """
        Recrea un Producto a partir de una línea de texto del archivo.
        Si la línea está mal formada, lanza un ValueError.
        """
        partes = linea.strip().split(",")
        # Aceptamos 4 partes (versión vieja sin categoría) o 5 (versión nueva)
        if len(partes) not in (4, 5):
            raise ValueError(f"Línea con formato incorrecto: '{linea.strip()}'")
        id_prod   = int(partes[0])
        nombre    = partes[1]
        cantidad  = int(partes[2])
        precio    = float(partes[3])
        categoria = partes[4] if len(partes) == 5 else "otros"
        return Producto(id_prod, nombre, cantidad, precio, categoria)
